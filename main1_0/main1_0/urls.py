"""main1_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('/student',views.student,name="student"),
    path('/savestudent',views.savestudent,name="savestudent"),
    path('/loginstudent',views.loginstudent,name="loginstudent"),
    path('/regstudent',views.regstudent,name="regstudent"),
    path('/teacher',views.teacher,name="teacher"),
    path('/loginteacher',views.loginteacher,name="loginteacher"),
    path('/regteacher',views.regteacher,name="regteacher"),
    path('/saveteacher',views.saveteacher,name="saveteacher"),
    path('/institute',views.institute,name="institute"),
    path('/logininstitute',views.logininstitute,name="logininstitute"),
    path('/reginstitute',views.reginstitute,name="reginstitute"),
    path('/saveinstitute',views.saveinstitute,name="saveinstitute"),

]
