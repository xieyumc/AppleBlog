"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import RegisterView
from WebConfig.views import web_config
from blog.views import PostViewSet, ImageViewSet, post_image
from django.urls import path, include



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("admin/", admin.site.urls),
    path('api/', include('blog.urls')),

    path('api/web_config', web_config, name='web_config'),

    path('api/img/post/<int:post_id>/<int:image_index>/', post_image, name='post_image'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)