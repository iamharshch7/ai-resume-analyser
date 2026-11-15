from django.db import models
from django.contrib.auth.models import User
import os

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Resume - {self.uploaded_at.strftime('%Y-%m-%d')}"
