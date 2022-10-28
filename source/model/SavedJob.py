from dataclasses import dataclass
from firebaseSetup.Firebase import database


# the primary id of the entity in Firebase will be id of
#  the user that wants to save the job
@dataclass
class SavedJob:
    JobId: str
    UserId: str

    # hydrates a SavedJob entity using a pyrebase response value and returns it
    def HydrateSavedJob(savedJob):
        return SavedJob(
            JobId=savedJob.val()["JobId"],
            UserId=savedJob.val()["UserId"]
        )
    

class SavedJobHelpers:

    # converts the entity into a dictionary
    def SavedJobToDict(savedJob: SavedJob) -> dict:
        return {
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
            database.child(collection).child(savedJob.UserId).set(
                SavedJobHelpers.SavedJobToDict(savedJob))
            return True
        except:
            return False
