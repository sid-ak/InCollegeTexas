from model.Job import Job, JobHelpers
from model.User import User
from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayJobTitlesHelper import JobTitleHelper


# Allows a logged in user to create a job posting or view all the jobs.
def FindJobInternshipAction(loggedUser: User):
    while True:
        print("\nPlease select one of the following options:\n")
        MenuHelpers.DisplayOptions(["Post a Job", "Find a Job"])

        try:
            optionNo: int = MenuHelpers.InputOptionNo()
            
            if optionNo == -1: break
            
            elif optionNo == 1:
                if (JobHelpers.IsJobLimitMet()):
                    print("\nThe maximum have jobs have been posted" +
                        "\nPlease come back later, thank you.")
                    break

                # Construct the job by taking user input
                job: Job = MakeJob(loggedUser)
                
                # Push that job to the DB.
                if JobHelpers.CreateJob(job) == True:
                    print(f"\n{job.Title} created successfully.")
                else:
                    raise Exception("CreateJob failed.")

            elif optionNo == 2:
                JobTitleHelper.DisplayJobTitle(loggedUser)

        except Exception as e:
              raise Exception(f"Something went wrong while selecting job option.\n{e}")
    

# Constructs the job by taking user input and returns it.
def MakeJob(jobPoster: User) -> Job:
    print("\nPlease enter the following details for the job posting: ")
    title: str = input("\nTitle: ")
    employer: str = input("\nEmployer: ")
    desc: str = input("\nDescription:\n")
    loc: str = input("\n\nLocation: ")
    salary: str = input("\nSalary: ")

    id: str = JobHelpers.CreateJobId(
        title,
        employer,
        desc,
        loc,
        salary
    )

    return Job(id, title, employer, desc, loc, salary, jobPoster)