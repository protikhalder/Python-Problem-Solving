class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def geet(self):
        if self.country =="india":
            print("nomo", self.name)
        else:
            print("hello", self.name)

p1 = Person("protik", "india")

print(p1.name)
print(p1.geet())