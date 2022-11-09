from model.User import User
from model.SavedJob import SavedJob
from model.Job import Job
from helpers.SavedJobHelpers import SavedJobHelpers
from helpers.JobHelpers import JobHelpers


def DeleteSavedJobIfDeleted(loggedUser: User, savedJobsCollection: str = "SavedJobs", jobsCollection: str ="Jobs"):
    # first get the list of all saved jobs by the user
    allSavedJobs: list[SavedJob] = SavedJobHelpers.GetAllSavedJobsOfUser(loggedUser=loggedUser, collection=savedJobsCollection)
    # now get the list of all existing jobs in the DB
    allExistingJobs: list[Job] = JobHelpers.GetAllJobs(collection=jobsCollection)

    if allSavedJobs != None and len(allSavedJobs) != 0 and allExistingJobs != None and len(allExistingJobs) != 0:

        # distinct list of job id's of all existing jobs
        idsExisting: list[str] = [allExistingJobs[i].Id for i in range(len(allExistingJobs))]

        # now loop through all saved jobs and see if they are among existing jobs
        # if not, delete these saved jobs from the DB
        savedJobsDeleted: list[SavedJob] = []
        for savedJob in allSavedJobs:
            if savedJob.JobId not in idsExisting:
                savedJobsDeleted.append(savedJob)
        
        if savedJobsDeleted != None and len(savedJobsDeleted) != 0:
            for job in savedJobsDeleted:
                try:
                    SavedJobHelpers.DeleteSavedJob(savedJob=job, collection=savedJobsCollection)
                except Exception as e:
                    print("\nFailure! Could not delete the saved job for some reason. {e}\n")
            
            # let the user know that some of their saved jobs have been deleted and therefore will be unsaved
            print("\nAttention! Among the jobs you have saved some have been deleted.")
            print("They have been removed from your list of saved jobs.\n")