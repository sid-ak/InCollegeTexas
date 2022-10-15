from model.User import User, UserHelpers

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

# this function will accept username and password and return True, if the registration
# was successful, False otherwise; it validates database size limits and uniqueness of username
def RegisterNewUser(collection: str="Users") -> bool:
    try:        
        # first let's check that the total number of users does not exceed 5
        if UserHelpers.IsUserLimitMet(collection=collection):
            return False
        # get all DB entries to a local list
        username = input("\nPlease enter your username: ")
        users = UserHelpers.GetAllUsers(collection=collection)
        if (users != None):
            # now check that the username is unique
            for user in users:
                if user.Username == username:
                    print("\nError! This username already exists!")
                    return False
    except:
        print("\nError! Something went wrong when connecting to database to fetch all entries!")
        return False
    
    # now let's check the password to see if it abides by the set standards
    password = input("\nPlease enter your password: ")
    if not ValidatePassword(password=password):
        print("\nError! Your password does not meet one or some of the standards!")
        return False 
    
    # if the validation checks above pass, now we can try to create a new entry with the given values
    firstName = input("\nPlease enter your first name: ")
    lastName = input("\nPlease enter your last name: ")
    try:
        userId = UserHelpers.CreateUserId(username, password)
        UserHelpers.UpdateUser(User(userId, username, firstName, lastName), collection=collection)
        return True
    except:
        print("\nError! Something went wrong when connecting to database to push a new entry!")
        return False
