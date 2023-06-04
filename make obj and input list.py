class Person:
    __counter = 1
    def __init__(self, name, gender):
        self.boyname = name
        self.genderBoy = gender
        self.cid = Person.__counter
        Person.__counter+=1
    @staticmethod
    def getter():
        print(f"{Person.__counter}")




p1 = Person("orpto","male")

p2 = Person("osfcafrpto", "Fmale")

p3 = Person("orpdfvsfvsdefto", "male")


print(p1.cid)
print(p2.cid)
print(p3.cid)


p1.getter()
# TODO: obj to list:
# l1 = [p1,p2,p3]
#
# for i in l1:
#     print(i.boyname, i.genderBoy)

# TODO: obj to dict:

# d = {'p1':p1, 'p2':p2, 'p3':p3}
#
# for i in d:
#     print(d[i].boyname, d[i].genderBoy)
#
