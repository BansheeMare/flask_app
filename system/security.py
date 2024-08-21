import bcrypt, random
import system.manage
import system.security
import system.session


def login_user(ip, device, user, password):
    user_data = system.manage.get_user(user)
    if user_data:
        hash = bcrypt.hashpw(password, user_data['salt'])
        if hash == user_data['hash']:
            system.session.start_session(ip, user)
            return True
    return False

def register_user(ip, device, user, password):
    user_data = system.manage.get_user(user)
    if user_data == False:
        salt = bcrypt.gensalt(random.randint(20, 40))
        hash = bcrypt.hashpw(password, salt)
        system.manage.insert_user(user, hash, salt)
        return login_user(ip, device, user, password)
    return False

