from dataclasses import dataclass
from firebaseSetup.Firebase import database


@dataclass
class AppliedJob:
    UserId: str
    JobId: str
    GraduationDate: str
    StartDate: str
    GoodFitReasoning: str

    # hydrates an AppliedJob entity using a pyrebase response value and returns it
    def HydrateAppliedJob(appliedJob):
        return AppliedJob(
            UserId = appliedJob.val()["UserId"],
            JobId = appliedJob.val()["JobId"],
            GraduationDate = appliedJob.val()["GraduationDate"],
            StartDate = appliedJob.val()["StartDate"],
            GoodFitReasoning = appliedJob.val()["GoodFitReasoning"]
        )