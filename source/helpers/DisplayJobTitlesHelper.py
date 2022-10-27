from model.Job import Job, JobHelpers
from helpers.MenuHelpers import MenuHelpers

class JobTitleHelper:

    def GetAllJobTitles(collection: str = "Jobs"):
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
                    JobTitleHelper.printDetails(jobList[optionNo-1])

                else:
                    print("Invalid entry! Please try again.\n")
            
            except:
                print("Invalid entry! Please try again.\n")
                break

    
    def printDetails(job: Job):
        print("Job Title: ", job.Title)
        print("Job Description: ", job.Description)
        print("Employer: ", job.Employer)
        print("Job Location: ", job.Location)
        print("Job Salary: ", job.Salary)
        JobTitleHelper.selectJobOptions(job)
    
    def selectJobOptions(job: Job):
        while True:
            print("\nPlease Select one of the following options\n")
            MenuHelpers.DisplayOptions(["Apply for the job", "Save job", "Delete job"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif(optionNo == 1):
                    print("applied for the job") #function to apply for the selected job
                
                elif(optionNo == 2):
                    print("Saved job") #function to save the selected job
                
                elif(optionNo == 3):
                    print("Delete Job") #function to delete a job

                else:
                    print("Invalid entry! Please try again.\n")
            
            except:
                print("Invalid entry! Please try again.\n")

    def FilterJobTitles():
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
