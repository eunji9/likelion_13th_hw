from django.db import models
from django.contrib.auth.models import User 
from main.models import Post #main앱의 Post모델을 import

# Create your models here.
class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #유저와 연결
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #Post 모델과 연결

    def __str__(self):
        return f"User {self.user.username} Post {self.post.title}"
    
    def summary(self):
        return self.post.summary()