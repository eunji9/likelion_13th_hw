from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

@login_required
def mypage(request):
    # 로그인한 유저의 글만 가져오기
    posts = Post.objects.filter(author=request.user)
    context = {
        'user':request.user,
        'posts':posts, #유저가 작성한 글 목록
    }
    return render(request, 'users/mypage.html', context)

@login_required
def new_post(request):
    return render(request, 'users/new-post.html')

@login_required
def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'users/detail.html', {'post': post})

@login_required  
def create(request):
    if request.method == 'POST':
        new_post = Post()
        new_post.title = request.POST['title']        
        new_post.difficulty = request.POST['difficulty']
        new_post.content = request.POST['content']
        new_post.pub_date = timezone.now()
        new_post.author = request.user  # 작성자는 로그인한 유저로 설정
        new_post.save()
        return redirect('users:detail', new_post.id)
    else:
        return render(request, 'users/new-post.html')

@login_required
def edit(request, id):
    edit_post = get_object_or_404(Post, pk=id, author=request.user)  # 로그인한 유저의 글만 수정 가능
    return render(request, 'users/edit.html', {"post": edit_post})

@login_required
def update(request, id):
    update_post = get_object_or_404(Post, pk=id, author=request.user)  
    if request.method == 'POST':
        update_post.title = request.POST['title']
        update_post.difficulty = request.POST['difficulty']
        update_post.content = request.POST['content']
        update_post.pub_date = timezone.now()
        update_post.save()
        return redirect('users:detail', update_post.id)
    return render(request, 'users/edit.html', {'post': update_post})

@login_required
def delete(request, id):
    delete_post = get_object_or_404(Post, pk=id, author=request.user) 
    delete_post.delete()
    return redirect('users:mypage')