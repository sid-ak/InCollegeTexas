from dataclasses import dataclass
from firebaseSetup.Firebase import database
import hashlib

# the primary id of the entity in Firebase will be id of
#  the user that wants to save the job
@dataclass
class SavedJob:
    Id: str
    JobId: str
    UserId: str

    # hydrates a SavedJob entity using a pyrebase response value and returns it
    def HydrateSavedJob(savedJob):
        return SavedJob(
            Id=savedJob.val()["Id"],
            JobId=savedJob.val()["JobId"],
            UserId=savedJob.val()["UserId"]
        )
    

class SavedJobHelpers:

    # converts the entity into a dictionary
    def SavedJobToDict(savedJob: SavedJob) -> dict:
        return {
            'Id': str(savedJob.Id),
            'JobId': str(savedJob.JobId),
            'UserId': str(savedJob.UserId)
        }

    # queries all saved job nodes from the DB
    def GetAllSavedJobs(collection: str = "SavedJobs") -> list[SavedJob]:
        try:
            savedJobsResponse = database.child(collection).get()

            if savedJobsResponse == None: return None

            savedJobsResponseList: list = savedJobsResponse.each()
            if (savedJobsResponseList == None): return None

            savedJobs: list[SavedJob] = []
            for saved in savedJobsResponse.each():
                if saved == None: continue
                else: savedJobs.append(SavedJob.HydrateSavedJob(saved))
            
            return savedJobs
        
        except:
            return None

    
    # creates the specified saved job in the DB
    def CreateSavedJob(savedJob: SavedJob, collection: str = "SavedJobs") -> bool:
        try:
            # primary key of node is user id
            database.child(collection).child(savedJob.Id).set(
                SavedJobHelpers.SavedJobToDict(savedJob))
            return True
        except:
            return False


    # creates a sha256 hash using all saved job details
    def CreateSaveJobId(
        jobId: str,
        userId: str,) -> str:
        return hashlib.sha256(
            str.encode(jobId.join(userId))).hexdigest()