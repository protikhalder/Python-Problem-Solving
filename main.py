# import time
# start = time.time()
# i = 1
# while(i<101):
#     print(i)
#     i+=1
# print(time.time()-start)


# l = [1,2,3,4,5]
# sum = 0
# for i in l:
#     sum=sum+i
# print(sum)
#
# product = 1
# for i in l:
#     product*=i
# print(product)


# TODO: integer value return string value

# def num(i):
#     digit = '123456789'
#     if i == 0:
#         return '0'
#     result = ''
#     while i>0:
#         result = digit[i%10] + result
#         i = i//10
#     return result
# print(num(123))
# TODO: list make tuple
# (1,2)
# (1,3)
# (1,4)
# (1,5)
# (2,2)
# (2,3)
# (2,4)
# (2,5)
# (3,2)
# (3,3)
# (3,4)
# (3,5)
# (4,2)
# (4,3)
# (4,4)
# (4,5)
# a = [1,2,3,4]
# b = [2,3,4,5]
#
# for i in a:
#     for j in b:
#         for k in range(1):
#             print('({},{})'.format(i,j))

# TODO: list revers

# L= [1,2,3,4,5]
# for i in range(0,len(L)//2):
#     other = len(L)-i-1
#     temp = L[i]
#     L[i] = L[other]
#     L[other] = temp
# print(L)

# TODO: Factorial Recursion
#
# def num(n):
#     if n == 1:
#         return 1
#     else:
#         return n*num(n-1)
# print(num(6))

#
# def fib(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2 )
# print(fib(5))

# def power(n):
#     if n < 1:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         prev = power(n//2)
#         curr = prev*2
#         print(curr)
#         return curr
# print(power(145))

# def mod(a,b):
#     if b<=0:
#         return -1
#     div = a//b
#     return a -div*b
# print(mod(10,3))

# def digits(n):
#     sum=0
#     while n>0:
#         sum+=n%10
#         n//=10
#     return sum
# print(digits(123))


# TODO: Stack
#
# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None
#     def is_empty(self):
#         return self.top == None
#     def push(self,value):
#         new_node = Node(value)
#         new_node.next = self.top
#         self.top = new_node
#
#     def peek(self):
#         if(self.is_empty()):
#             return "Empty"
#         else:
#             return self.top.data
#     def pop(self):
#         if(self.is_empty()):
#             return "Empty"
#         else:
#             self.top = self.top.next
#     def traverse(self):
#         temp = self.top
#         while temp != None:
#             print(temp.data)
#             temp = temp.next
# s = Stack()
# s.is_empty()

# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self.stack = deque()
#     def push(self,value):
#         self.stack.append(value)
#     def pop(self):
#         return self.stack.pop()
#     def size(self):
#         return len(self.stack)
#     def status(self):
#         if len(self.stack) == 0:
#             return False
#         else:
#             return True
# s = Stack()


# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.queue = deque()
#     def enqueue(self,value):
#         self.queue.appendleft(value)
#     def dequeue(self):
#         return self.queue.pop()
#     def size(self):
#         return len(self.queue)
#     def status(self):
#         if len(self.queue)== 0:
#             return False
#         else:
#             return True
# q = Queue()


# from collections import deque
#
# class Todolist:
#     def __init__(self):
#         self.stack = deque
#     def push(self,vaule):
#         input("Please give me: ")
#         self.stack.append(vaule)
#     def pop(self):
#         self.stack.pop()
#     def num_of_tasks(self):
#         return len(self.stack)
#     def Get_all_tasks(self):
#         return self.stack
#     def Get_one_by_one(self):
#         for i in self.stack:
#             print(i)
#
# t = Todolist()


#
# from collections import deque
#
# class Oderlist:
#     def __init__(self):
#         self.queue = deque()
#     def enqueue(self):
#         name = input("Give food name: ")
#         quantity = input("Give the quantity: ")
#         payment = input("Give the payment: ")
#         value = {"name": name, "quantity":quantity , "payment": payment}
#         self.queue.appendleft(value)
#     def dequeue(self):
#         self.queue.pop()
#     def oderlist(self):
#         return len(self.queue)
#     def all_oder_view(self):
#         return self.queue
#
# s=Oderlist()
# s.enqueue()
#
# s.enqueue()
# s.enqueue()
# s.dequeue()

# from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print_list(self):
        if(self.head == None):
            print("There is nothing in thr list!")
            return
        linkedlist = ""
        iterator = self.head
        while iterator:
            linkedlist = linkedlist + str(iterator.data) + " --------->>>"
            # jump
            iterator = iterator.next
        return linkedlist

    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data,None)

    def get_size(self):
        count = 0
        iterator = self.head
        while iterator:
           count = count + 1
           iterator = iterator.next
        return count

    def remove_at_index(self,index):
        if(index<0 or index >= self.get_size()):
            print("Cannot remove the element!")
            return
        if index == 0:
            self.head = self.head.next
        count = 0
        iterator = self.head
        while(iterator):
            if(count == index -1):
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count = count + 1

    def insert_at_index(self,index,data):
        if (index < 0 or index >= self.get_size()):
            print("Cannot remove the element!")
            return

        if(index == 0):
            self.insert_at_beginning(data)

        count = 0
        iterator = self.head
        while (iterator):
            if (count == index - 1):
                new_node = Node(data,iterator.next)
                iterator.next = new_node
                break
            iterator = iterator.next
            count = count + 1



L1 = LinkedList()
L1.insert_at_beginning(10)
print(L1.head)
L1.insert_at_beginning(20)
print(L1.head)
L1.insert_at_beginning(30)
L1.insert_at_beginning(40)
L1.insert_at_beginning(50)
print(L1.head)
print(L1.print_list())
L1.insert_at_end(200)
print(L1.print_list())
print(L1.get_size())
L1.remove_at_index(0)
print(L1.print_list())
L1.remove_at_index(4)
print(L1.print_list())
L1.insert_at_index(2,4000)
print(L1.print_list())