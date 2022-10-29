from model.Job import Job
from model.User import User
from model.AppliedJob import AppliedJob
from model.SavedJob import SavedJob
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.SavedJobHelpers import SavedJobHelpers


class JobsHelpers:

    # helps find if the user did not post the job provided
    def HelpFindUserPosted(loggedUser: User, jobInterested: Job) -> bool:
        return loggedUser.Id == jobInterested.Poster["Id"]


    # helps find if the user already applied for the job provided
    def HelpFindIfApplied(loggedUser: User, jobInterested: Job) -> bool:
        allApplied: list[AppliedJob] = AppliedJobHelpers.GetAllAppliedJobs()

        for applied in allApplied:
            # the combination of user id and job id is equal to id of applied - means it is not unique
            if (loggedUser.Id + jobInterested.Id) == (applied.UserId + applied.JobId):
                return True
            
        return False

    
    # helps find if the user already saved the job provided
    def HelpFindIfSaved(loggedUser: User, jobInterested: Job) -> bool:
        allSaved: list[SavedJob] = SavedJobHelpers.GetAllSavedJobs()

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