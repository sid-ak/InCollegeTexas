from model.User import User
from firebaseSetup.Firebase import database
from model.Entities import Entities

# Gets a PyreResponse of all users from the DB and returns
# a list of User entities after constructing it.
def GetAllUsers() -> list[User]:
    usersResponse = database.child(Entities.Users).get()
    
    users = []
    for user in usersResponse.each():
        users.append(User(
            Username = user.val()["Username"],
            Password = user.val()["Password"],
            FirstName = user.val()["FirstName"],
            LastName = user.val()["LastName"]
        ))

    return users