from django.contrib import admin

from Test2.models import Comment
from .models import Post

admin.site.register(Post)
admin.site.register(Comment)