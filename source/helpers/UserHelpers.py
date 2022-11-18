from model.Profile import Profile
from model.User import User
from firebaseSetup.Firebase import database
import hashlib
from helpers.ProfileHelpers import ProfileHelpers
from datetime import datetime


class UserHelpers:
    # The maximum of User entities that can be imported into Firebase.
    _userLimit: int = 10


    # Converts this entity into a dictionary
    def UserToDict(user: User) -> dict:
        return {
            'Id': str(user.Id),
            'Username': str(user.Username),
            'FirstName': str(user.FirstName),
            'LastName': str(user.LastName),
            'EmailEnabled': str(user.EmailEnabled),
            'SmsEnabled': str(user.SmsEnabled),
            'TargetedAdvertEnabled': str(user.TargetedAdvertEnabled),
            'LanguagePreference': str(user.LanguagePreference),
            'Friends': user.Friends,
            'University': str(user.University),
            'Major': str(user.Major),
            'Profile': Profile.ProfileToDict(user.Profile),
            'TierEnum': str(user.TierEnum),
            '_LastLoginTimestamp': str(user._LastLoginTimestamp),
            '_SignUpTimestamp': str(user._SignUpTimestamp)
        }


    # Gets a PyreResponse of all users from the DB and returns
    # a list of User entities after constructing it.
    def GetAllUsers(collection: str = "Users") -> list[User]:
        try:
            usersResponse = database.child(collection).get()
            if usersResponse == None: return None

            userResponseList: list = usersResponse.each()
            if (userResponseList == None): return None

            users: list[User] = []
            for user in userResponseList:
                if user == None: continue
                else: users.append(User.HydrateUser(user))

            return users
        except:
            return None


    # Gets a specific User from the database based on the user object provided.
    def GetUser(user: User, collection: str = "Users") -> User:
        try:
            user: User = User.HydrateUser(
                database.child(collection).child(user.Id).get())
            
            if user == None:
                raise Exception(
                    f"Could not get the specified user with username: {user.Username}")
            
            return user
        except:
            print(f"Could not get the specified user with username: {user.Username}")


    # Gets a specific User from the database based on the User ID provided.
    def GetUserById(userId: str, collection: str = "Users") -> User:
        try:
            user: User = User.HydrateUser(
                database.child(collection).child(userId).get())
            
            if user == None:
                raise Exception(
                    f"Could not get the specified user with user ID: {userId}")
            
            return user
        except:
            print(f"Could not get the specified user with user ID: {userId}")

    # returns user Id for a specific user FULL NAME
    def GetUserIdByName(name: str, collection: str = "Users") -> str:
        users = UserHelpers.GetAllUsers(collection)
        if not users: raise Exception("Could not retrieve users from DB\n")
        for user in users:
            if user.FirstName + " " + user.LastName == name:
                return user.Id
        return None

    # Creates the specified user in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def UpdateUser(user: User, collection: str = "Users") -> bool:
        try:
            if (UserHelpers.IsUserLimitMet(collection)):
                print("Maximum of number of users that can sign up have been met.\n"
                    + "User was not updated")
                return False
            
            if (ProfileHelpers.IsProfileExpLimitMet(user.Profile)):
                print("Maximum of number of experiences for a user profile have been met.\n"
                    + "User was not updated")
                return False

            database.child(collection).child(
                user.Id).set(UserHelpers.UserToDict(user))
            return True
        except Exception as e:
            print(e)
            return False


    # Creates a sha256 hash using the username and password.
    # Used as a unique UserId.
    def CreateUserId(username: str, password: str) -> str:
        return hashlib.sha256(
            str.encode(username.join(password))).hexdigest()


    # Deletes a user account.
    def DeleteUserAccount(user: User, collection: str = "Users") -> bool:
        users = UserHelpers.GetAllUsers(collection=collection)
        if (users != None):
            # now check that the username is unique
            for dbUser in users:
                if user.Username == dbUser.Username:
                    database.child(collection).child(user.Id).remove()
                    return True
        else:
            return False


    # helper to check if a given user is present in the db
    def CheckUserPresenceInDB(userToCheck: User, collection: str = "Users") -> bool:
        dbusers = UserHelpers.GetAllUsers(collection)
        for user in dbusers:
            if userToCheck.Username == user.Username:
                return True
        return False


    # Checks if the maximum number of users have signed up.
    def IsUserLimitMet(collection: str = "Users") -> bool:
        allUsers: list[User] = UserHelpers.GetAllUsers(collection)
        
        if allUsers == None or allUsers == []:
            return False
        
        return True if len(allUsers) == UserHelpers._userLimit else False
    

    # Gets a list Users based on the specified attribute.
    def SearchByAttribute(attribute: str, value: str, collection: str = "Users") -> list:
        try:
            users = UserHelpers.GetAllUsers(collection)
            results = []
            for user in users:
                if getattr(user, attribute) == value:
                    results.append(user)
            return results
        except:
            print("\nUh Oh! Something went wrong while searching for users\n")
            return []


    # Checks if the specified user exists in the DB using the provided ID.
    def UserExists(userId: str, collection: str = "Users") -> bool:
        return False if UserHelpers.GetUserById(
            userId, collection) == None else True


    # Updates the user's last log in timestamp.
    def UpdateLastLogin(loggedUser: User, collection: str = "Users"):
        try:
            loggedUser._LastLoginTimestamp = datetime.now()
            UserHelpers.UpdateUser(loggedUser, collection)
        
        except Exception as e:
            print(f"\nException encountered while updating user's last log in timestamp.\n{e}\n")