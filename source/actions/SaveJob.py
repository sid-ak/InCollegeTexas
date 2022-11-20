from model.SavedJob import SavedJob
from model.User import User
from model.Job import Job
from helpers.JobHelpers import JobHelpers
from helpers.SavedJobHelpers import SavedJobHelpers
from apis.outputAPIs import SavedJobsAPI


# saves the specified job for the specified user
def SaveJob(loggedUser: User, selectedJob: Job, collection: str = "SavedJobs", userCollection:str = "Users") -> bool:
    try:
        # first check if the user already saved the job
        if JobHelpers.HelpFindIfSaved(loggedUser=loggedUser, jobInterested=selectedJob):
            print("\nError! You have already saved this job\n")
            return False
        
        # now we can save the job for the user
        id: str = SavedJobHelpers.CreateSaveJobId(
            selectedJob.Id,
            loggedUser.Id
        )
        savedJob: SavedJob = SavedJob(Id=id, JobId=selectedJob.Id, UserId=loggedUser.Id)

        if SavedJobHelpers.CreateSavedJob(savedJob=savedJob, loggedUser=loggedUser, collection=collection):
            if not SavedJobsAPI(userCollection=userCollection, savedJobsCollection=collection):
                raise Exception("Couldn't update output file with saved job\n")
            print("\nSuccess! You have saved the job!\n")
            return True
        else:
            raise Exception("Create Saved Job failed.")

    except Exception as e:
        print(f"\nError! Operation failed for some reason.{e}\n")
        return False