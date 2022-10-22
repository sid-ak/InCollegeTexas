from dataclasses import dataclass, field
from model.User import User
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

    # Builds user profile object from pyrebase response
    def GetUserProfile(user: User):
        usersResponse = database.child("Users").child(user.Id).get()
        UserProfileResponse = usersResponse.val()['Profile']
        try:
            EducationListResponse = UserProfileResponse['EducationList']
        except:
            EducationListResponse = []

        try:
            ExperienceListResponse = UserProfileResponse['ExperienceList']
        except:
            ExperienceListResponse = []

        # build list of Experience class objects
        ExperienceList = []
        for exp in ExperienceListResponse:
            e = Experience.PyreToExperience(exp)
            ExperienceList.append(e)

        # build list of Education class objects
        EducationList = []
        for edu in EducationListResponse:
            ed = Education.PyreToEducation(edu)
            EducationList.append(ed)

        # returns empty list if no education or experience added
        # returns empty string for the rest
        return Profile(
            Id=UserProfileResponse['Id'],
            Title=UserProfileResponse['Title'],
            University=UserProfileResponse['University'],
            Major=UserProfileResponse['Major'],
            About=UserProfileResponse['About'],
            EducationList=EducationList,
            ExperienceList=ExperienceList
        )

class ProfileHelpers:
    def UpdateProfile(username: str, profile: Profile) -> bool:
        usersResponse = database.child("Users").get()
        for u in usersResponse.each():
            if u.val()['Username'] == username:
                user = User.HydrateUser(u)
                profile.Id = user.Id
                try:
                    database.child("Users").child(user.Id).child("Profile").set(profile.ProfileToDict())
                    return True
                except:
                    print('\nCould not update profile!\n')
                    return False


