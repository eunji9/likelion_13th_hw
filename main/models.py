from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Post 모델을 main앱에만 정의하고, author 필드로 User와 관계를 설정
class Post(models.Model):
    title = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]