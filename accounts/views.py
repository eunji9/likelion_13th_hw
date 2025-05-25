from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        age = request.POST['age']
        mbti = request.POST['mbti']

        if password == confirm:
            # username 중복 확인
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/signup.html', {'error': '이미 사용중인 아이디에용..!'})
            else:
                # User 생성 가능
                user = User.objects.create_user(username=username, password=password)

                # receiver로 생성된 Profile에 age, mbti 저장
                user.profile.age = age
                user.profile.mbti = mbti
                user.profile.save()

                auth.login(request, user)
                return redirect('/')
        
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않아용..😅'})

    return render(request, 'accounts/signup.html')