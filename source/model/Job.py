from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers

_jobLimit: int = 5

# A Job entity.
@dataclass
class Job:
    Id: int
    Title: str
    Employer: str
    Description: str
    Location: str
    Salary: str
    Poster: User

    # Hydrates a Job entity using a pyrebase response value and returns it.
    def HydrateJob(job):
        return Job(
                Id = job.val()["Id"],
                Title = job.val()["Title"],
                Employer = job.val()["Employer"],
                Description = job.val()["Description"],
                Location = job.val()["Location"],
                Salary = job.val()["Salary"],
                Poster = job.val()["Poster"]
            )

class JobHelpers:
    # Converts this entity into a dictionary.
    def JobToDict(job: Job) -> dict:
        return {
            'Id': str(job.Id),
            'Title': str(job.Title),
            'Employer': str(job.Employer),
            'Description': str(job.Description),
            'Location': str(job.Location),
            'Salary': str(job.Salary),
            'Poster': UserHelpers.UserToDict(job.Poster)
        }

    # Gets a PyreResponse of all jobs from the DB and returns
    # a list of Job entities after constructing it.
    def GetAllJobs(collection: str = "Jobs") -> list[Job]:
        try:
            jobsResponse = database.child(collection).get()

            if jobsResponse == None: return None
            
            jobsResponseList: list = jobsResponse.each()
            if (jobsResponseList == None): return None 
            
            jobs: list[Job] = []
            for job in jobsResponse.each():
                if job == None: continue
                else: jobs.append(Job.HydrateJob(job))

            return jobs
        except:
            return None

    # Creates the specified job in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def CreateJob(job: Job, collection: str = "Jobs") -> bool:
        try:
            database.child(collection).child(
                job.Id).set(JobHelpers.JobToDict(job))
            return True
        except:
            return False

    # Creates a sha256 hash using all job details.
    def CreateJobId(
        title: str,
        employer: str,
        desc: str,
        loc: str,
        salary: str) -> str:
        return hashlib.sha256(
            str.encode(title
                .join(employer)
                .join(desc)
                .join(loc)
                .join(salary))).hexdigest()
    
    # Checks if the maximum number of jobs have been posted.
    def IsLimitMet() -> bool:
        return True if JobHelpers.GetAllJobs() == _jobLimit else False