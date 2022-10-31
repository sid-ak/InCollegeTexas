from dataclasses import dataclass
from firebaseSetup.Firebase import database


@dataclass
class AppliedJob:
    UserId: str
    JobId: str
    JobTitle: str
    JobEmployer: str
    GraduationDate: str
    StartDate: str
    GoodFitReasoning: str

    # hydrates an AppliedJob entity using a pyrebase response value and returns it
    def HydrateAppliedJob(appliedJob):
        return AppliedJob(
            UserId = appliedJob.val()["UserId"],
            JobId = appliedJob.val()["JobId"],
            JobTitle=appliedJob.val()["JobTitle"],
            JobEmployer=appliedJob.val()["JobEmployer"],
            GraduationDate = appliedJob.val()["GraduationDate"],
            StartDate = appliedJob.val()["StartDate"],
            GoodFitReasoning = appliedJob.val()["GoodFitReasoning"]
        )