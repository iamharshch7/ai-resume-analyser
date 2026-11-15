from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('upload/', views.upload_resume, name='upload'),
    path('result/<int:resume_id>/', views.analysis_result, name='result'),
    path('history/', views.resume_history, name='history'),
    path('delete/<int:resume_id>/', views.delete_resume, name='delete'),
]
