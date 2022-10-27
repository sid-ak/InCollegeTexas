from cmath import log
from curses import flash
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
    
    # now let's proceed with collecting the relevant information on the job to be applied
    print("Please enter graduation date:")
    try:
        graduationDate = MenuHelpers.InputOptionNo()
        
        if graduationDate == -1:
            print("\nYou have selected to quit")
            return True
        else:
            # validate that the input is within the pattern mm/dd/yyyy
            result = JobsHelpers.HelpValidateDate(graduationDate)
    
    except:
        return False
    
