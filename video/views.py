from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer


# Create your views here.
class RoomAPIView(APIView):
    def post(self, request, format=None):
        room = Room.objects.create()
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
