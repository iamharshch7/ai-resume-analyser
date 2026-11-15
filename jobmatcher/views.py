from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resumes.models import Resume

@login_required
def job_match_view(request):
    resumes = request.user.resumes.all().order_by('-uploaded_at')
    context = {'resumes': resumes}

    if request.method == 'POST':
        resume_id = request.POST.get('resume_id')
        job_description = request.POST.get('job_description')

        if resume_id and job_description:
            resume = request.user.resumes.get(id=resume_id)
            # Placeholder analysis logic
            match_score = 75 # Mock score
            context.update({
                'match_score': match_score,
                'matched_resume': resume,
                'job_description': job_description
            })

    return render(request, 'jobmatcher/match.html', context)
