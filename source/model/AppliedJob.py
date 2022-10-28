from dataclasses import dataclass
from firebaseSetup.Firebase import database


@dataclass
class AppliedJob:
    UserId: str
    JobId: str
    GraduationDate: str
    StartDate: str
    GoodFitReasoning: str

    # hydrates an AppliedJob entity using a pyrebase response value and returns it
    def HydrateAppliedJob(appliedJob):
        return AppliedJob(
            UserId = appliedJob.val()["UserId"],
            JobId = appliedJob.val()["JobId"],
            GraduationDate = appliedJob.val()["GraduationDate"],
            StartDate = appliedJob.val()["StartDate"],
            GoodFitReasoning = appliedJob.val()["GoodFitReasoning"]
        )
    

class AppliedJobHelpers:

    # converts this entity into a dictionary
    def AppliedJobToDict(appliedJob: AppliedJob) -> dict:
        return {
            'UserId': str(appliedJob.UserId),
            'JobId': str(appliedJob.JobId),
            'GraduationDate': str(appliedJob.GraduationDate),
            'StartDate': str(appliedJob.StartDate),
            'GoodFitReasoning': str(appliedJob.GoodFitReasoning)
        }
    
    # queries all applid jobs nodes from the DB
    def GetAllAppliedJobs(collection: str = "AppliedJobs") -> list[AppliedJob]:
        try:
            appliedJobsResponse = database.child(collection).get()

            if appliedJobsResponse == None: return None

            appliedJobsResponseList: list = appliedJobsResponse.each()
            if (appliedJobsResponseList == None): return None

            appliedJobs: list[AppliedJob] = []
            for appliedJob in appliedJobsResponse.each():
                if appliedJob == None: continue
                else: appliedJobs.append(AppliedJob.HydrateAppliedJob(appliedJob))
            
            return appliedJobs

        except:
            return None


    # creates the specifid applied job in the DB
    def CreateAppliedJob(appliedJob: AppliedJob, collection: str = "AppliedJobs") -> bool:
        try:
            # the id of the applied job entry is the combination of user id and job id
            database.child(collection).child(appliedJob.UserId + appliedJob.JobId).set(
                AppliedJobHelpers.AppliedJobToDict(appliedJob))
            return True
        except:
            return False
    

    # deletes the specified applied job from the DB
    def DeleteAppliedJob(appliedJob: AppliedJob, collection: str = "AppliedJobs") -> bool:
        allAppliedJobs = AppliedJobHelpers.GetAllAppliedJobs(collection=collection)

        if (allAppliedJobs != None):
            for dbAppliedJob in allAppliedJobs:
                if appliedJob.JobId == dbAppliedJob.JobId and appliedJob.UserId == dbAppliedJob.UserId:
                    database.child(collection).child(appliedJob.UserId+appliedJob.JobId).remove()
                    return True
                
        else:
            return False
