from abstract.serializers import BaseSerializer
from .models import User

class UserSerializer(BaseSerializer):
    class Meta:
        fields = ['email', 'name', 'is_authorized']
        queryset = User.objects