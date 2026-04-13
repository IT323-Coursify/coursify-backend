from django.urls import path
from . import views

urlpatterns = [
    path('register/',           views.register,           name='register'),
    path('login/',              views.login,              name='login'),
    path('profile/',            views.profile,            name='profile'),
    path('assessment/submit/',  views.submit_assessment,  name='submit-assessment'),
    path('assessment/history/', views.assessment_history, name='assessment-history'),
    
]