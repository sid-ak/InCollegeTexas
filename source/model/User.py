from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database

# A User entity.
@dataclass
class User:
    Id: int
    Username: str
    FirstName: str = ""
    LastName: str = ""

    # Hydrates a User entity using a pyrebase response value and returns it.
    def HydrateUser(user):
        return User(
                Id = user.val()["Id"],
                Username = user.val()["Username"],
                FirstName = user.val()["FirstName"],
                LastName = user.val()["LastName"]
            )

class UserHelpers:
    # Converts this entity into a dictionary
    def UserToDict(user: User) -> dict:
        return {
            'Id': str(user.Id),
            'Username': str(user.Username),
            'FirstName': str(user.FirstName),
            'LastName': str(user.LastName)
        }

    # Gets a PyreResponse of all users from the DB and returns
    # a list of User entities after constructing it.
    def GetAllUsers(collection: str = "Users") -> list[User]:
        try:
            usersResponse = database.child(collection).get()
            
            users: list[User] = []
            for user in usersResponse.each():
                users.append(User.HydrateUser(user))

            return users
        except:
            return None

    # Creates the specified user in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def CreateUser(user: User, collection: str = "Users") -> bool:
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
