from django.contrib import admin
from .models import StudentProfile, AssessmentResult, CourseRecommendation

admin.site.register(StudentProfile)
admin.site.register(AssessmentResult)
admin.site.register(CourseRecommendation)