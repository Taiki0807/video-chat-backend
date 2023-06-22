from django.urls import path

from .views import RoomAPIView

urlpatterns = [
    path("room", RoomAPIView.as_view(), name="room"),
]
