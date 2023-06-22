from django.urls import re_path

from video import consumers

websocket_urlpatterns = [
    re_path(r"ws/signaling/(?P<roomID>\w+)/$", consumers.SignalingConsumer.as_asgi()),
]
