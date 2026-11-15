from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def landing_view(request):
    return render(request, 'dashboard/landing.html')

@login_required
def dashboard_home(request):
    resumes = request.user.resumes.all().order_by('-uploaded_at')
    context = {
        'resumes': resumes,
        'total_analyzed': resumes.count(),
        'latest_resume': resumes.first() if resumes.exists() else None
    }
    return render(request, 'dashboard/home.html', context)

@staff_member_required
def admin_dashboard_view(request):
    return render(request, 'dashboard/admin.html')
