from firebase.Firebase import database


# this function will validate the password and return True, if it is valid, False otherwise
def ValidatePassword(password: str) -> bool:
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
        return False


# this function will query the Firebase DB and check the current number of accounts
# it will return False if the number exceeds 5, True otherwise
def CheckDBSize() -> bool:
    # get all DB entries tp a local list
    queryResults = database.child('Users').get()

    if len(queryResults.each()) >= 5:
        print("\nAll permitted accounts have been created, please come back later!")
        return False
    else:
        return True

# this function will accept username and password and return True, if the registration
# was sucessful, False othwerwise; it validates database size limits and uniqueness of username
def RegisterNewUser(username: str, password: str) -> bool:
    try:
        # first let's check that the total number of users does not exceed 5
        # get all DB entries to a local list
        queryResults = database.child('Users').get()

        if not CheckDBSize():
            return False
        else:
            # now check that the username is unique
            for query in queryResults.each():
                if query.val()['username'] == username:
                    print("\nError! This username already exists!")
                    return False
    except:
        print("\nError! Something went wrong when connecting to database to fetch all entries!")
        return False    
    
    # now let's check the password to see if it abides by the set standards
    if not ValidatePassword(password=password):
        print("\nError! Your password does not meet one or some of the standards!")
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
        print("\nError! Something went wrong when connecting to database to push a new entry!")
        return False
