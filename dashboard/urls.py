from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('home/', views.dashboard_home, name='home'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]
