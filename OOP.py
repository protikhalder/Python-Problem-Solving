# oop power create own datatype for me

class Atm:
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        print("I am excute")
        self.mene()
    def get_balamce(self):
        return self.__balance
    def mene(self):
        user_input= input("""
        Hi how can i help you
        1. Press 1 create pin
        2. Press 2 change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        """)

        if user_input == "1":
            self.create_pin()
            #create pin
        elif user_input == "2":
            self.change_pin()
            #change pin
        elif user_input == "3":
            self.check_balance()

            #check balance
        elif user_input == "4":
            self.withdraw()
            # withdraw
        else:
            exit()

    def create_pin(self):
        user_pin = int(input("Enter your pin: "))
        self.pin = user_pin
        user_balnce = int(input("enter your balance: "))
        self.__balance = user_balnce

        print('pin crreate successfully')
        self.mene()


    def change_pin(self):
        old_pin = int(input("enter your old pin "))
        if old_pin == self.pin:
            new_pin = int(input("enter your new pin: "))
            self.pin = new_pin
            print("your pin change successfully")
            self.mene()
        else:
            print("soory worng pin")
            self.mene()

    def check_balance(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            print("Youie balance is: ", self.__balance)
        else:
            print("ypoue not real user")
            self.mene()

    def withdraw(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            amount = int(input("enter your amount: "))
            if amount <= self.__balance:
                self.__balance-=amount
                print("yor withdraw money:", amount)
                print("your current balac is: ", self.__balance)
            else:
                print("you not enough money")

        else:
            print("wrong pin")
        self.mene()




ogh = Atm()

print(ogh)

#TODO: parameterized constructor this obj -> class need parameter

# class Fraction:
#     def __init__(self,x,y):
#         self.nmu = x
#         self.boy = y
#     def __str__(self):
#         return '{}/{}'.format(self.nmu, self.boy)
# obj = Fraction(3,5)
#
# print(obj)




