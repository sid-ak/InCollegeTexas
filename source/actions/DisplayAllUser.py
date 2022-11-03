from model.User import User
from helpers.UserHelpers import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
from helpers.MessageHelpers import MessageHelpers
from model.Message import Message
 
def DisplayEveryUser(loggedUser: User, collection: str = "Users"):
        allUser = UserHelpers.GetAllUsers(collection)
        allUsers = list(filter(lambda user: user.Username != loggedUser.Username, allUser))
        displayU = list(map(lambda x: x.Username, allUsers))
        
        while True:
            print("\nSelect one of the user to send a message\n")
            MenuHelpers.DisplayOptions(displayU)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(allUser) + 1):
                    content: str = str(input(f"\nEnter the content for the message to {displayU[optionNo - 1]}:\n\n"))

                    messageSent: bool = MessageHelpers.UpdateMessage(Message(
                        MessageHelpers.CreateMessageId(),
                        loggedUser.Id,
                        allUsers[optionNo - 1].Id,
                        content
                    ))

                    if messageSent: print(f"\nMessage sent to {displayU[optionNo - 1]} successfully.")
                    else: print("\nMessage was not sent.\n")
            except Exception as e:
                raise Exception(f"Something went wrong, could not display all the users\n{e}")


            