from cmath import log
from curses import flash
import imp
from symbol import term
from model.User import User
from model.Job import Job
from helpers.UserHelpers import UserHelpers
from helpers.MenuHelpers import MenuHelpers
from helpers.JobsHelpers import JobsHelpers
from model.AppliedJob import AppliedJob
from model.AppliedJob import AppliedJobHelpers



def ApplyForJob(loggedUser: User, selectedJob: Job) -> bool:
    # first check if the user did not post this job  
    if JobsHelpers.HelpFindUserPosted(loggedUser=loggedUser, jobInterested=selectedJob):
        print("\nFailure! You cannot apply for a job you posted.\n")
        return False

    # now check if the user has already applied for this job
    if JobsHelpers.HelpFindIfApplied(loggedUser=loggedUser, jobInterested=selectedJob):
        print("\nFailure! You have already applied for this job.\n")
        return False

    # now let's proceed with collecting the relevant information on the job to be applied
    try:
        terminateOperation: bool = False

        # get and validate graduation date
        graduationDate: str = input("\nPlease enter graduation date (-1 to Exit): ")
        if graduationDate == "-1":
            print("\nYou have selected to quit\n")
            return True
        else:
            # validate that the input is within the pattern mm/dd/yyyy
            if not JobsHelpers.HelpValidateDate(graduationDate):
                print("\nError! Invalid graduation date, try again.")
                while True:
                    graduationDate = input("\nPlease enter graduation date (-1 to Exit): ")
                    if graduationDate == "-1":
                        terminateOperation = True
                        break
                    if not JobsHelpers.HelpValidateDate(graduationDate):
                        print("\nError! Invalid graduation date, try again.")
                    else:
                        break
                if terminateOperation:
                    print("\nYou have selected to quit\n")
                    return True

        # get and validate start date
        startDate: str = input("\nPlease enter start date (-1 to Exit): ")
        if startDate == "-1":
            print("\nYou have selected to quit\n")
            return True
        else:
            # validate that the input is within the pattern mm/dd/yyyy
            if not JobsHelpers.HelpValidateDate(startDate):
                print("\nError! Invalid start date, try again.")
                while True:
                    startDate = input("\nPlease enter start date (-1 to Exit): ")
                    if  startDate == "-1":
                        terminateOperation = True
                        break
                    if not JobsHelpers.HelpValidateDate(startDate):
                        print("\nError! Invalid start date, try again.")
                    else:
                        break
                if terminateOperation:
                    print("\nYou have selected to quit\n")
                    return True
        
        # get a paragraph why they are a good fit for the role
        goodFitReasoning = input("Please explain why you think you would be a good fit for this role (-1 To Exit): ")
        if goodFitReasoning == "-1":
            print("\nYou have selected to quit\n")
            return True
        else:
            if len(goodFitReasoning) == 0:
                print("\nError! Empty text provided, try again")
                while True:
                    goodFitReasoning = input("Please explain why you think you would be a good fit for this role (-1 To Exit): ")
                    if goodFitReasoning == "-1":
                        print("\nYou have selected to quit\n")
                        terminateOperation = True
                        break
                    if len(goodFitReasoning) == 0:
                        print("\nError! Empty text provided, try again")
                    else:
                        break


        appliedJob: AppliedJob = AppliedJob(
            UserId=loggedUser.Id, 
            JobId=selectedJob.Id,
            GraduationDate=graduationDate,
            StartDate=startDate,
            GoodFitReasoning=goodFitReasoning
            )

        if AppliedJobHelpers.CreateAppliedJob(appliedJob=appliedJob):
            print("\nSuccess! You have applied for the job!\n")
            return True
        else:
            raise Exception("Create Applied Job failed.")

    except:
        return False
        
