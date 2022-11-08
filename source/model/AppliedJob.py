from dataclasses import dataclass
from datetime import datetime

@dataclass
class AppliedJob:
    UserId: str
    JobId: str
    JobTitle: str
    JobEmployer: str
    GraduationDate: str
    StartDate: str
    GoodFitReasoning: str
    _CreatedTimestamp: datetime = datetime.now()


    # hydrates an AppliedJob entity using a pyrebase response value and returns it
    def HydrateAppliedJob(appliedJob):
        return AppliedJob(
            UserId = AppliedJobHydrator.HydrateProp(appliedJob, "UserId"),
            JobId = AppliedJobHydrator.HydrateProp(appliedJob, "JobId"),
            JobTitle = AppliedJobHydrator.HydrateProp(appliedJob, "JobTitle"),
            JobEmployer = AppliedJobHydrator.HydrateProp(appliedJob, "JobEmployer"),
            GraduationDate = AppliedJobHydrator.HydrateProp(appliedJob, "GraduationDate"),
            StartDate = AppliedJobHydrator.HydrateProp(appliedJob, "StartDate"),
            GoodFitReasoning = AppliedJobHydrator.HydrateProp(appliedJob, "GoodFitReasoning"),
            _CreatedTimestamp = AppliedJobHydrator.HydrateProp(appliedJob, "_CreatedTimestamp")
        )


class AppliedJobHydrator:


    # A dictionary to maintain the AppliedJob entity's property name (key) and its type (value).
    _appliedJobAttributes: dict[str, str] = {
        "UserId": "str",
        "JobId": "str",
        "JobTitle": "str",
        "JobEmployer": "str",
        "GraduationDate": "str",
        "StartDate": "str",
        "GoodFitReasoning": "str",
        "_CreatedTimestamp": "datetime"
    }


    # Hydrates an individual property for the AppliedJob entity.
    def HydrateProp(appliedJob, prop: str):
        if prop not in AppliedJobHydrator._appliedJobAttributes.keys():
            raise Exception(f"Property {prop} not defined for entity: AppliedJob")
        
        propType: str = AppliedJobHydrator._appliedJobAttributes.get(prop)
        value = None
        
        try:
            pyreValue = appliedJob.val()[prop]
            value = AppliedJobHydrator.Cast(pyreValue, propType)
        except:
            value = AppliedJobHydrator.GetDefaultValue(prop)
        
        if value == None: raise Exception(f"Could not hydrate prop: {prop} for AppliedJob")
        
        return value


    # Handles conversion to a certain type.
    def Cast(pyreValue, propType):
        if propType == "datetime":
            datetimeValue: datetime = datetime(pyreValue)
            return datetimeValue

        return pyreValue


    # Gets the default value for a property on the AppliedJob entity based on its type.
    def GetDefaultValue(prop: str):
        propType: str = AppliedJobHydrator._appliedJobAttributes.get(prop)

        if propType == "str": return ""
        if propType == "datetime": return datetime.now()
        else: return None
