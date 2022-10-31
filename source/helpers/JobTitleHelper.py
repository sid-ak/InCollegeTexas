from helpers.JobsHelpers import JobsHelpers
from model.Job import Job, JobHelpers
from model.User import User
from helpers.MenuHelpers import MenuHelpers
from actions.ApplyForJob import ApplyForJob
from actions.SaveJob import SaveJob
from model.User import User
from actions.UnsaveJob import UnsaveJob


class JobTitleHelper:

    #Gives an option to a logged in user to either filter the jobs or view them all
    def DisplayJobTitle(loggedUser: User, collection: str = "Jobs"):
        while True:
            print("\nPlease select if you want to filter the Job:\n")
            MenuHelpers.DisplayOptions(["Yes", "No"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break
                
                elif optionNo == 1:
                    JobTitleHelper.FilterJobs(loggedUser)
                
                elif optionNo == 2:
                    JobTitleHelper.DisplayJobs(
                        JobHelpers.GetAllJobs(collection), loggedUser)

                else:
                    print("Invalid entry! Please try again.\n")

            except Exception as e:
              raise Exception(f"Something went wrong, could not filter the jobs.\n{e}")

    
    #Print the details of the job after the logged in user has selected the job
    def PrintDetails(loggedUser: User, job: Job):
        print(f"Job Title: {job.Title}")
        print(f"Job Description: {job.Description}")
        print(f"Employer: {job.Employer}")
        print(f"Job Location: {job.Location}")
        print(f"Job Salary: {job.Salary}")
        JobTitleHelper.SelectJobOptions(loggedUser=loggedUser, job=job)
    
    
    #This Function gives the option to either apply or to save the job
    def SelectJobOptions(loggedUser: User, job: Job):
        while True:

            print("\nPlease select one of the following options:\n")
            optionList = ["Apply for the job", "Save the job", "Unsave the job"]

            flag: bool = job.Poster["Username"] == loggedUser.Username
            if flag:
                optionList.append("Delete job")

            MenuHelpers.DisplayOptions(optionList)

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

                elif (optionNo == 3):
                    if UnsaveJob(loggedUser=loggedUser, selectedJob=job):
                        print("\nOperation successfully completed!\n")
                    else:
                        print("\nFailure! Operation not completed!\n")

                elif(optionNo == 4 and flag):
                    if JobHelpers.DeleteJob(job) == True:
                        print(f"\n{job.Title} deleted successfully.")
                    else:
                        raise Exception("DeleteJob failed.")

                else:
                    print("Invalid entry! Please try again.\n")
            
            except Exception as e:
              raise Exception(f"Something went wrong, could not show the job options.\n{e}")

    
    # Filters jobs into applied, unapplied and saved.
    def FilterJobs(
        loggedUser: User,
        collectionApplied: str = "AppliedJobs",
        collectionSaved: str = "SavedJobs"):
        
        while True:
            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["Show applied jobs", "Show unapplied jobs", "Show saved Jobs"])

            try:
                optionNo: int = MenuHelpers.InputOptionNo()
                filteredJobs: list[Job] = []

                if optionNo == -1: break

                elif(optionNo == 1):
                    filteredJobs = JobsHelpers.GetAppliedJobs(
                        loggedUser, collectionApplied)
                    if filteredJobs != []:
                        print("\nApplied jobs found.")

                elif(optionNo == 2):
                    filteredJobs = JobsHelpers.GetUnappliedJobs(
                        loggedUser, collectionApplied)
                    if filteredJobs != []:
                        print("\nUnapplied jobs found.")

                elif(optionNo == 3):
                    filteredJobs = JobsHelpers.GetSavedJobs(
                        loggedUser, collectionSaved)
                    if filteredJobs != []:
                        print("\nSaved jobs found.")

                else:
                    print("Invalid entry! Please try again.\n")
                
                if filteredJobs != []:
                    JobTitleHelper.DisplayJobs(filteredJobs, loggedUser)
                else:
                    print("\nNo filtered jobs found.")

            except Exception as e:
              raise Exception(f"Something went wrong, could not filter the jobs by the options.\n{e}")

    
    # Helper method to display the given list of jobs.
    def DisplayJobs(jobList: list[Job], loggedUser: User):
        try:
            while True:
                jobTitleList: list[str] = list(map(lambda job: job.Title, jobList))

                print("\nSelect one of the following jobs to continue:\n")
                MenuHelpers.DisplayOptions(jobTitleList)
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(jobTitleList) + 1):
                    JobTitleHelper.PrintDetails(loggedUser, jobList[optionNo - 1])

                else: print("Invalid entry! Please try again.\n")

        except Exception as e:
            raise Exception(f"Something went wrong, could not select one of the jobs.\n{e}")
