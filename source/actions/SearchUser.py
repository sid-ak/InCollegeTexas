from logging import raiseExceptions
from firebaseSetup.Firebase import database
from model.User import UserHelpers
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser


# this function will check if the firstname and lastname of a user exists in the database
# and returns True if so, False otherwise
def SearchUser(firstname: str, lastname: str) -> bool:
    try:
        # let's get all the DB queries in a list first
        queryResults = UserHelpers.GetAllUsers()

        # now let's loop through all the quries and check which matches
        for query in queryResults:
            if query.FirstName == firstname and query.LastName == lastname:
                print("\nThey are a part of the InCollege system!")
                return True

        print("\nThey are not yet a part of the InCollege system!")   
        return False
    except:
        print("\nError! Something went wrong when connecting to database!")
        return False

def DisplayAuthentication():
    decision: int = input("Enter 1 to Log In\n2 to Sign Up")
    
    try:
        if (decision == 1):
            LoginUser()
        elif (decision == 2):
            RegisterNewUser()
        else:
            raise Exception()
    except:
        print("\nInvalid input.")
