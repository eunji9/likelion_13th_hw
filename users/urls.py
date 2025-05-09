from django.urls import path
from .views import *
from . import views

app_name="users"

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('new-post', new_post, name="new-post"),
    path('create', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"), 
]