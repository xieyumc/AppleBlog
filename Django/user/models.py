from django.db import models

# Create your models here.
# backend/app1/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    # 使用内置的 email 和 username 字段，确保 email 字段为必填项
    email = models.EmailField(unique=True, blank=False)

    # 收藏的文章，使用多对多关联
    favorites = models.ManyToManyField(Article, related_name='favorited_by', blank=True)
