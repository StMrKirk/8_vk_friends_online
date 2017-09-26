import vk
import sys


APP_ID = 6197135


def get_user_login():
    login = sys.argv[1]
    return login


def get_user_password():
    password = sys.argv[2]
    return password


def get_online_friends(login, password):
    friends_online_list = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online = api.friends.getOnline()
    friends_info = api.users.get(user_ids=friends_online)
    return friends_info


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('Имя: {:20} Фамилия: {:20}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
