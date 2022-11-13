from model.User import User
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from helpers.ProfileHelpers import ProfileHelpers
from helpers.UserHelpers import UserHelpers
from datetime import datetime

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


    # To show the logged in user the new users that have signed up
    def NotifyIfNewUsers(loggedUser: User, collection: str = "Users"):
        # Get all users
        allUsers: list[User] = UserHelpers.GetAllUsers(collection)
        if allUsers == None or allUsers == []:
            return None

        # find the users who have signed up after the logged in user's last login time
        newUsers: list[User] = list(filter(
            lambda user: user._SignUpTimestamp > loggedUser._LastLoginTimestamp and user.Id != loggedUser.Id, allUsers
        ))

        # print the new users
        if newUsers != None and newUsers != []: 
            for user in newUsers:
                print("\n" + user.FirstName + " " + user.LastName + " has joined InCollege.")