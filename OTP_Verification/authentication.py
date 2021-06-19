import otp_generator
def authen():
    i = input( "\n\nEnter your Otp : ")
    if i == otp_generator.OTP:
        print("OTP verified Succesfully")
    else:
        for k in range(3):
            print("Invalid OTP\nYou have  {} attempts left ".format(3-k))
            i=input("Enter your OTP again:")
            if i == otp_generator.OTP:
                print("OTP verified Succesfully")
        print("Reached Maximum Attemps")