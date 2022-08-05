"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Test2.views import comment_delete, comment_detail, comment_update, comments_list, create_comment

from Test1.views import create_post, post_delete, post_detail, post_update, posts_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_list),
    path('post_create/', create_post),
    path('post_detail/<int:post_id>/', post_detail),
    path('post_delete/<int:post_id>/', post_delete),
    path('post_update/<int:post_id>/', post_update),
    path('comments/', comments_list),
    path('comment_create/<int:post_id>/', create_comment),
    # path('comment_detail/<int:post_id>/', comment_detail),
    # path('comment_delete/<int:post_id>/', comment_delete),
    # path('comment_update/<int:post_id>/', comment_update),
]
