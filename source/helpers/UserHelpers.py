from model.Profile import Profile
from model.User import User
from firebaseSetup.Firebase import database
import hashlib

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
            'Profile': Profile.ProfileToDict(user.Profile)
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
            for user in usersResponse.each():
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

    # Creates the specified user in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def UpdateUser(user: User, collection: str = "Users") -> bool:
        try:
            if (UserHelpers.IsUserLimitMet(collection)):
                return False

            database.child(collection).child(
                user.Id).set(UserHelpers.UserToDict(user))
            return True
        except:
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

    # Checks if the maximum number of jobs have been posted.
    def IsUserLimitMet(collection: str = "Users") -> bool:
        allUsers: list[User] = UserHelpers.GetAllUsers(collection)
        
        if allUsers == ([] or None):
            return False
        
        return True if len(allUsers) == UserHelpers._userLimit else False
    
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
