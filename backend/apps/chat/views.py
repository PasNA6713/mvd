from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .consumers import CURRENT_CHATS


def room(request):
    return render(request, 'room.html')


@csrf_exempt
@async_to_sync
async def send(request):
    token = request.headers.get('Authorization')
    if token is None: return HttpResponse(status=403)
    channel_name = CURRENT_CHATS.get(token.lstrip('Token').strip())
    if channel_name is None: return HttpResponse(status=500)

    channel_layer = get_channel_layer()
    for i in range(100):
        await channel_layer.send(
            channel_name,
            {
                'type': 'chat_message',
                'message': str(i)
            }
        )
    return HttpResponse(status=200)