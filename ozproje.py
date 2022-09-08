import json
import os




class User():
    def __init__(self,username,password,email):
        self.username =username
        self.password = password
        self.email = email




class RepositoryUser:
    def __init__(self):
        self.users =[]
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUser() # bununla beraber kayıt tutulacak

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                #print(users) # desene yan yana yazar alt alta yazmasını istiyorsan ozamn da for kullan
                for user in users:
                    #print(user)
                    #print(user["username"]) # hata veriri çünkü bu json yapıda biz bunu tekrar paython yapısına döndürelim bunu dajson.load ile yaparız
                    user = json.loads(user)
                    #print(user["username"])  # #sümeyra,ziya isimleri alt alta geldi
                    #print(user["email"]) # emailllerinide bu şekilde istedik
                    newUser = User(username = user["username"],password= user["password"],email = user["email"])
                    self.users.append(newUser)

            print(self.users)



    def login(self,username,password):

        if self.isLoggedIn:
            print("Şuan Giriş yapmış görünüyorsunuz")
        else:
            for user in self.users:
                if user.username == username and password == user.password:
                    self.isLoggedIn = True
                    self.currentUser = user








    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}


    def register(self,user : User):
        self.users.append(user)
        self.savetoFile() #metodunu çağıracağız ki kayıtları dosyaya çekelim
        print("kullanıcı oluşturuldu")
        #print(user)   # kullanıcının kaydının gerçekleştiğini görürüz

    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giriş yapılmadı")
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__)) # nesne alacağım için dumps eğer dosya ile çalışsaydım dump olurdu
                                                    # dict yapmazsan json algılamaz bunu

        with open("users.json","w",encoding="utf-8") as file:
            json.dump(list,file)




repository = RepositoryUser()
while True:
    secim = input("1-kaydol \n2-giriş\n3- çıkış\n4-kayıt bilgileri\n5-Exit\n************")

    if secim == "5":
        break

    else:
        if secim == "1":
            username = input("username : ")
            password = input("password : ")
            email = input("email       : ")

            user = User(username=username,password=password,email=email)

            repository.register(user)
            #print(repository.users)  # buradan da kayıt edildiğini görebilirsin
        elif secim == "2":
            username = input("username: ")
            password = input("password: ")
            repository.login(username,password)

        elif secim == "3":
            repository.logout()
            print("siteden çıkış yaptınız")
        elif secim == "4":
            repository.identity()
            print("kulanıcı bilgilerine erişim ")
        else:
            print("yanlış seçim")













