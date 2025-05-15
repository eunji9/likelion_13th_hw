from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from main.models import Post

# Create your views here.

@login_required
def mypage(request):
    # 로그인한 유저의 글만 가져오기
    posts = Post.objects.filter(writer=request.user)
    context = {
        'user':request.user,
        'posts':posts, #유저가 작성한 글 목록
    }
    return render(request, 'users/mypage.html', context)

