#coding=utf-8

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
vk = vk_api.VkApi(token='09f69925b0d308fd3c063775295c127006b3e73ffba0983c4e6fca708761c1cce97a43f53bcaf593c3684')

answer = 'москва - река'

while True:
    messages = vk.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unread'})
    if messages['count'] >= 1:
        id = messages['items'][0]['last_message']['from_id']
        body = messages['items'][0]['last_message']['text']
        if body.lower() == 'привет' or body.lower() == 'здравствуй' or body.lower() == 'hello':
            vk.method('messages.send', {'peer_id': id, 'message': 'Привет', "random_id":random.randint(2, 100)})
        elif body.lower() == answer:
            vk.method('messages.send', {'peer_id': id, 'message': 'Верно!', "random_id":random.randint(2, 100)})
        elif body.lower() == 'да':
            vk.method('messages.send', {'peer_id': id, 'message': 'Пизда!', "random_id":random.randint(2, 100)})
        else:
            vk.method('messages.send', {'peer_id': id, 'message': 'Извините, пока я вас не понимаю', "random_id":random.randint(2, 100)})
    time.sleep(1)