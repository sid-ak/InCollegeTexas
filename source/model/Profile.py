from dataclasses import dataclass, field
from firebaseSetup.Firebase import database

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

    # converts a dictionary pyrebase response to edxperience object
    def PyreToExperience(ExperienceDict):
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
    def PyreToEducation(EducationDict):
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

    def ProfileToDict(self):
        return {
            'Id': str(self.Id),
            'Title': str(self.Title),
            'University': str(self.University),
            'Major': str(self.Major),
            'About': str(self.About),
            'EducationList': {i: self.EducationList[i].EducationToDict() for i in range(len(self.EducationList))},
            'ExperienceList': {i: self.ExperienceList[i].ExpToDict() for i in range(len(self.ExperienceList))}
        }
