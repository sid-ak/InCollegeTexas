from model.User import User
from model.Job import Job
from model.SavedJob import SavedJob
from helpers.SavedJobHelpers import SavedJobHelpers


# deletes the saved job of of the user
def UnsaveJob(loggedUser: User, selectedJob: Job, collection: str = "SavedJobs") -> bool:
    # first check that this job is saved by the user already
    allSavedJobsUser: list[SavedJob] = SavedJobHelpers.GetAllSavedJobsOfUser(loggedUser=loggedUser, collection=collection)

    # now loop through the saved job id's and see if this job is there
    for saved in allSavedJobsUser:
        if saved.JobId == selectedJob.Id:
            # now try to delete this job from SavedJobs node in the DB
            try:
                if not SavedJobHelpers.DeleteSavedJob(savedJob=saved, collection=collection):
                    print("\nError! Deletion of saved job failed.\n")
                else:
                    print("\nSuccess! The saved job is unsaved.\n")
            except Exception as e:
                print(f"\nFailure! Deletion of saved job failed for some reason. {e}\n")

            # we can safely assume that there are no duplicate saved jobs  
            return True
    
    # if by this return statement, the program did not delete the job, it means this job is not saved yet
    print("\nError! You cannot unsave a job that is not saved yet!\n")
    return False