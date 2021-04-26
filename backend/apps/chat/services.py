from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from .consumers import CURRENT_CHATS


def send_to_user(channel_name: str, message: str) -> None:
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(
        channel_name, {
            'type': 'chat_message',
            'message': str(message)
        })

def send_to_all(message: str) -> None:
    channel_layer = get_channel_layer()
    for user in CURRENT_CHATS.values():
        send_to_user(user, message)


async def a_send(channel_name, message: str) -> None:
    channel_layer = get_channel_layer()
    await channel_layer.send(
        channel_name, {
            'type': 'chat_message',
            'message': str(message)
    })


async def a_send_all(message: str) -> None:
    for user in CURRENT_CHATS.values():
        await a_send(user, message)

