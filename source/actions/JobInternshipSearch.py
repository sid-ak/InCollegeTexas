
# this function is under construction
from model.Job import Job, JobHelpers
from model.User import User

def FindJobInternshipAction(loggedUser: User) -> bool:
    print("\nPlease enter one of the following options to continue:\n"
        + "1 - Post a job")
    optionNo: int = int(input("\nEnter (-1 to Exit): "))
    
    try:
        if optionNo == -1:
            # TODO: Implement go back functionality.
            return False
        
        elif optionNo == 1:
            job: Job = MakeJob()
            raise Exception() if JobHelpers.CreateJob(job) == False else print(
                f"{job.Title} created successfully."
            )
        
        FindJobInternshipAction(loggedUser)
    except:
        print(f"{job.Title} could not be created.")
        return False

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