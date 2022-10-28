from cmath import log
from model.Job import Job, JobHelpers
from model.User import User
from helpers.MenuHelpers import MenuHelpers
from actions.ApplyForJob import ApplyForJob
from actions.SaveJob import SaveJob


class JobTitleHelper:

    #Gives an option to a logged in user to either filter the jobs or view them all
    def DisplayJobTitle(loggedUser: User):
        while True:
            print("\nPlease select if you want to filter the Job:\n")
            MenuHelpers.DisplayOptions(["Yes", "No"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break
                
                elif optionNo == 1:
                    JobTitleHelper.FilterJobTitles(loggedUser=loggedUser)
                
                elif optionNo == 2:
                    JobTitleHelper.GetAllJobTitles(loggedUser=loggedUser)

                else:
                    print("Invalid entry! Please try again.\n")

            except:
                print("Invalid entry! Please try again.\n")
                break

    #This functiones give the title of all the jobs in the database and gives an ption to select the job 
    def GetAllJobTitles(loggedUser: User, collection: str = "Jobs"):
        while True:

            jobList = JobHelpers.GetAllJobs()
            jobTitleList = []

            for job in jobList:
                jobTitleList.append(job.Title)
            
            print("\nPlease Select one of the following jobs\n")
            MenuHelpers.DisplayOptions(jobTitleList)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(jobList) + 1):
                    JobTitleHelper.PrintDetails(loggedUser=loggedUser, job=jobList[optionNo-1])

                else:
                    print("Invalid entry! Please try again.\n")
            
            except:
                print("Invalid entry! Please try again.\n")
                break

    #Print the deatils of the job after the logged in user has selected the job
    def PrintDetails(loggedUser: User, job: Job):
        print("Job Title: ", job.Title)
        print("Job Description: ", job.Description)
        print("Employer: ", job.Employer)
        print("Job Location: ", job.Location)
        print("Job Salary: ", job.Salary)
        JobTitleHelper.SelectJobOptions(loggedUser=loggedUser, job=job)
    
    #This Function gives the option to either apply or to save the job
    def SelectJobOptions(loggedUser: User, job: Job):
        while True:
            print("\nPlease Select one of the following options\n")
            MenuHelpers.DisplayOptions(["Apply for the job", "Save job", "Delete job"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif(optionNo == 1):
                    print("You have selected to apply for job.")
                    if ApplyForJob(loggedUser=loggedUser, selectedJob=job):
                        print("\nOperation successfully completed!\n")
                    else:
                        print("\nFailure! Operation not completed!\n")
                
                elif(optionNo == 2):
                    if SaveJob(loggedUser=loggedUser, selectedJob=job):
                        print("\nOperation successfully completed!\n")
                    else:
                        print("\nFailure! Operation not completed!\n")

                else:
                    print("Invalid entry! Please try again.\n")
            
            except:
                print("Invalid entry! Please try again.\n")

    def FilterJobTitles(loggedUser: User):
        while True:
            print("\nPlease Select one of the following options\n")
            MenuHelpers.DisplayOptions(["Show applied jobs", "Show unapplied jobs", "Show saved Jobs"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif(optionNo == 1):
                    print("List of applied Jobs") #applied job function

                elif(optionNo == 2):
                    print("List of unapplied Jobs") #unapplied job function

                elif(optionNo == 3):
                    print("List of saved Jobs") #saved jobs function

                else:
                    print("Invalid entry! Please try again.\n")
            except:
                print("Invalid entry! Please try again.\n")