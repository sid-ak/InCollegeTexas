from model.User import User
from helpers.UserHelpers import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
from helpers.MessageHelpers import MessageHelpers
from model.Message import Message
from enums.UserTierEnum import UserTierEnum

#This function helps dislay all the user in the database and gives the user to send a message to anyone if they are plus member or are friends with them
def DisplayEveryUser(loggedUser: User, collection: str = "Users"):
        allUser = UserHelpers.GetAllUsers(collection)
        allUsers = list(filter(lambda user: user.Username != loggedUser.Username, allUser))
        displayU = list(map(lambda x: x.Username, allUsers))

        while True:
            
            print("\nSelect one of the user to send a message\n")
            MenuHelpers.DisplayOptions(displayU)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()
                isFriends:bool = loggedUser.Friends.get(displayU[optionNo - 1])

                if optionNo == -1: break

                elif optionNo in range(1, len(allUser) + 1):
                    if(loggedUser.TierEnum == UserTierEnum.Plus or isFriends):
                        content: str = str(input(f"\nEnter the content for the message to {displayU[optionNo - 1]}:\n\n"))

                        messageSent: bool = MessageHelpers.UpdateMessage(Message(
                            MessageHelpers.CreateMessageId(),
                            loggedUser.Id,
                            allUsers[optionNo - 1].Id,
                            content
                        ))
                    else:
                        print("\nI'm sorry, you are not friends with that person.\n")
                        continue

                    if messageSent: print(f"\nMessage sent to {displayU[optionNo - 1]} successfully.")
                    else: print("\nMessage was not sent.\n")
            except Exception as e:
                raise Exception(f"Something went wrong, could not display all the users\n{e}")
            