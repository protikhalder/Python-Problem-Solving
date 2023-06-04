# class User:
#     def __init__(self):
#         self.name = 'p[rptoi'
#     def login(self):
#         print("L:ogin")
#
# class Student(User):
#
#     def __init__(self,os, po):
#         self.os = os
#         self.po = po
#     def enrool(self):
#         print("Enrool")
#
# U = User()
# S = Student()
# S.login()
# S.enrool()

# constructor example

#


# TODO : cant access Paranet class __INIT__ method beacuse child have own __INIT method
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
#
#     def buy(self):
#         print ("Buying a phone")
#
# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor")
#
# s=SmartPhone("Android", 2)
#
# s.buy()

# TODO child can't access private members of the Parent class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def __get(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.brand)
        self.get()

s = SmartPhone(10, "sdfs", "ascas")
s.check()
s.get()


