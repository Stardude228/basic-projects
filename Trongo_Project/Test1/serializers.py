from rest_framework import serializers

from Test2.serializers import CommentSerializer

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["user"] = instance.user.username
        dict_["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        return dict_
