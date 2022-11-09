from datetime import datetime, timedelta
from model.AppliedJob import AppliedJob
from model.User import User
from model.Job import Job
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.JobHelpers import JobHelpers


class JobNotificationHelpers:


    # Notifies the user if they did not apply for a job for a certain period of time.
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
    

    # Notifies the user if any jobs were posted after their last log in.
    def NotifyIfNewJobsPosted(loggedUser: User, collection = "Jobs"):

        notificationStr: str = "\nThe following new jobs were posted:\n"
        newJobs: list[Job] = JobHelpers.GetNewJobs(loggedUser, collection)
        if newJobs == None or newJobs == []: return

        print(notificationStr)
        for job in newJobs: print(job.Title)
