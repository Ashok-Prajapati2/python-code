# constutor

class Atm:

    def __init__(self):
        self.__pin = 0
        self.__balance = 0

    def check_amount(self):
        print(self.__balance)

    def deposit(self, pin, amount):
        if(self.__pin == pin):
            self.__balance = amount
        else:
            print("wrong pin")

    def setpin(self, pin):
        if(self.__pin == 0):
            self.__pin = pin
        else:
            self.oldpin = input("enter old pin : ")
            if(self.__pin == pin):
                self.__pin = pin
            else:
                print("please try again some time after")

a = Atm()
a.check_amount()

a.deposit(1234, 1000)
a.setpin(1212)
a.deposit(1212,10000)
a.check_amount()