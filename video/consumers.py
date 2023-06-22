import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class SignalingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["roomID"]
        self.room_group_name = "signaling_%s" % self.room_name

        # Get the channel layer
        self.channel_layer = get_channel_layer()

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive signaling message from WebSocket
    async def receive(self, text_data):
        message = json.loads(text_data)
        signaling_message = {
            "type": message.get("type", None),
            "sdp": message.get("sdp", None),
        }
        ice_candidate = message.get("ice_candidate", None)
        type = message.get("type", None)
        if type == "disconnect":
            # Send disconnect signaling message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_signaling_message",
                    "message_type": "disconnect",
                    "sender_channel": self.channel_name,
                    "exclude": [self.channel_name],
                },
            )
        if type == "camera-true" or type == "camera-false":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_signaling_message",
                    "message_type": type,
                    "sender_channel": self.channel_name,
                    "exclude": [self.channel_name],
                },
            )
        if type == "audio-true" or type == "audio-false":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_signaling_message",
                    "message_type": type,
                    "sender_channel": self.channel_name,
                    "exclude": [self.channel_name],
                },
            )

        if signaling_message["type"] is not None and signaling_message["sdp"] is not None:
            # Send signaling message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_signaling_message",
                    "message_type": signaling_message["type"],
                    "offer": signaling_message["sdp"],
                    "ice_candidate": ice_candidate,
                    "sender_channel": self.channel_name,
                    "exclude": [self.channel_name],
                },
            )
        else:
            # Handle invalid message
            pass

    # Receive signaling message from room group
    async def send_signaling_message(self, event):
        sdp = event.get("offer")
        ice_candidate = event.get("ice_candidate")
        message_type = event.get("message_type")
        print(message_type)
        sender_channel = event.get("sender_channel")
        if self.channel_name != sender_channel:
            # Send signaling message to WebSocket
            await self.send(
                text_data=json.dumps(
                    {
                        "type": message_type,
                        "sdp": sdp,
                        "ice_candidate": ice_candidate,
                    }
                )
            )
