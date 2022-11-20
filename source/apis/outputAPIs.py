# output api should be run when program starts.
# also re-run api when changes to output made
# if data conflict then trust myCollege data (firebase)
# only accept new jobs via API IF they have a diff title than jobs in firebase
# output data written to output api as it is created or changed in app
import os.path
from helpers.JobHelpers import JobHelpers
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.UserHelpers import UserHelpers
from helpers.APIHelpers import getCurrentPath, createOutputDirectory
from helpers.ProfileHelpers import ProfileHelpers
from model.Job import Job
from helpers.APIHelpers import getCurrentPath, createOutputDirectory
from model.Job import Job



def RunOutputAPIs(userCollection: str = "Users", jobsCollection: str = "Jobs",
                  appliedJobsCollection:str = "AppliedJobs", savedJobsCollection:str = "SavedJobs") -> bool:

    try: createOutputDirectory()
    except Exception as e:
        print(f"Couldn't make output directory {e}")
        return False

    try:
        if not AppliedJobsAPI(userCollection, jobsCollection, appliedJobsCollection):
            raise Exception("Applied Jobs API failed")

        if not SavedJobsAPI(userCollection, savedJobsCollection):
            raise Exception("Saved Jobs API failed")


        if not JobsAPI(jobsCollection):
            raise Exception("Jobs API failed")

        if not UserAPI(userCollection):
            raise Exception("User API failed")

        if not UserProfileAPI():
            raise Exception("User Profiles API failed")
            
        if not SavedJobsAPI(userCollection, savedJobsCollection):
            raise Exception("Saved Jobs API failed")

        if not JobsAPI(jobsCollection):
            raise Exception("Jobs API failed")

        return True

    except Exception as e:
        print(e)
        return False

def SingleJobAppendAPI(job: Job):
    try: FILE_NAME = os.path.join(getCurrentPath(), "output", "MyCollege_jobs.txt")
    except Exception as e:
        print(f"Error appending Job file name to path {e}\n")
        return False
    try:
        with open(FILE_NAME, "a") as outputFile:
            try:
                outputFile.write(f"{job.Title}\n")
                outputFile.write(f"{job.Description}\n")
                outputFile.write(f"{job.Employer}\n")
                outputFile.write(f"{job.Location}\n")
                outputFile.write(f"{job.Salary}\n")
                outputFile.write("=====\n")

            except Exception as e:
                print(f"Error writing job details to file {e}\n")
                return False

        return True

    except Exception as e:
        print(f"Error Occurred: {e}")
        return False

def JobsAPI(jobsCollection: str = "Jobs") -> bool:
    try: FILE_NAME = os.path.join(getCurrentPath(), "output", "MyCollege_jobs.txt")
    except Exception as e:
        print(f"Error appending file name to path {e}\n")
        return False

    try:
        with open(FILE_NAME, "w") as outputFile:
            allJobs = JobHelpers.GetAllJobs(jobsCollection)
            if not allJobs: allJobs = [] # if no jobs in DB
            for job in allJobs:
                try:
                    outputFile.write(f"{job.Title}\n")
                    outputFile.write(f"{job.Description}\n")
                    outputFile.write(f"{job.Employer}\n")
                    outputFile.write(f"{job.Location}\n")
                    outputFile.write(f"{job.Salary}\n")
                    outputFile.write("=====\n")

                except Exception as e:
                    print(f"Error writing saved job title to file {e}\n")
                    return False

        return True

    except Exception as e:
        print(f"Error Occurred: {e}")
        return False

def AppliedJobsAPI(userCollection: str = "Users", jobsCollection: str = "Jobs", appliedJobsCollection:str = "AppliedJobs") -> bool:

    # create file called MyCollege_appliedJobs.txt
    try: FILE_NAME = os.path.join(getCurrentPath(), "output", "MyCollege_appliedJobs.txt")
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
                    job.Id, appliedJobsCollection)
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


def SavedJobsAPI(userCollection: str = "Users", savedJobsCollection: str = "SavedJobs") -> bool:

    # create file called MyCollege_savedJobs.txt
    try: FILE_NAME = os.path.join(getCurrentPath(), "output", "MyCollege_savedJobs.txt")

    except Exception as e:
        print(f"Could not make saved jobs api file in directory {e}")
        return False
    try:
        with open(FILE_NAME, "w") as outputFile:
            allUsers = UserHelpers.GetAllUsers(collection=userCollection)
            if allUsers == None: allUsers = []

            for user in allUsers:
                savedJobs = JobHelpers.GetSavedJobs(user, collection=savedJobsCollection)
                if not savedJobs: continue # user has no saved jobs

                try: outputFile.write(f"Username: {user.Username}\n")
                except Exception as e:
                    print(f"Error writing username to file {e}\n")
                    return False

                for savedJob in savedJobs:
                    try: outputFile.write(f"{savedJob.Title}\n")
                    except Exception as e:
                        print(f"Error writing saved job title to file {e}\n")
                        return False

                try: outputFile.write("=====\n")
                except Exception as e:
                    print(f"Error writing to file {e}\n")
                    return False

        return True

    except Exception as e:
        print(f"Error Occurred: {e}")
        return False


# User API: write to file all users and their subscriptions
def UserAPI(userCollection:str = "Users") -> bool:
    # create file called MyCollege_users.txt
    try: FILE_NAME = os.path.join(getCurrentPath() , "output", "MyCollege_users.txt")
    except Exception as e:
        print(f"Error appending file name to path {e}\n")
        return False

    try:
        with open(FILE_NAME, "w") as outputFile:
            allUsers = UserHelpers.GetAllUsers(collection=userCollection)
            if allUsers == None: raise Exception("Users couldn't be retrieved")
            for user in allUsers:
                # place username of each user
                try: outputFile.write("{}, {}\n".format(user.Username, str(user.TierEnum).lstrip("UserTierEnum.")))
                except Exception as e: print(f"Could not write to file {e}\n")

        return True

    except Exception as e:
        print(f"An error occurred running the user output API! {e}\n")
        return False

# User Profiles API: write to file all users and their profiles
def UserProfileAPI(userCollection:str = "Users") -> bool:
    # create file called MyCollege_profiles.txt
    try: FILE_NAME = os.path.join(getCurrentPath() , "output", "MyCollege_profiles.txt")
    except Exception as e:
        print(f"Error appending file name to path {e}\n")
        return False

    try:
        with open(FILE_NAME, "w") as outputFile:
            allUsers = UserHelpers.GetAllUsers(collection=userCollection)
            if allUsers == None: raise Exception("Users couldn't be retrieved")
            for user in allUsers:
                # get user profile
                userProfile = user.Profile
                if userProfile == None: raise Exception("User profile couldn't be retrieved")

                if ProfileHelpers.ProfileExists(user):
                    # write user profile to file
                    try: 
                        outputFile.write(f"{userProfile.Title}\n{userProfile.Major}\n{userProfile.University}\n{userProfile.About}\n")
                        # writing experience:
                        outputFile.write("Experience:\n")
                        experience_output = ProfileHelpers.HelpPrintExperienceList(userProfile.ExperienceList).strip()
                        outputFile.write(f"{experience_output}\n")
                        # writing education:
                        outputFile.write("Education:\n")
                        education_output = ProfileHelpers.HelpPrintEducationList(userProfile.EducationList).strip()
                        outputFile.write(f"{education_output}\n")
                    except Exception as e: print(f"Could not write to file {e}\n")

                    # each user profile separated by a line of "====="
                    try:
                        outputFile.write("=====\n")
                    except Exception as e:
                        print(f"Error writing to file {e}\n")
        return True
    except Exception as e:
        print(f"An error occurred running the user profile output API! {e}\n")
        return False

def SavedJobsAPI(userCollection: str = "Users", savedJobsCollection: str = "SavedJobs") -> bool:

    # create file called MyCollege_savedJobs.txt
    try: FILE_NAME = os.path.join(getCurrentPath()+"\output", "MyCollege_savedJobs.txt")

    except Exception as e:
        print(f"Could not make saved jobs api file in directory {e}")
        return False
    try:
        with open(FILE_NAME, "w") as outputFile:
            allUsers = UserHelpers.GetAllUsers(collection=userCollection)
            if allUsers == None: allUsers = []

            for user in allUsers:
                savedJobs = JobHelpers.GetSavedJobs(user, collection=savedJobsCollection)
                if not savedJobs: continue # user has no saved jobs

                try: outputFile.write(f"Username: {user.Username}\n")
                except Exception as e:
                    print(f"Error writing username to file {e}\n")
                    return False

                for savedJob in savedJobs:
                    try: outputFile.write(f"{savedJob.Title}\n")
                    except Exception as e:
                        print(f"Error writing saved job title to file {e}\n")
                        return False

                try: outputFile.write("=====\n")
                except Exception as e:
                    print(f"Error writing to file {e}\n")
                    return False

        return True

    except Exception as e:
        print(f"An error occurred running the user profile output API! {e}\n")
        return False