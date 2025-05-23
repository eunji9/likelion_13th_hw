from django.urls import path
from .views import *
from . import views

app_name="users"

urlpatterns = [
    path('mypage/<int:user_id>', views.mypage, name='mypage'),
    path('follow/<int:id>', follow, name="follow"),
]