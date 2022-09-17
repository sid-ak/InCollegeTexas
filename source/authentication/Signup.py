from firebase.Firebase import database


# this function will validate the password and return True, if it is valid, False otherwise
def validatePassword(password: str) -> bool:
    checkLength = False
    checkUpperCase = False
    checkDigit = False
    checkSpecialCharacter = False
    if len(password) >= 8 and len(password) <= 12:
        checkLength = True

    for charCheck in password:
        if charCheck.isupper():
            checkUpperCase = True
        elif charCheck.isdigit():
            checkDigit = True
        elif charCheck.islower() == False:
            checkSpecialCharacter = True
    
    if checkDigit and checkLength and checkSpecialCharacter and checkUpperCase:
        return True
    else:
        False


# this function will accept username and password and return True, if the registration
# was sucessful, False othwerwise; it validates database size limits and uniqueness of username
def RegisterNewUser(username: str, password: str) -> bool:
    try:
        # first let's check that the total number of users does not exceed 5
        # get all DB entries to a local list
        queryResults = database.child('Users').get()

        if len(queryResults.each()) > 5:
            print("Error! There are already 5 accounts in the system!")
            return False
        else:
            # now check that the username is unique
            for query in queryResults.each():
                if query.val()['username'] == username:
                    print("Error! This username already exists!")
                    return False
    except:
        print("Error! Something went wrong when connecting to database to fetch all entries!")
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
        
        return True
    except:
        print("Error! Something went wrong when connecting to database to push a new entry!")
        return False
