class Person:
    def __init__(self, name, age):
        self.nameboy = name
        self.ageboy = age


def Oop(parameter):
    print("hi me name is ", parameter.nameboy, "my age is", parameter.ageboy)
    parameter.nameboy = "polokhr"
    return parameter



p = Person("protik",45)
print(id(p))
p1 = Oop(p)
print(id(p1))
x = Oop(p)
print(id(x.nameboy))



