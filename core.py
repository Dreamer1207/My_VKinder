# импорты
import vk_api

from config import acces_token

# получение данных о пользователе

vkapi = vk_api.VkApi(token=acces_token)

def get_profile_info(user_id):
    
    info, = vkapi.method('users.get',
                         {'user_id': user_id,
                          'fields': 'city'
                          }
                         )
    return info

if __name__ == '__main__':
    pass


