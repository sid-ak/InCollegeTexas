from firebase.Firebase import database
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser

print('Welcome! Please, select "1" to login or "2" to sign up with a new account')
while True:
    try:
        decision = int(input("Enter (-1 to Exit): "))
        if decision == 1:
            print("\nLogin Selected.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if LoginUser(username=username, password=password):
                    print("Success! You have successfully logged into your account.")
                    break
            else:
                print("Failure! Incorrect credentials.")
        elif decision == 2:
            print("\nSignup Selected.")
            username = input("Please enter your username: ")
            password = input("Please enter your password")
            if RegisterNewUser(username=username, password=password):
                print("Sucess! You have sucessfully created a new account.")
                break
            else:
                print("Failure! We have not been able to create a new account for you.")
        elif decision == -1:
            print("Exit selected.")
        else:
            print("Invalid entry! Please try again.")
    except:
        print("Invalid entry! Please try again.")
                