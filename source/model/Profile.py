from dataclasses import dataclass, field
import hashlib

@dataclass
class JobExperience:
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
            'YearsAttended': str(self.YearsAttended)
        }

@dataclass
class Profile:
    ProfileID: str = "" # hashed value of all values
    Title: str = "" #e.g: Third year Comp Sci
    University: str = "" # to grab from User as default
    Major: str = ""  # to grab from User as default
    About: str = "" # paragraph
    ProfileEducation: Education = Education()
    ProfileExperience: list[JobExperience] = field(default_factory=list)

    def ProfileToDict(self):
        return {
            'ProfileID': str(self.ProfileID),
            'Title': str(self.Title),
            'University': str(self.University),
            'Major': str(self.Major),
            'About': str(self.About),
            'Education': self.ProfileEducation.EducationToDict(),
            'Experience': {i: self.ProfileExperience[i].ExpToDict() for i in range(len(self.ProfileExperience))}
        }

#Profile is of the following format
# Profile(Title='', University='', Major='', About='',
# ProfileEducation=Education(SchoolName='', Degree='', YearsAttended=0), ProfileExperience=Experience(PastJobs=[]))
