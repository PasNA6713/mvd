from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import SessionModel
from .services import send_to_user, send_to_all
from .tasks import celery_send_all


def room(request):
    return render(request, 'room.html')

@csrf_exempt
def send(request):
    token = request.headers.get('Authorization')
    if token is None: return HttpResponse(status=403)
    channel_name = SessionModel.objects.get(pk=token.lstrip('Token').strip()).session
    if channel_name is None: return HttpResponse(status=204)

    for i in range(100):
        celery_send_all.delay(i)
    return HttpResponse(status=200)