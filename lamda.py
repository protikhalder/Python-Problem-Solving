


# TODO: lamda multiply and power
# multipul = lambda x,y:x*y
# print(multipul(206,4564))
#
#
# power = lambda x,y: x**y
# print(power(2,3))

# TODO: map list and Dict
# some_num = [2,3,4,5,6,7]
# doble = map(lambda x:x+x,some_num)
# print(list(doble))


# d1 = {3:"e",2:"a", 1:"c", 7:"b", 5:"d"}
# doble = map(lambda key: key+key,d1)
# print(list(doble))

# string = ["my", "python "]
# cap = map(lambda x: str.upper(x),string)
# print(list(cap))

# TODO : sortvalue by lamda

# attendamce = [34,45,67,89,45,435,23,2,4,24,34]
#
# vp1 = sorted(attendamce,key=lambda x:x**2)
# print(vp1)

d1 = {3:"e",2:"a", 1:"c", 7:"b", 5:"d"}

f1 = sorted(d1.items(),key=lambda x:x[0])

print(f1)

sort = sorted(f1,key=lambda x:x[1])
print(sort)
