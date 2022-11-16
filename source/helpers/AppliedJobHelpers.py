from datetime import datetime
from model.AppliedJob import AppliedJob
from firebaseSetup.Firebase import database
from model.User import User

class AppliedJobHelpers:

    # converts this entity into a dictionary
    def AppliedJobToDict(appliedJob: AppliedJob) -> dict:
        return {
            'UserId': str(appliedJob.UserId),
            'JobId': str(appliedJob.JobId),
            'JobTitle': str(appliedJob.JobTitle),
            'JobEmployer': str(appliedJob.JobEmployer),
            'GraduationDate': str(appliedJob.GraduationDate),
            'StartDate': str(appliedJob.StartDate),
            'GoodFitReasoning': str(appliedJob.GoodFitReasoning),
            '_CreatedTimestamp': str(appliedJob._CreatedTimestamp)
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
    def CreateAppliedJob(appliedJob: AppliedJob, loggedUser: User, collection: str = "AppliedJobs") -> bool:
        try:
            # first check if the user already applied
            allApplied: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(loggedUser=loggedUser, collection=collection)
            
            if allApplied != None:
                for applied in allApplied:
                    if applied.JobId == appliedJob.JobId:
                        print("\nError! You have already applied for this job.\n")
                        return False

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


    # deletes all applied jobs by a particular user
    def DeleteAppliedJobsOfUser(applierUser: User, collection: str = "AppliedJobs") -> bool:
        allAppliedJobs: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobs(collection=collection)
        try:
            if (allAppliedJobs != None):
                for dbAppliedJob in allAppliedJobs:
                    if dbAppliedJob.UserId == applierUser.Id:
                        database.child(collection).child(dbAppliedJob.UserId+dbAppliedJob.JobId).remove()
                return True
            
            else:
                return False
        
        except Exception as e:
            print(f"\nFailure! Could not delete the instances of applied jobs by a user for some reason.{e}\n")
            return False


    # Gets the job the user last applied to.
    def GetLastAppliedJob(loggedUser: User, collection: str = "AppliedJobs") -> AppliedJob:

        try:
            # Get all the applied jobs of the user specified.
            appliedJobs: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobsOfUser(
                loggedUser, collection
            )
            if appliedJobs == None or appliedJobs == []: return None

            # Get the created timestamps of the applied jobs and sort them.
            appliedJobDates: list[datetime] = list(map(
                lambda appliedJob: appliedJob._CreatedTimestamp, appliedJobs
            ))
            appliedJobDates.sort()

            # Access the last element of the sorted list of timestamps to get the latest.
            lastAppliedJobDate: datetime = appliedJobDates[-1]

            # Get the applied job that matches the last applied job date.
            lastAppliedJob: AppliedJob = next(filter(
                lambda appliedJob: appliedJob._CreatedTimestamp == lastAppliedJobDate, appliedJobs
            ), None)

            return lastAppliedJob

        except Exception as e:
            print(f"Could not get last applied job user due to an exception.\n{e}")
            return None

    # returns a list of AppliedJob (s) for a specific Job
    def GetApplicationsForSpecificJob(jobId: str, collection:str = "AppliedJobs") -> list[AppliedJob]:

        try:
            allJobApplications = AppliedJobHelpers.GetAllAppliedJobs(collection=collection)
            if allJobApplications == None: return []

            jobApplications = list(
                filter(lambda application: application.JobId == jobId, allJobApplications)
            )
            return jobApplications
        except Exception as e:
            print(f"An error occurred while accessing applications for job: {jobId} {e}\n")
            return None


