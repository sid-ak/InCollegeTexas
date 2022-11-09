from model.User import User
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from model.Job import JobHelpers
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.ProfileHelpers import ProfileHelpers

class NotificationHelpers:


    # Notifies the user if they applied for jobs that were deleted.
    def NotifyIfAppliedJobsDeleted(
        loggedUser: User,
        appliedJobsCollection: str = "AppliedJobs",
        allJobsCollection: str = "Jobs"):
        # first get the list of all applied jobs by the user
        allAppliedByUser: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser=loggedUser, collection=appliedJobsCollection)
        # now get the list of all existing jobs in the DB
        allExistingJobs: list[Job] = JobHelpers.GetAllJobs(collection=allJobsCollection)

        if allAppliedByUser != None and allAppliedByUser != [] and allExistingJobs != None and allExistingJobs != []:
            # distinct list of job id's of all existing jobs
            idsExisting: list[str] = [allExistingJobs[i].Id for i in range(len(allExistingJobs))]

            # now loop through all applied jobs and see if they are among existing jobs
            # if not, notify the user that their application for that job is removed and delete that applied job
            appliedJobsDeleted: list[AppliedJob] = []
            for appliedJob in allAppliedByUser:
                if appliedJob.JobId not in idsExisting:
                    appliedJobsDeleted.append(appliedJob)

            # notify the user by listing the jobs deleted
            if appliedJobsDeleted != None and len(appliedJobsDeleted) != 0:
                # now try to delete these jobs
                for job in appliedJobsDeleted:
                    try:
                        AppliedJobHelpers.DeleteAppliedJob(appliedJob=job, collection=appliedJobsCollection)
                    except Exception as e:
                        print("\nFailure! Could not delete the applied job for some reason. {e}\n")

                if appliedJobsDeleted != None:
                    # now let the user know which applied jobs got deleted
                    print("\nAttention! Among the jobs you have applied for some have been deleted.")
                    print("\nHere they are: \n")
                    for i in range(len(appliedJobsDeleted)):
                        print(f"{i+1}. {appliedJobsDeleted[i].JobTitle} from {appliedJobsDeleted[i].JobEmployer}")
                    
                    print("\nYour applications for these jobs are revoked.\n")  


    # Notifies the user if they have any unread messages.
    def NotifyIfUnreadMessages(loggedUser: User, collection = "Messages"):
        unreadMessages: list[Message] = MessageHelpers.GetAllReceivedMessages(
            loggedUser.Id, onlyUnread = True, messageCollection = collection)
        
        if unreadMessages == None or unreadMessages == []: return
        
        unreadMessagesCount: int = len(unreadMessages)
        print(f"\nNotifications:\nYou have {unreadMessagesCount} message(s) waiting for you.\n")

    # Notifies the user if they don't have their profile created
    def NotifyIfProfileNotCreated(loggedUser: User):
        if ProfileHelpers.ProfileExists(loggedUser) == False:
            print("\nDon't forget to create a profile")
