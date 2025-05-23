from django.db import models
from django.contrib.auth.models import User

# Post 모델을 main앱에만 정의하고, writer 필드로 User와 관계를 설정
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]
    
class Comment(models.Model): 
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def str(self):
        return self.blog.title + " : " + self.content[:20] + "by" + self.writer.profile.nickname