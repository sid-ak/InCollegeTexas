from model.User import User, UserHelpers

# this function will check if the username and password exists 
# and returns True if so, False otherwise
def LoginUser() -> User:
    try:
        print("\nLogin Selected.")
        username = input("\nPlease enter your username: ")
        password = input("Please enter your password: ")
        userId = UserHelpers.CreateUserId(username, password)
        users = UserHelpers.GetAllUsers()
        if (users == None):
            raise Exception()

        for user in users:
            if user.Id == userId:
                print("\nYou have successfully logged in.")
                return user
            else:
                continue

        print("\nIncorrect username/password, please try again.")
        return None
    except:
        print("\nError! Something went wrong when connecting to database!")
        return None
