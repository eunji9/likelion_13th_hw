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
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments': comments})
    
    elif request.method == 'POST':
        new_comment=Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now() 
        new_comment.save()
        return redirect('main:detail', id)

def create(request):
    if request.user.is_authenticated:
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.writer = request.user #로그인한 유저를 작성자로 설정
        new_post.difficulty = request.POST['difficulty']
        new_post.content = request.POST['content']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')
        new_post.save()
        
        import re #tag에서 띄어쓰기, 줄바꿈 등의 모든 공백을 대상으로 만들 때 사용
        words = re.split(r'\s+',new_post.content.strip()) #공백을 기준으로 분리. 원래는 split(' ')을 이용하여 or의 방식으로 ' '와 '\n'을 나타낼 수 있는지 보았지만 불가능한듯 ㅠ
        tag_list = []
        #나눈 단어가 '#'으로 시작한다면 tag_list에 저장
        for w in words:
            if w.startswith('#') and len(w)>1:
                tag_list.append(w[1:]) #tag_list에 있는 Tag들을 new_post의 tags에 추가
                    
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})

def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.difficulty = request.POST['difficulty']
        update_post.content = request.POST['content']
        update_post.pub_date = timezone.now()

        if request.FILES.get('image'):
            update_post.image = request.FILES.get('image')
        update_post.save()

        import re
        #해시태그 추출하기
        words = re.split(r'\s+',update_post.content.strip())

        #중간에,, 먼저..! 기존 태그 삭제
        update_post.tags.clear()

        tag_list=[]
        for w in words:
            if w.startswith('#') and len(w)>1:
                tag_list.append(w[1:])
                    
        for t in tag_list:
            tag, boolean=Tag.objects.get_or_create(name=t)
            update_post.tags.add(tag.id)

        return redirect('main:detail', update_post.id)
    return redirect('accounts:login', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:freepage')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('main:detail', comment.post.id)

def tag_list(request): #모든 태그 목록을 볼 수 있는 페이지
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags': tags})

def tag_posts(request, tag_id): #특정 태그를 가진 게시글의 목록을 볼 수 있는 페이지
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })

def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)