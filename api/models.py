from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=20, default="Grade 12")
    strand     = models.CharField(max_length=20, default="STEM")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.strand}"

class AssessmentResult(models.Model):
    student        = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    strand         = models.CharField(max_length=20)
    riasec_scores  = models.JSONField(default=dict)
    mbti_type      = models.CharField(max_length=10)
    academic_scores = models.JSONField(default=dict)
    top_course     = models.CharField(max_length=100)
    match_score    = models.FloatField()
    taken_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.top_course}"

class CourseRecommendation(models.Model):
    assessment   = models.ForeignKey(AssessmentResult, on_delete=models.CASCADE, related_name="recommendations")
    course_name  = models.CharField(max_length=100)
    match_score  = models.FloatField()
    reason       = models.TextField()
    rank         = models.IntegerField()

    def __str__(self):
        return f"{self.course_name} ({self.match_score}%)"