from model.Job import Job
from model.User import User

class JobsHelpers:

    # helps find  if the user did not post the job provided
    def HelpFindUserPosted(loggedUser: User, jobInterested: Job) -> bool:
        return loggedUser.Id == jobInterested.Poster.Id