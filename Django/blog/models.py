from django.db import models

class Post(models.Model):
    THEME_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()  # 存储Markdown内容
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    author = models.CharField(max_length=100)
    cover_url = models.URLField(blank=True, null=True)
    # cover_square = models.URLField(blank=True, null=True)  # 正方形封面图像URL
    # cover_alt = models.CharField(max_length=255, blank=True, null=True)  # 封面图像描述
    tags = models.CharField(max_length=200, blank=True, null=True)
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='light')  # 主题，限定为 'light' 或 'dark'
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title