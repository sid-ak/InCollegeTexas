from firebase.Firebase import database
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser

# this is the main run file

print('Welcome! Please, select "1" to login or "2" to sign up with a new account')
while True:
    try:
        decision = int(input("Enter (-1 to Exit): "))
        if decision == 1:
            print("\nLogin Selected.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if LoginUser(username=username, password=password):
                    print("\nSuccess! You have successfully logged into your account.")
                    break
            else:
                print("Failure! Incorrect credentials.")
        elif decision == 2:
            print("\nSignup Selected.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if RegisterNewUser(username=username, password=password):
                print("\nSucess! You have sucessfully created a new account.")
                break
            else:
                print("\nFailure! We have not been able to create a new account for you.")
        elif decision == -1:
            print("\nExit selected.")
            break
        else:
            print("Invalid entry! Please try again.")
    except:
        print("Invalid entry! Please try again.")
               


