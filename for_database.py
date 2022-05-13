import getpass
import mysql.connector
import os

from tqdm import tqdm
import time
import colorama

class User:
    def init(self):
        self.login = None
        self.password = None

    def tizimga_kirish(self):
        self.tozalash()
        self.dizayn2()
        tanlash = ["1","2","3"]
        registratsiya = input("[1/2/3]\n>>> ").strip()

        while registratsiya not in tanlash:
            print("invalid")
            self.tozalash()
            self.dizayn2()
            self.tanlash()
            registratsiya = input("[1/2/3]\n>>>  ").strip()

        if registratsiya == tanlash[0]:
            self.tozalash()

            for v in tqdm (range(10)):   # zagruzka uchun
                time.sleep(0.3)
            self.tozalash()
            self.register()

        elif registratsiya == tanlash[1]:
            self.tozalash()

            for m in tqdm (range(10)):   # zagruzka uchun
                time.sleep(0.3)
            self.tizimni_uzgartirish()

        elif registratsiya == tanlash[2]:
            self.tozalash()
            self.chiqish()

    def register(self):
        name = input("login: ").strip().capitalize()
        while self.com(name) or not name.isalpha():
            self.tozalash()
            print("Invalid")
            name = input("login: ").strip().capitalize()

        password_word = getpass.getpass("password").strip()
        while self.com(password_word):
            self.tozalash()
            print("invalid")
            password_word = getpass.getpass("password").strip()
        self.tozalash()
        self.login = name
        self.password = password_word
        self.write_to_mysql()

        for i in tqdm(range(10)):   # zagruzka va ranglar
            time.sleep(0.3)
        print(colorama.Fore.GREEN + (f"{self.dizayn}"))
        self.tizimni_uzgartirish()

    def write_to_mysql(self):
        baza = mysql.connector.connect(
            host="localhost",
            user="Polat",
            password="307129007",
            database="lenovo"
            )
        mycursor = baza.cursor()
        mycursor.execute(f"INSERT INTO qwer (login, password) VALUES ('{self.login}','{self.password}')")
        baza.commit()

    def tizimni_uzgartirish(self):
        self.tozalash()
        self.dizayn()
        options = ["1", "2", "3","4"]
        registratsiya2 = input("[1/2/3/4]\n>>> ").strip()
        while registratsiya2 not in options:
            print("invalid")
            self.tozalash()
            self.dizayn()
            self.options()
            registratsiya2 = input("[1/2/3/4]\n>>> ").strip()

        if registratsiya2 == options[0]:
            self.tozalash()
            self.tekshirish()
        elif registratsiya2 == options[1]:
            self.tozalash()
            self.register2()
        elif registratsiya2 == options[2]:
            self.tozalash()
            self.delete_account()
        elif registratsiya2 == options[3]:
            self.tozalash()
            self.chiqish()

    def tekshirish(self):
        baza = mysql.connector.connect(
            host="localhost",
            user="Polat",
            password="307129007",
            database="lenovo"
        )

        mycursor = baza.cursor()

        new_login = input("LOGIN: ")
        new_password = input("PASSWORD: ")

        asosiy = f"select * from qwer where login='{new_login}' and password='{new_password}'"

        mycursor.execute(asosiy)
        barchasi = mycursor.fetchall()

        if barchasi:
            print("\n\nWELCOME\n\n")
            a=input("tekshirishga qaytsinmi [y/n]")
            if a=="y":
                self.tizimni_uzgartirish()
            elif a=="n":
                self.chiqish()

        else:
            self.tozalash()
            print("MAVJUD EMAS YOKI XATO KIRITDINGIZ\n\n")
            q=input("QAYTADAN TEKSHIRISH [1]\n\n MENUGA O'TISH [2]\n\n>>> ")
            if q=="1":
                self.tekshirish()
            elif q=="2":
                self.tizimni_uzgartirish()

    def register2(self):
        name2 = input("login: ").strip().capitalize()
        while self.com(name2) or not name2.isalpha():
            self.tozalash()
            print("Invalid")
            name2 = input("login: ").strip().capitalize()

        pass_word = getpass.getpass("password").strip()
        while self.com(pass_word):
            self.tozalash()
            print("invalid")
            pass_word = getpass.getpass("password").strip()

        self.tozalash()
        self.login = name2
        self.password = pass_word
        self.change_login()

    def change_login(self): #databaza uchun
        baza2 = mysql.connector.connect(
            host="localhost",
            user="Polat",
            password="307129007",
            database="lenovo"
    )
        mycursor = baza2.cursor()

        mycursor.execute(f"update qwer set login='{self.login}', password='{self.password}' where id=1")
        baza2.commit()
        for m in tqdm (range(10)):
            time.sleep(0.3)
        print(colorama.Fore.YELLOW+("MALUMOTLAR O'ZGARTIRILDI"))
        self.tizimni_uzgartirish()

    def delete_account(self):
        baza = mysql.connector.connect(
            host="localhost",
            user="Polat",
            password="307129007",
            database="lenovo"
        )
        mycursor = baza.cursor()
        qwerty=input("Malumotni o'chirish uchun password kiriting\n\npassword: ")
        qwert = f"delete from qwer where password='{qwerty}'"
        mycursor.execute(qwert)

        baza.commit()

        for r in tqdm (range(10)): # rang va zagruzka
            time.sleep(0.3)
        print(colorama.Fore.RED +("\n\nMALUMOT O'CHIRILDI\n\n"))

        for t in tqdm(range(10)): # zagruzka uchun
            time.sleep(0.3)
        self.tizimni_uzgartirish()

    def chiqish(self):
        print("BYE")


    def dizayn(self):
        print(colorama.Fore.GREEN+("""
        malumot DATABASEga joylashtirildi yoki mavjud
                 TEKSHIRISH  [1]
                 ÖZGARTİRİSH [2]
                 Öchirish    [3]
                 
                 CHIQISH     [4]
                """))

    def dizayn2(self):
        print(colorama.Fore.MAGENTA+("""
        
        login/password kiritish [1]
        
        menuga kirish [2]
        
        chiqish [3]
        
        """))

    def tozalash(self):
        os.system("clear")


    @staticmethod
    def com(str_):
        return not bool(str_)

    def chiqish(self):
        print("GOOD BYE")

qwert = User()

qwert.tizimga_kirish()