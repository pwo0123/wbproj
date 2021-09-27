from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
from .models import CFS
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django.core import serializers


@database_sync_to_async
def getinfo(self):
    return CFS.objects.all()


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        await self.send(await getinfo(self))



