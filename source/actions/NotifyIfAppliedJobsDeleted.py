from model.User import User
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from model.Job import JobHelpers


def NotifyIfAppliedJobsDeleted(loggedUser: User, collection: str = "AppliedJobs"):
    # first get the list of all applied jobs by the user
    allAppliedByUser: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser=loggedUser, collection=collection)
    # now get the list of all existing jobs in the DB
    allExistingJobs: list[Job] = JobHelpers.GetAllJobs()


    # distinct list of job id's of all existing jobs
    idsExisting: list[str] = [allExistingJobs[i].Id for i in range(len(allExistingJobs))]

    # now loop through all applied jobs and see if they are among existing jobs
    # if not, notify the user that their application for that job is removed and delete that applied job
    appliedJobsDeleted: list[AppliedJob] = []
    for appliedJob in allAppliedByUser:
        if appliedJob.JobId not in idsExisting:
            appliedJobsDeleted.append(appliedJob)

    # notify the user by listing the jobs deleted
    if len(appliedJobsDeleted) != 0:
        print("\nAttention! Among the jobs you have applied for some have been deleted.")
        print("\nHere they are: \n")
        for i in range(len(appliedJobsDeleted)):
            print(f"{i+1}. {appliedJobsDeleted[i].JobTitle} from {appliedJobsDeleted[i].JobEmployer}")
        
        # now try to delete these jobs
        for job in appliedJobsDeleted:
            try:
                AppliedJobHelpers.DeleteAppliedJob(appliedJob=job)
            except Exception as e:
                print("\nFailure! Could not delete the applied job for some reason. {e}\n")
        
        print("\nYour applications for these jobs are revoked.\n")
            
        
    
