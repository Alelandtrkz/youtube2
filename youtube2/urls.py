"""
URL configuration for youtube2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import home_page
from app1.views import login_page
from app1.views import register_page
from app1.views import video_page
from app1.views import video_2
from app1.views import video_3
from app1.views import video_4
from app1.views import video_5
from app1.views import video_6
from app1.views import dar_likes
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home_page),
    path('login', LoginView.as_view(template_name='login.html'), name= 'login'),
    path('register', register_page),
    path('video', video_page),
    path('You-Belong-With-Me', video_2),
    path('Ed-Maverick-Quiero', video_3),
    path('Genshin-impact', video_4),
    path('Kimetsu_no_Yaiba', video_5),
    path('Bilibili', video_6),
    path('account/', include ('django.contrib.auth.urls')),
    path('likes/',dar_likes, name ='dar_like'),
]
