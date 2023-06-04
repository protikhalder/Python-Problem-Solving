class Libaray:
    def __init__(self, id, name):
        self.bookID = id
        self.bookName = name

    def settermethed(self, bookmane):
        self.bookName = bookmane
    def getmetho(self):
        print(f"This is the book name: {self.bookName}")


book = Libaray(101,"Crasdef sacvhabs adfnckc ")

print(book.getmetho())


book.settermethed("afvjasdnfkjafasnfakjasff")

print(book.getmetho())
