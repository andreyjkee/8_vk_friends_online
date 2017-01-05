import getpass
import vk

APP_ID = -1


def get_user_login():
    print('Enter your vk login:')
    login = input()
    return login


def get_user_password():
    print('Enter your vk password:')
    password = getpass.getpass()
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    list_online = api.friends.getOnline()
    return api.users.get(user_ids=list_online, fields=['last_name', 'first_name'])


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('{0} {1}'.format(friend.get('first_name', ''), friend.get('last_name')))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
