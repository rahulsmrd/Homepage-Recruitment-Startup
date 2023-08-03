"""startup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/<pk>/', views.SignUp, name='signup'),
    path('skilltest/', views.skilltest, name='skill_test'),
    path('posts/', views.postlist.as_view(), name='posts'),
    path('createPost/',views.createpost.as_view(), name='create_post'),
    path("login/",auth_views.LoginView.as_view(template_name='home/login.html'),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path('login/', views.Login, name='login'),
]
