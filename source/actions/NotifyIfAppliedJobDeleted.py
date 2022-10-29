from model.User import User
from model.AppliedJob import AppliedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from model.Job import Job
from model.Job import JobHelpers


def NotifyIfAppliedJobDeleted(loggedUser: User, collection: str = "AppliedJobs"):
    print("\nIN NOTIFY IF JOB DELETED")
    # first get the list of all applied jobs by the user
    allAppliedByUser: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser=loggedUser, collection=collection)
    # now get the list of all existing jobs in the DB
    allExistingJobs: list[Job] = JobHelpers.GetAllJobs()


    # distinct list of job id's of all existing jobs
    idsExisting: list[str] = [allExistingJobs[i].Id for i in range(len(allExistingJobs))]

    print("HERE IS THE LIST OF ALL APPLIED JOBS: ")
    for job in allAppliedByUser:
        print(job.JobId)
    print("HERE IS THE LIST OF ALL EXISTING JOBS IN THE DB: ")
    for job in idsExisting:
        print(job)

    # now loop through all applied jobs and see if they are among existing jobs
    # if not, notify the user that their application for that job is removed and delete that applied job
    appliedJobsDeleted: list[AppliedJob] = []
    for appliedJob in allAppliedByUser:
        if appliedJob.JobId not in idsExisting:
            appliedJobsDeleted.append(appliedJob)

    if len(appliedJobsDeleted) != 0:
        print("\nAttention! Among the jobs you have applied for some have been deleted.")
        print("Here they are: ")
        
    
