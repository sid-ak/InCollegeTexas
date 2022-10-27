from cmath import log
import imp
from model.User import User
from model.Job import Job
from helpers.UserHelpers import UserHelpers
from helpers.MenuHelpers import MenuHelpers
from helpers.JobsHelpers import JobsHelpers



def ApplyForJob(loggedUser: User, selectedJob: Job) -> bool:
    # first check if the user did not post this job    
    if JobsHelpers.HelpFindUserPosted(loggedUser=loggedUser, jobInterested=selectedJob):
        print("\nFailure! You cannot apply for a job you posted.")
        return False
    
    
