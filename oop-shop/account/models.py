import permissions

class User:
    objects = []

    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authorized = False
        print('User successfully created!')
        User.objects.append(self)

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception('Passwords do not match!')
        self.__password = password
        print('User successfully registered!')
    
    def login(self, password):
        if self.__password != password:
            raise Exception('Password is incorrect!')
        self.is_authorized = True
        print('User successfully logged in!')

    def logout(self):
        permissions.login_required(self)
        self.is_authorized = False
        print('User successfully logged out!')
    
    def __str__(self):
        return self.email