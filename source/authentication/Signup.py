from firebase.Firebase import database
from PasswordValidation import validatePassword


# this function will accept username and password and return True, if the registration
# was sucessful, False othwerwise; it validates database size limits and uniqueness of username
def RegisterNewUser(username: str, password: str) -> bool:
    try:
        # first let's check that the total number of users does not exceed 5
        # get all DB entries to a local list
        queryResults = database.child('Users').get()

        if len(queryResults) > 5:
            print("Error! There are already 5 accounts in the system!")
            return False
        else:
            # now check that the username is unique
            for query in queryResults:
                if query.val()['username'] == username:
                    print("Error! This username already exists!")
                    return False
    except:
        print("Error! Something went wrong when connecting to database!")
        return False    
    
    # now let's check the password to see if it abides by the set standards
    if not validatePassword(password=password):
        print("Error! Your password does not meet one or some of the standards!")
        return False 

    # if the validation checks above pass, now we can try to create a new entry with the given values
    try:
        # save a new entry inside the "Users" node
        database.child('Users').push(
            {
                "username": username, 
                "password": password
            }
        )
    except:
        print("Error! Something went wrong when connecting to database!")
        return False
