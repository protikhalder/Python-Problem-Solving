# TODO: sum value

# tel = {'jack': 4098, 'sape': 4139}
#
# print(sum(tel.values()))
# sum = 0
# for i in tel.values():
#     sum = sum+i
# print(sum)
# TODO: tulpe to list to dict to dict
# lsy = ('sapesd', 4139), ('guidosdds', 4127), ('jacksdv', 4098)
# list = [('sape', 4139), ('guido', 4127), ('jack', 4098)]
# opp = dict(list)
# aop=list
# print(aop)
# sum=0
# for i in opp.values():
#     sum = sum +i
# print(sum)

# TODO: How to take Dictionary Input From User

# d = {}
# size = int(input("Enter loop: "))
# for i in range(size):
#     key = input("Enter key: ")
#     value = input("Enter value")
#     d[key] = value
# print(d)


# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions,answers ):
#     print('What is your {0}?  It is {1}.'.format(q,a))



# for i in reversed(range(1,11,2)):
#     print(i)


# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(set(basket)):
#     print(i)

# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for i in raw_data:
#     if not math.isnan(i):
#         filtered_data.append(i)
# print(filtered_data)

#
# TODO: dict_convert[i]=value
# stu = [('sapesd', 4139), ('guidosdds', 4127), ('jacksdv', 4098) , ('sape', 4139), ('guido', 4127), ('jack', 4098)]
# ditt=[]
# sim= 0
# dict_convert = dict(stu)
# for i in dict_convert.values():
#     ditt.append(i)
#     # print(dict_convert[i])
#     sim+=i
# print(sim)
# print(ditt)
# TODO:item
# stu = [('sapesd', 4139), ('guidosdds', 4127), ('jacksdv', 4098)]
# dict = dict(stu)
# for i,j in dict.items():
#     print(i,"=",j)

# TODO: ADD dict {}
# stu = [('sapesd', 4139), ('guidosdds', 4127), ('jacksdv', 4098)]
# dict = dict(stu)
#
# dict["protik"]=5345
#
# print(len((dict)))
#
# TODO: nested Dict value=change
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# myfamily["child1"]["year"]=354345
# print(myfamily[ "child1"])

# num = int(input("Enter input"))
# roll = 0
# stu = {}
# for i in range(num):
#     roll+=1
#     name=input("Enter name: ")
#     food = input("Enter food: ")
#     vegetable = input("Enter vegetable: ")
#     meat = input("Enter meat: ")
#     stu[roll]=[[name],[food],[vegetable], [meat]]
# print(stu)
# s=[]
# for i in stu:
#     s=stu[i]
# print(s)
#
# print(stu)

# d1 = {3:"e",2:"a", 1:"c", 7:"b", 5:"d"}
# print(sorted(d1.items(),key=lambda x:x[1]))
# [(2, 'a'), (7, 'b'), (1, 'c'), (5, 'd'), (3, 'e')] # value sorted