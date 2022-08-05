from .models import MyUser

def register():
    username = input("Type a username: ")
    password = input("Type a password: ")
    MyUser.create(username=username, password=password)
    return 'User signed up successfully!'