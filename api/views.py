from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import StudentProfile, AssessmentResult, CourseRecommendation
from .serializers import (
    RegisterSerializer, StudentProfileSerializer, AssessmentResultSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})
    return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    student = StudentProfile.objects.get(user=request.user)
    serializer = StudentProfileSerializer(student)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assessment_history(request):
    student = StudentProfile.objects.get(user=request.user)
    results = AssessmentResult.objects.filter(student=student).order_by('-taken_at')
    serializer = AssessmentResultSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_assessment(request):
    student = StudentProfile.objects.get(user=request.user)
    data    = request.data

    result = AssessmentResult.objects.create(
        student        = student,
        strand         = data.get('strand'),
        riasec_scores  = data.get('riasec_scores', {}),
        mbti_type      = data.get('mbti_type', ''),
        academic_scores = data.get('academic_scores', {}),
        top_course     = data.get('top_course', ''),
        match_score    = data.get('match_score', 0),
    )

    for rec in data.get('recommendations', []):
        CourseRecommendation.objects.create(
            assessment  = result,
            course_name = rec.get('course_name'),
            match_score = rec.get('match_score'),
            reason      = rec.get('reason', ''),
            rank        = rec.get('rank'),
        )

    return Response({'message': 'Assessment saved.', 'id': result.id},
                    status=status.HTTP_201_CREATED)