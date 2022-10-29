from model.Job import Job, JobHelpers
from helpers.MenuHelpers import MenuHelpers

class JobTitleHelper:

    #Gives an option to a logged in user to either filter the jobs or view them all
    def DisplayJobTitle(loggedUserUsername, collection: str = "Jobs"):
        while True:
            print("\nPlease select if you want to filter the Job:\n")
            MenuHelpers.DisplayOptions(["Yes", "No"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break
                
                elif optionNo == 1:
                    JobTitleHelper.FilterJobTitles()
                
                elif optionNo == 2:
                    JobTitleHelper.GetAllJobTitles(loggedUserUsername, collection)

                else:
                    print("Invalid entry! Please try again.\n")

            except Exception as e:
              raise Exception(f"Something went wrong, could not filter the jobs.\n{e}")

    #This functiones give the title of all the jobs in the database and gives an ption to select the job 
    def GetAllJobTitles(loggedUserUsername, collection: str = "Jobs"):
        while True:

            jobList = JobHelpers.GetAllJobs(collection)
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
                    if(jobList[optionNo-1].Poster['Username'] == loggedUserUsername): flag = True
                    JobTitleHelper.PrintDetails(jobList[optionNo-1], flag)

                else:
                    print("Invalid entry! Please try again.\n")
            
            except Exception as e:
              raise Exception(f"Something went wrong,  could not select one of the jobs.\n{e}")

    #Print the deatils of the job after the logged in user has selected the job
    def PrintDetails(job: Job, flag:bool):
        print(f"Job Title: {job.Title}")
        print(f"Job Description: {job.Description}")
        print(f"Employer: {job.Employer}")
        print(f"Job Location: {job.Location}")
        print(f"Job Salary: {job.Salary}")
        JobTitleHelper.SelectJobOptions(job, flag)
    
    #This Function gives the option to either apply or to save the job
    def SelectJobOptions(job: Job, flag):
        while True:

            print("\nPlease Select one of the following options\n")
            optionList = ["Apply for the job", "Save job"]

            if flag:
                optionList.append("Delete job")

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
            
            except Exception as e:
              raise Exception(f"Something went wrong, could not show the job options.\n{e}")

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
              raise Exception(f"Something went wrong, could not filter the jobs by the options.\n{e}")

