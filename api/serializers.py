from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentProfile, AssessmentResult, CourseRecommendation

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        StudentProfile.objects.create(user=user)
        return user

class StudentProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email    = serializers.CharField(source='user.email',    read_only=True)

    class Meta:
        model  = StudentProfile
        fields = ['username', 'email', 'grade_level', 'strand', 'created_at']

class CourseRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CourseRecommendation
        fields = ['rank', 'course_name', 'match_score', 'reason']

class AssessmentResultSerializer(serializers.ModelSerializer):
    recommendations = CourseRecommendationSerializer(many=True, read_only=True)

    class Meta:
        model  = AssessmentResult
        fields = ['id', 'strand', 'riasec_scores', 'mbti_type',
                  'academic_scores', 'top_course', 'match_score',
                  'taken_at', 'recommendations']