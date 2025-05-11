from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import *
from .models import Post

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')

def freepage(request):
    posts = Post.objects.all()
    print(posts) #글이 제대로 로드되었는지 확인
    return render(request, 'main/freepage.html',{'posts': posts})

def new_post(request):
    return render(request, 'main/new-post.html')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post': post})

def create(request):
    if request.method =='POST':
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.difficulty = request.POST['difficulty']
        new_post.content = request.POST['content']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')
        new_post.author = request.user #로그인한 유저를 작성자로 설정
        new_post.save()       
        return redirect('main:freepage')
    return render(request, 'users/new-post.html')

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})

def update(request, id):
    update_post = Post.objects.get(pk=id)
    update_post.title = request.POST['title']
    update_post.difficulty = request.POST['difficulty']
    update_post.content = request.POST['content']
    update_post.pub_date = timezone.now()
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:freepage')