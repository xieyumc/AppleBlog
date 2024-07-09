from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# 用于处理文章的常规CRUD操作
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 用于提供文章图片的视图函数
def post_image(request, post_id, image_index):
    post = get_object_or_404(Post, id=post_id)
    if post.cover_image:
        with open(post.cover_image.path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    else:
        # 如果没有图片，可以返回一个默认图片或404
        return HttpResponse(status=404)