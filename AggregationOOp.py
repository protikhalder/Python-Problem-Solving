class Customer:
    def __init__(self, name, email, address):
        self.nameC = name
        self.emailC = email
        self.addressC = address

    # def printmethod(self):
    #     print(self.nameC, self.emailC, self.addressC)


    def printMethod(self):
       print( self.addressC.pinA, self.addressC.get(), self.addressC.stateA )

    def edit_profile(self, new_name, n_pin, n_city, n_state):
        self.nameC = new_name
        self.addressC.edit_address(n_pin,n_city,n_state)


class Address:
    def __init__(self, pin, city, state):
        self.pinA = pin
        self.__cityA = city
        self.stateA =  state
    def get(self):
       return self.__cityA

    def edit_address(self, new_pin, new_city, new_state):
        self.pinA = new_pin
        self.__cityA = new_city
        self.stateA = new_state


A = Address(12312312, "london", "USA")


C = Customer("Protik", "email@P", A)
C.printMethod()
C.edit_profile("PoloK", 123123, "bangladesh", "Dhaka")
C.printMethod()




