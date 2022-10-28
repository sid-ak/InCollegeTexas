from cmath import e
from curses import can_change_color
from model.Job import Job, JobHelpers
from helpers.MenuHelpers import MenuHelpers
from model.User import User

class JobTitleHelper:

    #Gives an option to a logged in user to either filter the jobs or view them all
    def DisplayJobTitle(canDeleteJob):
        while True:
            print("\nPlease select if you want to filter the Job:\n")
            MenuHelpers.DisplayOptions(["Yes", "No"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break
                
                elif optionNo == 1:
                    JobTitleHelper.FilterJobTitles(canDeleteJob = canDeleteJob)
                
                elif optionNo == 2:
                    JobTitleHelper.GetAllJobTitles(canDeleteJob = canDeleteJob)

                else:
                    print("Invalid entry! Please try again.\n")

            except:
                print("Invalid entry! Please try again.\n")
                break

    #This functiones give the title of all the jobs in the database and gives an ption to select the job 
    def GetAllJobTitles(collection: str = "Jobs", canDeleteJob = None):
        while True:

            jobList = JobHelpers.GetAllJobs()
            jobTitleList = []
            flag = False

            for job in jobList:
                jobTitleList.append(job.Title)
            
            print("\nPlease Select one of the following jobs\n")
            MenuHelpers.DisplayOptions(jobTitleList)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(jobList) + 1):
                    if(jobList[optionNo-1].Poster['Username'] == canDeleteJob): flag = True
                    JobTitleHelper.PrintDetails(jobList[optionNo-1], flag)

                else:
                    print("Invalid entry! Please try again.\n")
            
            except:
                print("Invalid entry! Please try again.\n")
                break

    #Print the deatils of the job after the logged in user has selected the job
    def PrintDetails(job: Job, flag):
        print("Job Title: ", job.Title)
        print("Job Description: ", job.Description)
        print("Employer: ", job.Employer)
        print("Job Location: ", job.Location)
        print("Job Salary: ", job.Salary)
        JobTitleHelper.SelectJobOptions(job, flag)
    
    #This Function gives the option to either apply or to save the job
    def SelectJobOptions(job: Job, flag):
        while True:

            print("\nPlease Select one of the following options\n")
            optionList = ["Apply for the job", "Save job"]

            if flag:
                optionList.append("Delete")

            MenuHelpers.DisplayOptions(optionList)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif(optionNo == 1):
                    print("applied for the job") #function to apply for the selected job
                
                elif(optionNo == 2):
                    print("Saved job") #function to save the selected job
                
                elif(optionNo == 3 and flag):

                    if JobHelpers.DeleteJob(job) == True:
                        print(f"\n{job.Title} created successfully.")
                    else:
                        raise Exception("CreateJob failed.")

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
            except Exception as e:
              raise Exception(f"Something went wrong while selecting job option.\n{e}")

