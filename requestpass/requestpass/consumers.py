from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Friend1Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to Friend2
        await self.channel_layer.group_send(
            'friend2_group',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def disconnect(self, close_code):
        pass

class Friend2Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('friend2_group', self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('friend2_group', self.channel_name)

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
