from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CommentSerializer

from .models import Comment

@api_view(['GET'])
def comments_list(request):
    queryset = Comment.objects.all()
    serializer = CommentSerializer(instance=queryset, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_comment(request, comment_id):
    serializer = CommentSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Коммент успешно создан")

@api_view(["GET"])
def comment_detail(request, post_id):
    comment = get_object_or_404(Comment, id=post_id)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(["DELETE"])
def comment_delete(request, post_id):
    post = get_object_or_404(Comment, id=post_id)
    post.delete()
    return Response("Коммент успешно удален")

@api_view(["PUT", "PATCH"])
def comment_update(request, post_id):
    post = get_object_or_404(Comment, id=post_id)
    serializer = CommentSerializer(instance=post, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Коммент успешно обновлен")