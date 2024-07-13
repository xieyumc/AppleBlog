from django.db import models

class Post(models.Model):
    THEME_CHOICES = (
        ('light', 'AUTO'),
        ('dark', 'Dark'),
    )
    available = models.BooleanField(default=True)  # 用于标记文章是否可见
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()  # 存储Markdown内容
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100)
    cover_url = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='light')  # 主题，限定为 'light' 或 'dark'
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)