from datetime import datetime, timedelta
from model.AppliedJob import AppliedJob
from model.User import User
from helpers.AppliedJobHelpers import AppliedJobHelpers

class JobNotificationHelpers:


    # Notifies the user if they did not apply for a job for a certain period     of time.
    def NotifyIfNotAppliedJob(loggedUser: User, collection = "AppliedJobs"):
        
        notificationStr: str = "\nRemember - you're going to want to have a job when you graduate."
        notificationStr += "\nMake sure that you start to apply for jobs today!\n"

        lastAppliedJob: AppliedJob = AppliedJobHelpers.GetLastAppliedJob(loggedUser, collection)
        if lastAppliedJob == None:
            print(notificationStr)
            return

        lastAppliedJobTimestamp: datetime = lastAppliedJob._CreatedTimestamp
        currentTimestamp: datetime = datetime.now()

        maxDays: int = 7
        timeElapsed: timedelta = currentTimestamp - lastAppliedJobTimestamp
        daysElapsed: int = timeElapsed.days

        if daysElapsed >= maxDays: print(notificationStr)

    # Tells the user how many jobs they have applied to
    def NotifyAppliedJobsCount(loggedUser: User):
        JobCount = len(AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser))
        message = "\nYou have currently applied for {}".format(JobCount)
        print(message + " jobs." if JobCount != 1 else message + " job.") 
