from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_user_info/', views.edit_user_info, name='edit_user_info'),
    
    path('upload/', views.upload_pdf, name='upload_pdf'),

]

