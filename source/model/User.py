from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from enums.LanguageEnum import LanguageEnum

# A User entity.
@dataclass
class User:
    Id: str
    Username: str
    FirstName: str = ""
    LastName: str = ""
    EmailEnabled: bool = True
    SmsEnabled: bool = True
    TargetedAdvertEnabled: bool = True
    LanguagePreference: LanguageEnum = LanguageEnum.English

    # Hydrates a User entity using a pyrebase response value and returns it.
    def HydrateUser(user):
        return User(
                Id = user.val()["Id"],
                Username = user.val()["Username"],
                FirstName = user.val()["FirstName"],
                LastName = user.val()["LastName"],
                EmailEnabled = user.val()["EmailEnabled"],
                SmsEnabled = user.val()["SmsEnabled"],
                TargetedAdvertEnabled = user.val()["TargetedAdvertEnabled"],
                LanguagePreference = user.val()["LanguagePreference"]
            )
    
class UserHelpers:
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
            'LanguagePreference': str(user.LanguagePreference)
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

    # Creates the specified user in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def UpdateUser(user: User, collection: str = "Users") -> bool:
        try:
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

    # Toggles the email preference for a user.
    def ToggleEmailEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.EmailEnabled = not user.EmailEnabled            
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nEmail Enabled: {user.EmailEnabled}")
        except:
            print("Exception occurred. Email preference could not be toggled.")

    # Toggles the sms preference for a user.
    def ToggleSmsEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.SmsEnabled = not user.SmsEnabled            
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nSMS Enabled: {user.SmsEnabled}")
        except:
            print("Exception occurred. SMS preference could not be toggled.")

    # Toggles the advertising preference for a user.
    def ToggleTargetedAdvertEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.TargetedAdvertEnabled = not user.TargetedAdvertEnabled            
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nTargeted Advertising Enabled: {user.TargetedAdvertEnabled}")
        except:
            print("Exception occurred. Targeted Advertising preference could not be toggled.")

    # Sets the preferred language for a user as specified.
    def SetLangPreference(user: User, language: LanguageEnum, collection: str = "Users"):
        try:
            if user == None: return

            user.LanguagePreference = language            
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nPreferred language set to: {user.LanguagePreference.name}")
        except:
            print("Exception occurred. Targeted Advertising preference could not be toggled.")
