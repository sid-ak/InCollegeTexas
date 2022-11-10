from model.User import User
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.ProfileHelpers import ProfileHelpers

class UserNotificationHelpers:   
   
    # Notifies the user if they don't have their profile created
    def NotifyIfProfileNotCreated(loggedUser: User):
        if ProfileHelpers.ProfileExists(loggedUser) == False:
            print("\nDon't forget to create a profile")