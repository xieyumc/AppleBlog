from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer
import mimetypes
from django.core.cache import cache  # 引入缓存
from django.conf import settings  # 访问缓存超时配置
import hashlib  # 用于生成唯一缓存键


# 用于处理文章的常规CRUD操作
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # 检查缓存中是否有文章数据
        cached_queryset = cache.get('post_queryset')
        if cached_queryset:
            return cached_queryset

        # 如果缓存中没有数据，则查询数据库并缓存
        queryset = Post.objects.filter(available=True)
        cache.set('post_queryset', queryset, timeout=60 * 15)  # 缓存15分钟
        return queryset


# 用于提供文章图片的视图函数
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


def post_image(request, post_id, image_index):
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all().order_by('id')  # 按ID排序，确保顺序一致
    image_index -= 1  # 使索引从1开始计数

    if images and 0 <= image_index < len(images):
        image = images[image_index]

        # 生成唯一的缓存键，基于文章ID和图片索引
        cache_key = f'post_{post_id}_image_{image_index}'
        cached_image = cache.get(cache_key)

        if cached_image:
            # 从缓存中返回图片数据
            mime_type, _ = mimetypes.guess_type(image.image.path)
            if not mime_type:
                mime_type = "application/octet-stream"
            response = HttpResponse(cached_image, content_type=mime_type)
            response['Cache-Control'] = 'public, max-age=2592000'
            return response

        # 如果缓存中没有图片数据，则读取文件并缓存
        image_path = image.image.path
        with open(image_path, 'rb') as f:
            image_data = f.read()
            cache.set(cache_key, image_data, timeout=2592000)  # 缓存30天
            mime_type, _ = mimetypes.guess_type(image_path)
            if not mime_type:
                mime_type = "application/octet-stream"
            response = HttpResponse(image_data, content_type=mime_type)
            response['Cache-Control'] = 'public, max-age=2592000'
            return response
    else:
        return HttpResponse(status=404)