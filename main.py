import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from response import get_response
import random

with open('token.txt', 'r', encoding='UTF-8') as file_text:
    TOKEN = file_text.read()

vk_session = vk_api.VkApi(token=TOKEN)
vk_get_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 10**10)

        response = get_response(message)

        vk_get_api.messages.send(user_id=user_id, random_id=random_id, message=response)
