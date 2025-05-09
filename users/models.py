from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)

    #난이도 선택하게 하기
    DIFFICULTY_CHOICES = [
        ('easy', '쉬움'),
        ('normal', '보통'),
        ('hard', '어려움'),
    ]
    difficulty = models.CharField(
        max_length=6, 
        choices=DIFFICULTY_CHOICES,  # difficulty 필드에서 선택할 수 있는 값들
        default='normal',  # 기본값은 '보통'
    )

    content = models.TextField()
    pub_date = models.DateField()
    #글 작성자 추가 (User 모델과 연결)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]