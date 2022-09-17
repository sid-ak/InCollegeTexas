from firebase.Firebase import database


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
                    return True
                else:
                    print("Error! Incorrect password!")
                    return False

        if not foundUser:
            print("Error! Could not find an account with is username!")   
            return False
    except:
        print("Error! Something went wrong when connecting to database!")
        return False