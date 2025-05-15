from django.urls import path
from .views import *
from . import views

app_name="users"

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
]