from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer
import mimetypes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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
        image_path = image.image.path
        # 自动检测文件的 MIME 类型
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = "application/octet-stream"  # 当类型无法识别时使用默认类型
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type=mime_type)
    else:
        return HttpResponse(status=404)