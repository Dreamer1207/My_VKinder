# импорты
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import comunity_token

# отправка сообщений
vk = vk_api.VkApi(token=comunity_token)



def message_send(user_id, message, attachment=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'attachment': attachment,
               'random_id': get_random_id()})
    

# обработка событий / получение сообщений

vk = vk_api.VkApi(token=comunity_token)
longpoll = VkLongPoll(vk)

# эxо
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message_send(event.user_id, event.text.lower())
        
if __name__ == '__main__':
    pass
