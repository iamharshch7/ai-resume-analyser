from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume
from .services import extract_resume_text
from analyzer.services import analyze_resume_logic # We will build this next

@login_required
def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume_file'):
        file = request.FILES['resume_file']

        # Validation: check extension
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in ['.pdf', '.docx']:
            messages.error(request, "Only PDF and DOCX files are allowed.")
            return redirect('resumes:upload')

        # Validation: check size (max 5MB)
        if file.size > 5 * 1024 * 1024:
            messages.error(request, "File size exceeds 5MB limit.")
            return redirect('resumes:upload')

        resume = Resume.objects.create(user=request.user, file=file)

        # Process and extract text
        text = extract_resume_text(resume.file.path)
        resume.extracted_text = text
        resume.save()

        # Trigger initial analysis
        analyze_resume_logic(resume)

        messages.success(request, "Resume uploaded and analyzed successfully!")
        return redirect('resumes:result', resume_id=resume.id)

    return render(request, 'resumes/upload.html')

@login_required
def analysis_result(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    analysis = getattr(resume, 'analysis', None)
    return render(request, 'resumes/result.html', {'resume': resume, 'analysis': analysis})

@login_required
def resume_history(request):
    resumes = request.user.resumes.all().order_by('-uploaded_at')
    return render(request, 'resumes/history.html', {'resumes': resumes})

@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    resume.delete()
    messages.success(request, "Resume deleted.")
    return redirect('resumes:history')

import os
