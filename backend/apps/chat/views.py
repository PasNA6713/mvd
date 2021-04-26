from multiprocessing import Process

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .consumers import CURRENT_CHATS
from .services import send_to_user, send_to_all


def room(request):
    return render(request, 'room.html')

from loguru import logger
@logger.catch
@csrf_exempt
def send(request):
    token = request.headers.get('Authorization')
    if token is None: return HttpResponse(status=403)
    channel_name = CURRENT_CHATS.get(token.lstrip('Token').strip())
    if channel_name is None: return HttpResponse(status=500)

    for i in range(100):
        p = Process(target=send_to_all(i))
        p.start()
    return HttpResponse(status=200)