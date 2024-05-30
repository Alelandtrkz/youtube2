

from django.shortcuts import render, redirect, HttpResponse
from app1.models import home_video_links
from app1.models import video_page_links
from app1.models import table_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


# Create your views here.

def home_page(reqest):
    data={
        'video':home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3':home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),

    }
    return render(reqest,'home.html', context=data)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = auth.authenticate(username =username, password=password)
        if my_user is None:
            auth.login(request,my_user)
            return redirect('http://127.0.0.1:8000')
        else:
            messages.info(request, 'invalid credentials')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.ifo(request, 'You are out')
    return redirect('http://127.0.0.1:8000')


def register_page(request):

    if request.method == 'POST':

        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Registrado {username}')
            return redirect('http://127.0.0.1:8000')
    else:
        form = UserRegisterForm()

    context = {'form' : form}

    return render(request, 'register.html', context)

def video_page(reqest):
    deta = {
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),


        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'likes': home_video_links.objects.get(id=1)
    }



    return render(reqest, 'video.html', context= deta,)




def video_2(reqest):

    dita={
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),

        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'comments': home_video_links.objects.get(id=5),
        'likes2': home_video_links.objects.get(id=2)

    }
    return  render(reqest,'video2.html', context=dita)

def video_3(reqest):

    dota={
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),

        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'likes3': home_video_links.objects.get(id=3)


    }
    return  render(reqest,'video3.html', context=dota)

def video_4(reqest):

    data={
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),

        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'likes4': home_video_links.objects.get(id=4)


    }
    return  render(reqest,'video4.html', context=data)

def video_5(reqest):

    data={
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),

        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'likes5': home_video_links.objects.get(id=5)


    }
    return  render(reqest,'video5.html', context=data)

def video_6(reqest):

    data={
        'vid1': video_page_links.objects.get(id=1),
        'vidt': home_video_links.objects.get(id=1),
        'vid2': home_video_links.objects.get(id=2),
        'vid3': home_video_links.objects.get(id=3),
        'vid4': home_video_links.objects.get(id=4),
        'vid5': home_video_links.objects.get(id=5),
        'vid6': home_video_links.objects.get(id=6),

        'video': home_video_links.objects.get(id=1),
        'video2': home_video_links.objects.get(id=2),
        'video3': home_video_links.objects.get(id=3),
        'video4': home_video_links.objects.get(id=4),
        'video5': home_video_links.objects.get(id=5),
        'video6': home_video_links.objects.get(id=6),
        'likes6': home_video_links.objects.get(id=6)


    }
    return  render(reqest,'video6.html', context=data)


def dar_likes(request):
    post = get_object_or_404(home_video_links,id =1)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/')