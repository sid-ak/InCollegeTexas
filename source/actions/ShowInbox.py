from model.User import User
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.UserHelpers import UserHelpers
from helpers.MenuHelpers import MenuHelpers

def ShowInbox(
    loggedUser: User,
    userCollection = "Users",
    messageCollection = "Messages"):
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
                MessageHelpers.DisplayMessage(receivedMessages[option])

    except Exception as e:
        print(f"Inbox could not be displayed.\n{e}")
