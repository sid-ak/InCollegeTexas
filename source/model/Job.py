from dataclasses import dataclass

# A Job entity.
@dataclass
class Job:
    Id: str
    Title: str
    Employer: str
    Description: str
    Location: str
    Salary: str
    PosterId: str


    # Hydrates a Job entity using a pyrebase response value and returns it.
    def HydrateJob(job):
        return Job(
                Id = JobHydrator.HydrateProp(job, "Id"),
                Title = JobHydrator.HydrateProp(job, "Title"),
                Employer = JobHydrator.HydrateProp(job, "Employer"),
                Description = JobHydrator.HydrateProp(job, "Description"),
                Location = JobHydrator.HydrateProp(job, "Location"),
                Salary = JobHydrator.HydrateProp(job, "Salary"),
                PosterId = JobHydrator.HydrateProp(job, "PosterId")
            )


class JobHydrator:


    # A dictionary to maintain the Job entity's property name (key) and its type (value).
    _jobAttributes: dict[str, str] = {
        "Id": "str",
        "Title": "str",
        "Employer": "str",
        "Description": "str",
        "Location": "str",
        "Salary": "str",
        "PosterId": "str"
    }


    # Hydrates an individual property for the Job entity.
    def HydrateProp(job, prop: str):
        if prop not in JobHydrator._jobAttributes.keys():
            raise Exception(f"Property {prop} not defined for entity: Job")
        
        value = None
        
        try:
            value = job.val()[prop]
        except:
            value = JobHydrator.GetDefaultValue(prop)
        
        if value == None: raise Exception(f"Could not hydrate prop: {prop} for Job")
        
        return value


    # Gets the default value for a property on the Job entity based on its type.
    def GetDefaultValue(prop: str):
        propType: str = JobHydrator._jobAttributes.get(prop)

        if propType == "str": return ""
        else: return None
