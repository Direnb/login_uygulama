import json5
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currenUser = {}
    #load users from json
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r') as file:
                users = json5.load(file)
                for user in users:
                    user = json5.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('kullanıcı oluşturuldu.')
    def login(self, username, password):


        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currenUser = user
                print('login yapıldı.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currenUser = {}
        print('Çıkış yapıldı.')
    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currenUser.username}')
        else:
            print('giriş yapılmadı.')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json5.dumps(user.__dict__))

        with open('users.json','w') as file:
            json5.dump(list, file)

repository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim = input('1- Register\n2_ Login\n3- Logout\n4- identity\n5- Exit\nseciminiz : ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username = username, password = password, email = email)
            repository.register(user)
            print(repository.users)
        elif secim == '2':
                if repository.isLoggedIn:
                    print('zaten giriş yapılmış.')
                else:
                    username = input('usename: ')
                    password = input('password: ')

                    repository.login(username, password)

        elif secim == '3':
            repository.logout()
        elif secim=='4':
            repository.identity()
        else:
            print('yanlış seçim')

