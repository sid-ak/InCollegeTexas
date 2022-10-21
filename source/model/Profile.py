from dataclasses import dataclass, field
from model.User import User, UserHelpers

@dataclass
class Experience:
    ExperienceTitle: str = ""
    Employer: str = ""
    DateStarted: str = "" # MM/DD/YY format
    DateEnded: str = "" # MM/DD/YY format
    Location: str = ""
    Description: str = ""

    def ExpToDict(self):
        return{
            'Title': str(self.ExperienceTitle),
            'Employer': str(self.Employer),
            'DateStarted': str(self.DateStarted),
            'DateEnded': str(self.DateEnded),
            'Location': str(self.Location),
            'Description': str(self.Description)
        }

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

"""
    Profile is of the following format
    Profile(Title='', University='', Major='', About='',
        ProfileEducation=Education(SchoolName='', Degree='', YearsAttended=0), 
        ProfileExperience=Experience(PastJobs=[]))
"""
@dataclass
class Profile:
    Id: str = User.Id # hashed value of all values
    Title: str = "" #e.g: Third year Comp Sci
    University: str = User.University # to grab from User as default
    Major: str = User.Major  # to grab from User as default
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

