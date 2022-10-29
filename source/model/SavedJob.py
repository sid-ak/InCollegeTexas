from dataclasses import dataclass
from firebaseSetup.Firebase import database
import hashlib

# the primary id of the entity in Firebase will be id of
#  the user that wants to save the job
@dataclass
class SavedJob:
    Id: str
    JobId: str
    UserId: str

    # hydrates a SavedJob entity using a pyrebase response value and returns it
    def HydrateSavedJob(savedJob):
        return SavedJob(
            Id=savedJob.val()["Id"],
            JobId=savedJob.val()["JobId"],
            UserId=savedJob.val()["UserId"]
        )
    