from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import VideosSerializer

class VideoAPIView(APIView):
    
    def post(self, request):
        serializer = VideosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Video created', status=200)
