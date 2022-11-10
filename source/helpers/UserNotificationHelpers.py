from model.User import User
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.ProfileHelpers import ProfileHelpers

class UserNotificationHelpers:   
   
    # Notifies the user if they don't have their profile created
    def NotifyIfProfileNotCreated(loggedUser: User):
        if ProfileHelpers.ProfileExists(loggedUser) == False:
            print("\nDon't forget to create a profile")
    
    # Notifies the user if they have any unread messages.
    def NotifyIfUnreadMessages(loggedUser: User, collection: str = "Messages"):
        unreadMessages: list[Message] = MessageHelpers.GetAllReceivedMessages(
            loggedUser.Id, onlyUnread = True, messageCollection = collection)
        
        if unreadMessages == None or unreadMessages == []: return
        
        unreadMessagesCount: int = len(unreadMessages)
        print(f"\nNotifications:\nYou have {unreadMessagesCount} message(s) waiting for you.\n")
