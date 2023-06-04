
#TODO: N number of average sum

# num = int(input("N nmuber input: "))
# total_sum = 0
# for i in range(num):
#     numbers = float(input(" enter any type of number: "))
#     total_sum+=numbers
# avg = total_sum/num
#TODO: N number of average sum


# sum =(8, 2, 3, 0, 7) #Tuple
# print(type(sum))

# TODO: They give me list or tuple and SUM

# def pope(qe):
#     total=0
#     for i in qe:
#         total+=i
#     print(total)
# num = [1, 2, 3, 4, 5, 1, 4, 5]
# pope(num)
# TODO: They give me list or tuple and SUM

# TODO round number in list

# def roundnumber(we):
#     return sum(we)/len(we)
#
# num = [1, 2, 3, 4, 5, 1, 4, 5,435]
# result = roundnumber(num)
#
# print(round(result, 2))

# TODO round number in list

# TODO:Factireal number
# def fact(n):
#     if n ==1:
#         return n
#     else:
#         return n * fact(n-1)
# print(fact(6))
# TODO:Factireal number

# TODO Convert Integer to String without using str()
# def convert(number):
#     dital = '0123456789'
#     result = ''
#     while number!=0:
#         current_number = number % 10
#         result = dital[current_number]+result
#         number//=10
#     return result
# print(convert(234))

# TODO Perform Login and Registration in Python
#
# class loginegPage:
#     def __str__(self):
#         self.name = ""
#         self.password = 0
#         self.databse = {}
#         self.menu()
#
#     def menu(self):
#         user_input = input('''
#         1. Enter 1 to Register
#         2. Enter 2 to login
#         ''')
#
#         if user_input== "1":
#             self.Registationsytem()
#         if user_input == "2":
#             self.loginsytem()
#
#     def Registationsytem(self):
#         user_name = input('Enter youre name: ')
#         self.name = user_name
#         user_password = input("Enter your password: ")
#         self.password = user_password
#         self.databse[self.name] = self.password
#         print("register susccessfully")
#         self.menu()
#     def loginsytem(self):
#         email = input('Enter youre name: ')
#         password =  input("Enter your password: ")
#
#         flag = 0
#         for i in self.databse:
#             if email == i:
#                 flag = 1
#                 if password == self.databse[i][1]:
#                     print("welcome")






class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None
        print("Amin Init function")


    def insert_beginning(self,data):
        new_node = Node(data,self.head)
        self.head= new_node


    def printlist(self):
        if self.head==None:
            print("LinkList is Empty")
            return
        linkedlist = " "
        iterator = self.head

        while iterator:
            linkedlist = linkedlist + str(iterator.data) + "------->>"
            #jump
            iterator = iterator.next
        return linkedlist


    def size(self):
        count = 0
        iterator = self.head

        while iterator:
            iterator = iterator.next
            count =count + 1
        return count



    def remove(self, index):
        if index<0 or index>=self.size():
            print("Elemnet not in List")
        if index ==0:
            self.head = self.head.next

        count = 0
        iterator = self.head

        while iterator:
            if(count == index-1):
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count = count+1




    def insert_at_index(self, index, data):
        if index<0 or index>=self.size():
            print("Element Empty")
            return
        if index == 0:
            self.insert_beginning(data)

        count = 0
        iterator = self.head
        while iterator:
            if(count == index-1):
                new_node = Node(data, iterator.next)
                iterator.next = new_node
                break
            iterator = iterator.next
            count+=1




s = Linklist() # class Obje S

s. insert_beginning(10)
s.insert_beginning(20)
s.insert_beginning(30)
s.insert_beginning(40)
s.insert_at_index(2,200)
s.remove(2)

print(s.printlist())
print(s.size())



































