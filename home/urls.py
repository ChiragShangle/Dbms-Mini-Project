"""tnportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    
    path('courses',views.course,name='courses'),
    path('edit',views.edit,name='edit'),
    path('login',views.loginuser,name='login'),
    path('register',views.register,name='register'),
    path('student',views.student,name='student'),
    path('adminstrant',views.adminn,name='admin'),
    path('mailuser',views.mailuser,name='mailuser'),
    path('logout',views.logout_user,name='logout'),
    path('organization',views.organization,name='organization'),
    path('edit',views.edit,name='edit'),
    path('project',views.project,name='project'),
    path('profile',views.profile,name='profile'),
    path('academics',views.academics, name='academics'),
    path('record',views.record,name='record'),
    path('UCompany',views.upcom,name='UCompany'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminauth',views.adminauth,name='adminauth'),


   
]
