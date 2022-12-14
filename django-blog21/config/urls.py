"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from blog.views import create_comment, create_post, delete_comment, delete_post, post_detail, posts_list, update_comment, update_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_list),
    path('post_create/', create_post),
    path('post_detail/<int:post_id>/', post_detail),
    path('post_delete/<int:post_id>/', delete_post),
    path('post_update/<int:post_id>/', update_post),
    
    path('comment_create/', create_comment),
    path('comment_delete/<int:comment_id>/', delete_comment),
    path('comment_update/<int:comment_id>/', update_comment),
]
