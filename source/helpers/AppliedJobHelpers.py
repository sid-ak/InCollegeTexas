from model.AppliedJob import AppliedJob
from firebaseSetup.Firebase import database
from model.User import User


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

        except Exception as e:
            print(f"\nFailure! Could not fetch all applied jobs for some reason.{e}\n")
            return None


    # queries all applied jobs nodes for a specified user from the DB
    def GetAllAppliedJobsOfUser(loggedUser: User, collection: str = "AppliedJobs") -> list[AppliedJob]:
        try:
            allAppliedJobs = AppliedJobHelpers.GetAllAppliedJobs(collection=collection)
            if allAppliedJobs == None or allAppliedJobs == []: return None

            appliedJobsUser: list[AppliedJob] = []
            for applied in allAppliedJobs:
                if applied.UserId == loggedUser.Id:
                    appliedJobsUser.append(applied)
            
            return appliedJobsUser
        except Exception as e:
            print(f"\nFailure! Could not fetch all applied jobs for the user for some reason.{e}\n")
            return None


    # creates the specifid applied job in the DB
    def CreateAppliedJob(appliedJob: AppliedJob, collection: str = "AppliedJobs") -> bool:
        try:
            # the id of the applied job entry is the combination of user id and job id
            database.child(collection).child(appliedJob.UserId + appliedJob.JobId).set(
                AppliedJobHelpers.AppliedJobToDict(appliedJob))
            return True
        except Exception as e:
            print(f"\nFailure! Could not create an instance of applied job for some reason.{e}\n")
            return False
    

    # deletes the specified applied job from the DB
    def DeleteAppliedJob(appliedJob: AppliedJob, collection: str = "AppliedJobs") -> bool:
        allAppliedJobs = AppliedJobHelpers.GetAllAppliedJobs(collection=collection)

        try:
            if (allAppliedJobs != None):
                for dbAppliedJob in allAppliedJobs:
                    if appliedJob.JobId == dbAppliedJob.JobId and appliedJob.UserId == dbAppliedJob.UserId:
                        database.child(collection).child(appliedJob.UserId+appliedJob.JobId).remove()
                        return True
                    
            else:
                return False
        
        except Exception as e:
            print(f"\nFailure! Could not delete the instance of applied job for some reason.{e}\n")
            return False