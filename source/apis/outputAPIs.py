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

def RunOutputAPIs(userCollection: str = "Users", jobsCollection: str = "Jobs", appliedJobsCollection:str = "AppliedJobs") -> False:
    try:
        if not AppliedJobsAPI(userCollection, jobsCollection, appliedJobsCollection):
            raise Exception("Applied Jobs API failed")

        return True
    except Exception as e:
        print(e)


def AppliedJobsAPI(userCollection: str = "Users", jobsCollection: str = "Jobs", appliedJobsCollection:str = "AppliedJobs") -> bool:

    # create file called MyCollege_appliedJobs.txt
    try: FILE_NAME = os.path.join(getCurrentPath(), "MyCollege_appliedJobs.txt")
    except Exception as e:
        print(f"Error appending file name to path {e}\n")
        return False

    try:
        with open(FILE_NAME, "w") as outputFile:
            allJobs = JobHelpers.GetAllJobs(collection=jobsCollection)
            if allJobs == None: raise Exception("All jobs couldn't be retrieved")
            for job in allJobs:
                # place title of each job posting
                try: outputFile.write(f"{job.Title}\n")
                except Exception as e: print(f"Could not write job title to file {e}\n")

                # gets all job applications of a specific JobId/job posting from allJobApplciations
                jobApplications = AppliedJobHelpers.GetApplicationsForSpecificJob(
                    job, appliedJobsCollection)
                if jobApplications == None: raise Exception("Getting applications for job error")

                # for each job, get and write users and reason for good fit
                for application in jobApplications:
                    user = UserHelpers.GetUserById(application.UserId, collection=userCollection)
                    # check if user exists
                    if not UserHelpers.UserExists(user.Id):
                        continue
                    try:
                        outputFile.write(f"{user.Username}, {application.GoodFitReasoning}\n")
                    except Exception as e:
                        print(f"Could not write username and reason to file {e}\n")

                # each job posting separated by a line of "====="
                try:
                    outputFile.write("=====\n")
                except Exception as e:
                    print(f"Error writing to file {e}\n")

        return True

    except Exception as e:
        print(f"An error occurred running the applied jobs output API! {e}\n")
        return False

