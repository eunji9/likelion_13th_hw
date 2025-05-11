from django.urls import path
from .views import *
from . import views

app_name = "main"
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('free/', views.freepage, name="freepage"),
    path('new-post', new_post, name="new-post"),
    path('create', create, name="create"),
    path('<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),    
]