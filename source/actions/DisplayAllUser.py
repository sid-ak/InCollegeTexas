from model.User import User
from helpers.UserHelpers import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
from helpers.MessageHelpers import MessageHelpers
from enums.UserTierEnum import UserTierEnum

#This function helps display all the user in the database and gives the user to 
# send a message to anyone if they are plus member or are friends with them
def DisplayEveryUser(
    loggedUser: User,
    messageCollection: str = "Messages",
    userCollection: str = "Users"):
        
        allUsers: list[User] = UserHelpers.GetAllUsers(userCollection)
        otherUsers: list[User] = list(filter(lambda user: user.Username != loggedUser.Username, allUsers))
        otherUsernames: list[str] = list(map(lambda x: x.Username, otherUsers))

        while True:
            
            print("\nSelect one of the user to send a message\n")
            MenuHelpers.DisplayOptions(otherUsernames)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(allUsers) + 1):
                    friendUsername: str = otherUsernames[optionNo - 1]
                    isFriends: bool = loggedUser.Friends.get(friendUsername)
                    friendUserId: User = otherUsers[optionNo - 1].Id
                    
                    if (loggedUser.TierEnum == UserTierEnum.Plus or isFriends):
                        messageSent: bool = MessageHelpers.SendMessage(
                            loggedUser.Id,
                            friendUserId,
                            messageCollection,
                            userCollection)

                        if not messageSent: raise Exception()
                    
                    else:
                        print("\nI'm sorry, you are not friends with that person.\n")
                        continue

            except Exception as e:
                raise Exception(f"Something went wrong, could not display all the users\n{e}")
