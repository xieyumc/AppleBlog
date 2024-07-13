from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer
# 用于处理文章的常规CRUD操作
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(available=True)

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
        with open(image.image.path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    else:
        return HttpResponse(status=404)