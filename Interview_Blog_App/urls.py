"""Interview_Blog_App URL Configuration

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
from Interview_Blog_App import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.IndexPage,name="ipage"),
    path('register/', views.Register,name="register"),
    path('login/', views.Login,name="login"),
    path('register/home/', views.Home,name="home"),
    path('login/home/', views.Home,name="home"),
    path('reg_info', views.Reg_Info,name="reg_info"),
    path('explore/', views.Explore,name="expolre"),
    path('add_new_exp/', views.Add_New_Exp,name="add_new_exp"),
    path('my_exp/', views.My_Exp,name="my_exp"),
    path('bookmarks/', views.Bookmarks,name="bookmarks"),

]
