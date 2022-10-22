from model.Profile import Profile, Experience, Education
from model.User import User
from firebaseSetup.Firebase import database

class ProfileHelpers:
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