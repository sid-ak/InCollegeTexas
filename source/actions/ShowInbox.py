from model.User import User
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.UserHelpers import UserHelpers
from helpers.MenuHelpers import MenuHelpers

def ShowInbox(
    loggedUser: User,
    userCollection: str = "Users",
    messageCollection: str = "Messages"):
    try:
        while True:
            receivedMessages: list[Message] = MessageHelpers.GetAllReceivedMessages(
                loggedUser.Id,
                messageCollection = messageCollection)
            
            if receivedMessages == None or receivedMessages == []:
                print("\nNo messages to show.\n")
                return
            
            i: int = 1
            for message in receivedMessages:
                sender: User = UserHelpers.GetUserById(message.SenderId, userCollection)
                isRead: str = "Read" if message.IsRead else "Unread"
                print(f"\n{i}. From: {sender.FirstName} {sender.LastName} ({isRead})")
                i += 1
        
            print("\nEnter a message number to display it:")
            option: int = MenuHelpers.InputOptionNo() - 1
        
            if option == -1: break
            if option not in range(0, len(receivedMessages)): break
            else:
                message: Message = receivedMessages[option]
                MessageHelpers.DisplayMessage(message)
                
                print("\nEnter 1 to reply to the message or 2 to delete it:")
                decision: int = MenuHelpers.InputOptionNo()
                
                if decision == 1:
                    if not MessageHelpers.SendMessage(
                        loggedUser.Id, sender.Id, messageCollection, userCollection):
                        raise Exception()
                    break
                
                elif decision == 2:
                    if not MessageHelpers.DeleteMessageById(message.Id): raise Exception()
                    break


    except Exception as e:
        print(f"Something went wrong.\n{e}")
