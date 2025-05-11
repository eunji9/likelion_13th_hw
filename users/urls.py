from django.urls import path
from .views import *
from . import views

app_name="users"

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('new-post', views.new_post, name="new-post"),
    path('create', views.create, name="create"),
    path('<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"), 
]