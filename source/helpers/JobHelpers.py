from firebaseSetup.Firebase import database
import hashlib
from model.Job import Job
from model.User import User
from model.AppliedJob import AppliedJob
from model.SavedJob import SavedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.SavedJobHelpers import SavedJobHelpers
from datetime import datetime

class JobHelpers:

    _jobLimit: int = 10

    # Converts this entity into a dictionary.
    def JobToDict(job: Job) -> dict:
        return {
            'Id': str(job.Id),
            'Title': str(job.Title),
            'Employer': str(job.Employer),
            'Description': str(job.Description),
            'Location': str(job.Location),
            'Salary': str(job.Salary),
            'PosterId': str(job.PosterId),
            '_CreatedTimestamp': str(job._CreatedTimestamp)
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
    def IsJobLimitMet(collection: str = "Jobs") -> bool:
        allJobs: list[User] = JobHelpers.GetAllJobs(collection)
        
        if allJobs == None or allJobs == []:
            return False
        
        return True if len(allJobs) == JobHelpers._jobLimit else False


    def DeleteJob(job: Job, collection: str = "Jobs"):
        jobs = JobHelpers.GetAllJobs(collection=collection)
        if (jobs != None):
            for dbJob in jobs:
                if job.Id == dbJob.Id and job.Title == dbJob.Title:
                    database.child(collection).child(job.Id).remove()
                    return True
        else:
            return False


    def GetJobByID(jobID: str, collection: str = "Jobs") -> Job:
        try:
            jobs = JobHelpers.GetAllJobs(collection=collection) 

            if jobs == None:
                raise Exception(
                    f"Could not get the specified job with Job ID: {jobID}")

            for job in jobs:
                if(job.Id == jobID): 
                    return job
        
        except:
            print(f"Could not get the specified job with Job ID: {jobID}")
        
    
        # helps find if the user did not post the job provided
    def HelpFindUserPosted(loggedUser: User, jobInterested: Job) -> bool:
        return loggedUser.Id == jobInterested.PosterId


    # helps find if the user already applied for the job provided
    def HelpFindIfApplied(loggedUser: User, jobInterested: Job, collection: str = "AppliedJobs") -> bool:
        allApplied: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobs(collection)
        if allApplied == None or allApplied == []: return False

        for applied in allApplied:
            # the combination of user id and job id is equal to id of applied - means it is not unique
            if (loggedUser.Id + jobInterested.Id) == (applied.UserId + applied.JobId):
                return True
            
        return False

    
    # helps find if the user already saved the job provided
    def HelpFindIfSaved(loggedUser: User, jobInterested: Job, collection: str = "SavedJobs") -> bool:
        allSaved: list[SavedJob] = SavedJobHelpers.GetAllSavedJobs(collection)
        if allSaved == None or allSaved == []: return False

        for saved in allSaved:
            if (loggedUser.Id == saved.UserId) and (jobInterested.Id == saved.JobId):
                return True
            
        return False


    # helps find out if the provided input corresponds to date within pattern mm/dd/yyyy
    def HelpValidateDate(input: str) -> bool:
        try:
            divided: str = input.split("/")
            if len(divided) == 3:
                if len(divided[0]) == 2 and len(divided[1]) == 2 and len(divided[2]) == 4:
                    month: int = int(divided[0])
                    day: int = int(divided[1])
                    year: int = int(divided[2])

                    if month not in range(1, 13):
                        return False
                    if day not in range(1, 32):
                        return False
                    if year not in range(1, 7000):
                        return False
                    
                    return True
                else:
                    return False
            else:
                return False
        
        except:
            return False


    # Returns a list of applied jobs of type list[Job] and not list[AppliedJob].    
    def GetAppliedJobs(loggedUser: User, collection: str = "AppliedJobs") -> list[Job]:
        try:
            appliedJobs: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser, collection)

            if appliedJobs == None:
                raise Exception(
                    f"Could not get any applied job by the user: {loggedUser.Username}")

            appliedJobTitles: list[str] = []
            jobs: list[Job] = []
            for appliedJob in appliedJobs:
                job: Job = JobHelpers.GetJobByID(appliedJob.JobId)
                appliedJobTitles.append(job.Title)
                jobs.append(job)

            return jobs
            
        except:
            print(f"Could not get any applied job by the user: {loggedUser.Username}")

    
    # Returns a list of unapplied jobs of type list[Job].
    def GetUnappliedJobs(
        loggedUser: User,
        collectionApplied: str = "AppliedJobs",
        collectionJob : str = "Jobs") -> list[Job]:
        
        try:
            appliedJobs = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser, collectionApplied)

            if appliedJobs == None:
                raise Exception(
                    f"There are no jobs remaining to be applied by the user: {loggedUser.Username}")
            
            allJobs: list[Job] = JobHelpers.GetAllJobs(collectionJob)
            
            allJobIds: list[str] = list(map(lambda x: x.Id, allJobs))
            appliedJobIds: list[str] = list(map(lambda x: x.JobId, appliedJobs))
            unappliedJobIds: list[str] = list(set(allJobIds) - set(appliedJobIds))
            
            unappliedJobTitles: list[str] = []
            jobs: list[Job] = []
            for unappliedJobId in unappliedJobIds:
                job: Job = JobHelpers.GetJobByID(unappliedJobId)
                unappliedJobTitles.append(job.Title)
                jobs.append(job)
            
            return jobs

        except:
            print(f"There are no jobs remaining to be applied by the user: {loggedUser.Username}")


    # Return a list of saved jobs of type list[Job] and not list[SavedJob].
    def GetSavedJobs(loggedUser: User, collection: str = "SavedJobs") -> list[Job]:
        try:
            savedJobs: list[SavedJob] = SavedJobHelpers.GetAllSavedJobsOfUser(loggedUser, collection)

            if savedJobs == None:
                raise Exception(
                    f"Could not get any Saved job by the user: {loggedUser.Username}")

            savedJobTitles: list[str] = []
            jobs: list[Job] = []
            for savedJob in savedJobs:
                job: Job = JobHelpers.GetJobByID(savedJob.JobId)
                savedJobTitles.append(job.Title)
                jobs.append(job)

            return jobs

        except:
            print(f"Could not get any Saved job by the user: {loggedUser.Username}")


    # Gets a list of all the jobs that have been posted after the user last logged in.
    def GetNewJobs(loggedUser: User, collection: str = "Jobs") -> list[Job]:
        try:
            lastLogin: datetime = loggedUser._LastLoginTimestamp
            allJobs: list[Job] = JobHelpers.GetAllJobs(collection)
            if allJobs == None or allJobs == []: return []
            
            latestJobs: list[Job] = list(filter(lambda job:
                job._CreatedTimestamp > lastLogin and job.PosterId != loggedUser.Id, allJobs))
            
            if latestJobs == None or latestJobs == []: return []

            return latestJobs

        except Exception as e:
            print(f"\nException occurred while getting new jobs.\n{e}\n")
