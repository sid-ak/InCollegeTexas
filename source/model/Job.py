from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User
from helpers.UserHelpers import UserHelpers

# A Job entity.
@dataclass
class Job:
    Id: str
    Title: str
    Employer: str
    Description: str
    Location: str
    Salary: str
    Poster: User

    # Hydrates a Job entity using a pyrebase response value and returns it.
    def HydrateJob(job):
        return Job(
                Id = job.val()["Id"],
                Title = job.val()["Title"],
                Employer = job.val()["Employer"],
                Description = job.val()["Description"],
                Location = job.val()["Location"],
                Salary = job.val()["Salary"],
                Poster = job.val()["Poster"]
            )
