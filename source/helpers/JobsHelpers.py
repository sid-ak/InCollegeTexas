from enum import Flag
from model.Job import Job
from model.User import User

class JobsHelpers:

    # helps find if the user did not post the job provided
    def HelpFindUserPosted(loggedUser: User, jobInterested: Job) -> bool:
        return loggedUser.Id == jobInterested.Poster.Id

    
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