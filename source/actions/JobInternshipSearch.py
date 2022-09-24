from model.Job import Job, JobHelpers
from model.User import User

def FindJobInternshipAction(loggedUser: User):
    while True:
        print("\nPlease enter one of the following options to continue:\n"
            + "1 - Post a job")
                
        try:
            optionNo: int = int(input("\nEnter (-1 to go back): "))
            
            if optionNo == -1: break
            
            elif optionNo == 1:
                if (JobHelpers.IsLimitMet()):
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

        except:
            print(f"Exception: \n{job.Title} could not be created.")
    

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