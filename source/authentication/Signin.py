from firebaseSetup.Firebase import database


# this function will check if the username and password exists 
# and returns True if so, False otherwise
def LoginUser(username: str, password: str) -> bool:
    try:
        # let's get all the DB queries in a list first
        queryResults = database.child('Users').get()

        # now let's loop through all the quries and check which matches
        foundUser = False
        for query in queryResults:
            if query.val()['username'] == username:
                foundUser = True
                if query.val()['password'] == password:
                    print("\nYou have successfully logged in.")
                    return True
                else:
                    print("\nIncorrect username/password, please try again.")
                    return False

        if not foundUser:
            print("\nIncorrect username/password, please try again.")   
            return False
    except:
        print("\nError! Something went wrong when connecting to database!")
        return False