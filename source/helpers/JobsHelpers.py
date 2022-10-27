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
            print(divided)
        
        except:
            return False