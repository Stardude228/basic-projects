from abstract.serializers import BaseSerializer

from .models import Category, Product, Comment

class CategorySerializer(BaseSerializer):
    class Meta:
        fields = ['title']
        queryset = Category.objects
    
class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ['id_', 'title', 'price', 'description', 'quantity', 'category']
        queryset = Product.objects
    
    def serialize_object(self, object_):
        dict_ = super().serialize_object(object_)
        dict_['category'] = object_.category.title
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ['body', 'created_at']
        queryset = Comment.objects