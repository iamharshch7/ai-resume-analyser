from django.urls import path
from . import views

app_name = 'jobmatcher'

urlpatterns = [
    path('', views.job_match_view, name='match'),
]
