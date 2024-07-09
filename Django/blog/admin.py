from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Image

# 注册Post模型
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pub_date', 'featured', 'theme')
    search_fields = ('title', 'author')
    list_filter = ('featured', 'theme', 'pub_date')
    date_hierarchy = 'pub_date'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ( 'post', 'Image_Number', 'alt_text', 'image')
    search_fields = ('post__title', 'alt_text')
    list_filter = ('post',)

    def Image_Number(self, obj):
        images = list(obj.post.images.all().order_by('id'))
        return images.index(obj) + 1
    Image_Number.short_description = 'Image_Number'