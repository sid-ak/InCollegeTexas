from dataclasses import dataclass, field

@dataclass
class Experience:
    Title: str = ""
    Employer: str = ""
    DateStarted: str = "" # MM/DD/YY format
    DateEnded: str = "" # MM/DD/YY format
    Location: str = ""
    Description: str = ""

    def ExpToDict(self):
        return{
            'Title': str(self.Title),
            'Employer': str(self.Employer),
            'DateStarted': str(self.DateStarted),
            'DateEnded': str(self.DateEnded),
            'Location': str(self.Location),
            'Description': str(self.Description)
        }

    # converts a dictionary pyrebase response to experience object
    def HydrateExperience(ExperienceDict):
        return Experience(
            Title=ExperienceDict['Title'],
            Employer=ExperienceDict['Employer'],
            DateStarted=ExperienceDict['DateStarted'],
            DateEnded=ExperienceDict['DateEnded'],
            Location=ExperienceDict['Location'],
            Description=ExperienceDict['Description'],
        )

@dataclass
class Education:
    SchoolName: str = ""
    Degree: str = ""
    YearsAttended: int = 0

    def EducationToDict(self):
        return {
            'SchoolName': str(self.SchoolName),
            'Degree': str(self.Degree),
            'YearsAttended': int(self.YearsAttended)
        }

    # converts a dictionary pyrebase response to education object
    def HydrateEducation(EducationDict):
        return Education(
            SchoolName=EducationDict['SchoolName'],
            Degree=EducationDict['Degree'],
            YearsAttended=EducationDict['YearsAttended']
        )

"""
    Profile is of the following format
    Profile(Title='', University='', Major='', About='',
        ProfileEducation=Education(SchoolName='', Degree='', YearsAttended=0), 
        ProfileExperience=Experience(PastJobs=[]))
"""
@dataclass
class Profile:
    Id: str = "" # hashed value of all values
    Title: str = "" #e.g: Third year Comp Sci
    University: str = "" # to grab from User as default
    Major: str = ""  # to grab from User as default
    About: str = "" # paragraph
    EducationList: list[Education] = field(default_factory=list)
    ExperienceList: list[Experience] = field(default_factory=list)

    def HydrateProfile(profile: dict):
        return Profile(
            Id = ProfileHydrator.HydrateProp(profile, "Id"),
            Title = ProfileHydrator.HydrateProp(profile, "Title"),
            University = ProfileHydrator.HydrateProp(profile, "University"),
            Major = ProfileHydrator.HydrateProp(profile, "Major"),
            About = ProfileHydrator.HydrateProp(profile, "About"),
            EducationList = ProfileHydrator.HydrateProp(profile, "EducationList"),
            ExperienceList = ProfileHydrator.HydrateProp(profile, "ExperienceList"),
        )

    def ProfileToDict(self):
        try:
            if self == None:
                self = Profile()
            
            if (self.EducationList == None):
                self.EducationList = [Education()]
            
            if (self.ExperienceList == None):
                self.ExperienceList = [Experience()]

            return {
                'Id': str(self.Id),
                'Title': str(self.Title),
                'University': str(self.University),
                'Major': str(self.Major),
                'About': str(self.About),
                'EducationList': {i: self.EducationList[i].EducationToDict() for i in range(len(self.EducationList))},
                'ExperienceList': {i: self.ExperienceList[i].ExpToDict() for i in range(len(self.ExperienceList))}
            }
        except Exception as e:
            print(f"Could not convert a Profile entity to a dictionary object.\n{e}")

class ProfileHydrator:

    # A dictionary to maintain the Profile entity's property name (key) and its type (value).
    _profileAttributes: dict[str, str] = {
        "Id": "str",
        "Title": "str",
        "University": "str",
        "Major": "str",
        "About": "bool",
        "EducationList": "list[Education]",
        "ExperienceList": "list[Experience]"
    }

    # Hydrates an individual property for the Profile entity.
    def HydrateProp(profile: dict, prop: str):
        if prop not in ProfileHydrator._profileAttributes.keys():
            raise Exception(f"Property {prop} not defined for entity: Profile")
        
        propType: str = ProfileHydrator._profileAttributes.get(prop)
        value = None
        
        try:
            pyreValue = profile[prop]
            value = ProfileHydrator.CastComplexType(pyreValue, propType)
        except:
            value = ProfileHydrator.GetDefaultValue(prop)
        
        if value == None: raise Exception(f"Could not hydrate prop: {prop} for Profile")
        
        return value
    
    # Handles conversion to a complex type.
    def CastComplexType(pyreValue, propType):
        if propType == "list[Education]":
            educationList: list[Education] = []
            for education in pyreValue:
                educationList.append(Education.HydrateEducation(education))
            return educationList
        
        if propType == "list[Experience]":
            educationList: list[Experience] = []
            for experience in pyreValue:
                educationList.append(Experience.HydrateExperience(experience))
            return educationList
        
        return pyreValue
    
    # Gets the default value for a property on the Profile entity based on its type.
    def GetDefaultValue(prop: str):
        propType: str = ProfileHydrator._profileAttributes.get(prop)

        if propType == "str": return ""
        elif propType == "bool": return True
        elif propType == "list[Education]": return [Education()],
        elif propType == "list[Experience]": return [Experience()]
        else: return None

    def HydrateProfile(profile):
        profileReturn: Profile = Profile(
            Id = profile["Id"],
            Title = profile["Title"],
            University = profile["University"],
            Major = profile["Major"],
            About = profile["About"],
        )
        
        # need to fetch EducationList and ExperienceList seperately since Firebase does not store empty lists
        try:
            profileReturn.EducationList = profile["EducationList"]
        except:
            profileReturn.EducationList = []
        try:
            profileReturn.ExperienceList = profile["ExperienceList"]
        except:
            profileReturn.ExperienceList = []


        return profileReturn   
