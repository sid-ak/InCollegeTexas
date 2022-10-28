from model.SavedJob import SavedJob
from model.User import User
from model.Job import Job


# saves the specified job for the specified user
def SaveJob(loggedUser: User, selectedJob: Job) -> bool:
    # first check if the user already saved the job
    pass