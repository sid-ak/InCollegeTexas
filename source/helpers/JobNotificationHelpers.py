from datetime import datetime, timedelta
from model.AppliedJob import AppliedJob
from model.User import User
from helpers.AppliedJobHelpers import AppliedJobHelpers

class JobNotificationHelpers:


    # Notifies the user if they did not apply for a job for a certain period     of time.
    def NotifyIfNotAppliedJob(loggedUser: User, collection = "AppliedJobs"):
        
        lastAppliedJob: AppliedJob = AppliedJobHelpers.GetLastAppliedJob(loggedUser, collection)
        if lastAppliedJob == None: return

        lastAppliedJobTimestamp: datetime = lastAppliedJob._CreatedTimestamp
        currentTimestamp: datetime = datetime.now()

        maxDays: int = 7
        timeElapsed: timedelta = currentTimestamp - lastAppliedJobTimestamp
        daysElapsed: int = timeElapsed.days

        if daysElapsed >= maxDays:
            print("\nRemember - you're going to want to have a job when you graduate."
                + "\nMake sure that you start to apply for jobs today!\n")
