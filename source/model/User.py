from dataclasses import dataclass
from firebaseSetup.Firebase import database

@dataclass
class User:
    Username: str
    Password: str
    FirstName: str
    LastName: str

    # Hydrates a User entity using a pyrebase response value and returns it.
    def HydrateUser(user):
        return User(
                Username = user.val()["Username"],
                Password = user.val()["Password"],
                FirstName = user.val()["FirstName"],
                LastName = user.val()["LastName"]
            )

# Gets a PyreResponse of all users from the DB and returns
# a list of User entities after constructing it.
def GetAllUsers(collection: str = "Users") -> list[User]:
    usersResponse = database.child(collection).get()
    
    users = []
    for user in usersResponse.each():
        users.append(User.HydrateUser(user))

    return users

