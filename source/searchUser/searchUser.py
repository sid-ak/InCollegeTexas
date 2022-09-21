from firebaseSetup.Firebase import database


# this function will check if the firstname and lastname of a user exists in the database
# and returns True if so, False otherwise
def SearchUser(firstname: str, lastname: str) -> bool:
    try:
        # let's get all the DB queries in a list first
        queryResults = database.child('Users').get()

        # now let's loop through all the quries and check which matches
        foundUser = False
        for query in queryResults:
            if query.val()['firstName'] == firstname and query.val()['lastName'] == lastname:
                foundUser = True
                print("\nThey are a part of the InCollege system!")
                return True

        if not foundUser:
            print("\nThey are not yet a part of the InCollege system!")   
            return False
    except:
        print("\nError! Something went wrong when connecting to database!")
        return False