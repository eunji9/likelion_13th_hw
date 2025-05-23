from django.urls import path
from .views import *
from . import views

app_name = "main"
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('new-post/', views.new_post, name="new-post"),
    path('free/', views.freepage, name="freepage"),
    path('create', views.create, name="create"),
    path('<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name="delete_comment"),
    path('tag-list', views.tag_list, name="tag-list"),
    path('tag-posts/<int:tag_id>', views.tag_posts, name="tag-posts"),
    path('likes/<int:post_id>',likes, name="likes"),
]