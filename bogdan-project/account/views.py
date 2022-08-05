from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, CheckSerializer

User = get_user_model()

class RegisterAPIView(APIView):

    def get(self, request):
        query = User.objects.all()
        serializer = CheckSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Успешно зарегистрировались', status=201)
