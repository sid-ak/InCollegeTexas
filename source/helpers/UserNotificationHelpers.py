from model.User import User
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from model.Job import JobHelpers
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.ProfileHelpers import ProfileHelpers

class UserNotificationHelpers:   
   
    # Notifies the user if they don't have their profile created
    def NotifyIfProfileNotCreated(loggedUser: User):
        if ProfileHelpers.ProfileExists(loggedUser) == False:
            print("\nDon't forget to create a profile")

    # Tells the user how many jobs they have applied to
    def NotifyAppliedJobsCount(loggedUser: User):
        JobCount = len(AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser))
        message = "\nYou have currently applied for {}".format(JobCount)
        print(message + " jobs." if JobCount != 1 else message + " job.") 