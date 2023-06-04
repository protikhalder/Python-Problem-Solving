import pyotp
from timeit import default_timer as timer

# base_32_secret_key = pyotp.random_base32()
# print(base_32_secret_key)
#
# with open("secret_key.txt", 'w') as f:
#     f.write(base_32_secret_key)

with open("secret_key.txt", 'r') as f:
    base_32_sert_key = f.read()

TimebasedOtp = pyotp.TOTP(base_32_sert_key)

current_otp = TimebasedOtp.now()

# print(current_otp) #614052

def verfication(time_gap, user_otp, genarator_otp, TimebasedOtp):
    if(time_gap<30) and (user_otp == genarator_otp):
        print("Hello user your verified")
        return
    elif(time_gap<30) and (user_otp!=genarator_otp):
        print("Enter otp not correect , hence u are not verifie")
        print("We send new OTP , Please wait")
        resend_otp(TimebasedOtp)
    elif(time_gap)>30:
        print("time up")
        print("We send new OTP , Please wait")
        resend_otp(TimebasedOtp)



def resend_otp(TimebasedOtp):
    current_otp = TimebasedOtp.now()
    while True:
        new_currentotp = TimebasedOtp.now()
        if new_currentotp != current_otp:
            print(f"Current_otp:", new_currentotp)
            start = timer
            enter_usre = input("Enter opt: ")
            end = timer
            resend_time_intertval = end-start
            print(f"Time taken: {resend_time_intertval } ")
            verfication(resend_time_intertval,enter_usre,new_currentotp, TimebasedOtp)
            break



while True:
    new_currentotp = TimebasedOtp.now()
    if new_currentotp!=current_otp:
        print(f"Current OTP: {new_currentotp}")
        start = timer()
        Enter_otp=input("enter otp: ")
        end = timer()

        time_interval = end-start
        print(f"Time taken: {time_interval} ")
        verfication(time_interval,Enter_otp,new_currentotp, TimebasedOtp)
        break



