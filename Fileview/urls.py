"""Fileview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loadview', views.index),
    path('fileload', views.fileload),
    path('fileview', views.fileview),  # 页面展示
    path('queryfile', views.queryfile),
    path('login/', views.loginManager, ),
    path('loginVerify', views.loginVerify),
    path('filedown', views.filedown),
    path('keyQuery', views.keyQuery),
    path('deletefile', views.deletefile),
    # path('verifyuser',views.verifyuser),
    path('logoutuser', views.logoutuser)
]
