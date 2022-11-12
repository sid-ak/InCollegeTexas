from datetime import datetime, timedelta
from model.AppliedJob import AppliedJob
from model.User import User
from model.Job import Job
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.JobHelpers import JobHelpers


class JobNotificationHelpers:


    # Notifies the user if they did not apply for a job for a certain period of time.
    def NotifyIfNotAppliedJob(loggedUser: User, collection: str = "AppliedJobs"):
        
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
    def NotifyIfNewJobsPosted(loggedUser: User, collection: str = "Jobs"):

        newJobs: list[Job] = JobHelpers.GetNewJobs(loggedUser, collection)
        if newJobs == None or newJobs == []: return

        if len(newJobs) == 1:
            print(f"\nA new job {newJobs[0].Title} has been posted.\n")
            return

        print("\nThe following new jobs were posted:\n")
        for job in newJobs: print(job.Title)


    # Tells the user how many jobs they have applied to
    def NotifyAppliedJobsCount(loggedUser: User, collection: str = "AppliedJobs"):
        JobCount = len(AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser, collection=collection))
        message = "\nYou have currently applied for {}".format(JobCount)
        print(message + " jobs." if JobCount != 1 else message + " job.")


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
