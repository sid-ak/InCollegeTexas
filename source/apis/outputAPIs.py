# output api should be run when program starts.
# also re-run api when changes to output made
# if data conflict then trust myCollege data (firebase)
# only accept new jobs via API IF they have a diff title than jobs in firebase
# output data written to output api as it is created or changed in app
import os.path
from helpers.JobHelpers import JobHelpers
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.UserHelpers import UserHelpers
from helpers.APIHelpers import getCurrentPath

def RunOutputAPIs():
    AppliedJobsAPI()

def AppliedJobsAPI(userCollection: str = "Users", jobsCollection: str = "Jobs", appliedJobsCollection:str = "AppliedJobs"):

    # create file called MyCollege_appliedJobs.txt
    FILE_NAME = os.path.join(getCurrentPath(), "MyCollege_appliedJobs.txt")

    try:
        with open(FILE_NAME, "w") as outputFile:
            allJobs = JobHelpers.GetAllJobs(collection=jobsCollection)
            for job in allJobs:
                # place title of each job posting
                outputFile.write(f"{job.Title}\n")

                # gets all job applications of a specific JobId/job posting from allJobApplciations
                jobApplications = AppliedJobHelpers.GetApplicationsForSpecificJob(
                    job, appliedJobsCollection)

                # for each job, get and write users and reason for good fit
                for application in jobApplications:
                    username = UserHelpers.GetUserById(application.UserId, collection=userCollection).Username
                    outputFile.write(f"{username}, {application.GoodFitReasoning}\n")

                # each job posting separated by a line of "====="
                outputFile.write("=====\n")

        return True

    except Exception as e:
        print(f"An error occurred running the applied jobs output API! {e}\n")
        return False

