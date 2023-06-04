import  random
# This number range create random number
genaratorOTP = random.randint(000000,100000)
username = input("Enter your name: ")
print("Hello", username)
print("this is your random number: ", genaratorOTP)

password = input("Enter your otp: ")

if password == str(genaratorOTP):
    print("login success")
else:
    password!=str(genaratorOTP)
    print("faild")
