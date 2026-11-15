from django.db import models
from resumes.models import Resume

class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='analysis')
    overall_score = models.IntegerField()
    ats_score = models.IntegerField()
    technical_skills = models.TextField()
    soft_skills = models.TextField()
    education_analysis = models.TextField()
    experience_analysis = models.TextField()
    projects_analysis = models.TextField()
    missing_skills = models.TextField()
    grammar_suggestions = models.TextField() # JSON stored as text
    strengths = models.TextField() # JSON stored as text
    weaknesses = models.TextField() # JSON stored as text
    recommendations = models.TextField() # JSON stored as text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.resume.id}"
