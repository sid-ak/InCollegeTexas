from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser
from helpers.MenuHelpers import MenuHelpers
from helpers.UserHelpers import UserHelpers

# this function will check if the firstname and lastname of a user exists in the database
# and returns True if so, False otherwise
def SearchUser() -> bool:
    try:
        firstName: str = input("\nPlease enter first name: ")
        lastName: str = input("Please enter last name: ")

        users = UserHelpers.GetAllUsers()
        for user in users:
            if user.FirstName == firstName and user.LastName == lastName:
                print("\nThey are a part of the InCollege system!")
                DisplayAuthentication()
                return True

        print("\nThey are not yet a part of the InCollege system!")   
        return False
    except:
        print("\nError! Something went wrong when connecting to database!")
        return False

def DisplayAuthentication():
    while True:
        print("\nPlease enter one of the following options to continue:")
        MenuHelpers.DisplayOptions(["Log In", "Sign Up"])
        
        try:
            decision: int = MenuHelpers.InputOptionNo()

            if decision == -1: break

            if (decision == 1):
                LoginUser()
            elif (decision == 2):
                RegisterNewUser()
            else:
                raise Exception()
        except:
            print("\nInvalid input.")