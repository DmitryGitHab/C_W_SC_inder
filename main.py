from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# token = input('Token: ')
token = '418ddac8c6d19089c5db6355783a862998e819167f02d4c3fe54c967ccb70cdca52b207132160ab9dd641'

vk = vk_api.VkApi(token=token)
print(vk)

longpoll = VkLongPoll(vk)





def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })


write_msg(209056331, 'шалом')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")







#
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
