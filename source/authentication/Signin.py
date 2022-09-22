from model.User import GetAllUsers, CreateUserId

# this function will check if the username and password exists 
# and returns True if so, False otherwise
def LoginUser(username: str, password: str) -> bool:
    try:
        userId = CreateUserId(username, password)
        users = GetAllUsers()
        if (users == None):
            raise Exception()

        for user in users:
            if user.Id == userId:
                print("\nYou have successfully logged in.")
                return True
            else:
                continue

        print("\nIncorrect username/password, please try again.")
        return False
    except:
        print("\nError! Something went wrong when connecting to database!")
        return False
