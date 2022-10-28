from model.SavedJob import SavedJob
from model.User import User
from model.Job import Job
from helpers.JobsHelpers import JobsHelpers
from model.SavedJob import SavedJobHelpers


# saves the specified job for the specified user
def SaveJob(loggedUser: User, selectedJob: Job) -> bool:
    try:
        # first check if the user already saved the job
        if JobsHelpers.HelpFindIfSaved(loggedUser=loggedUser, jobInterested=selectedJob):
            print("\nError! You have already saved this job\n")
            return False
        
        # now we can save the job for the user
        id: str = SavedJobHelpers.CreateSaveJobId(
            selectedJob.Id,
            loggedUser.Id
        )
        savedJob: SavedJob = SavedJob(Id=id, JobId=selectedJob.Id, UserId=loggedUser.Id)

        if SavedJobHelpers.CreateSavedJob(savedJob=savedJob):
            print("\nSuccess! You have saved the job!\n")
            return True
        else:
            raise Exception("Create Saved Job failed.")

    except:
        print("\nError! Operation failed for some reason.\n")
        return False