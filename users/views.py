from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from main.models import Post

# Create your views here.

@login_required
def mypage(request, user_id):
    # 로그인한 유저의 글만 가져오기
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(writer=user)
    context = {
        'user':user,
        'posts':posts, #유저가 작성한 글 목록
    }
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)