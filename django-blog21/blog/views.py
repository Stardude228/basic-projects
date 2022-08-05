from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    title = request.query_params.get('title')
    if title:
        queryset = queryset.filter(title__icontains=title)
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Пост успешно создан')

@api_view(['GET'])
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response('Пост успешно удален')

@api_view(['PUT', 'PATCH'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(instance=post, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Пост успешно обновлен')

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Коммент успешно создан')

@api_view(['DELETE'])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return Response('Коммент успешно удален')

@api_view(['PUT', 'PATCH'])
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(instance=comment, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Коммент успешно обновлен')