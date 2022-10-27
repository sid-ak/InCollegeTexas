from model.User import User, Profile
from firebaseSetup.Firebase import database
from helpers.UserHelpers import UserHelpers


# non-return function to print the profile of a user
def ViewProfile(loggedUser: User, userToSearch: User = None):

    if not userToSearch:
        printProfile(loggedUser)
    else:
        printProfile(userToSearch)


def printProfile(user: User):
    try:
        print(f"\n{user.FirstName} {user.LastName}")
        print("Title: " + user.Profile.Title)
        print("University: " + user.Profile.University)
        print("Major: " + user.Profile.Major)
        print("About: " + user.Profile.About)

        educationList = user.Profile.EducationList
        if len(educationList) == 0:
            print("Education: No education to show!")
        else:
            try:
                EduIndex = 1
                for education in user.Profile.EducationList:
                    print(f"Education #{EduIndex}:")
                    print(f"\tSchool: {'N/A' if education.SchoolName == '' else education.SchoolName}")
                    print(f"\tDegree: {'N/A' if education.Degree == '' else education.Degree}")
                    print(f"\tYears Attended: {'0' if education.YearsAttended == 0 else education.YearsAttended}\n")
                    EduIndex += 1
            except Exception as e:
                print(f"Something went wrong while showing the education for user {user.Username}\n{e}")

        experienceList = user.Profile.ExperienceList
        if len(experienceList) == 0:
            print("Experience: No experience to show!")
        else:
            try:
                ExpIndex = 1
                for experience in experienceList:
                    print(f"\tExperience #{ExpIndex}:")
                    print(f"\tTitle: {experience.Title}")
                    print(f"\tEmployer: {experience.Employer}")
                    print(f"\tLocation: {experience.Location}")
                    print(f"\tDate Started: {experience.DateStarted}")
                    print(f"\tDate Ended: {experience.DateEnded}")
                    print(f"\tDescription: {experience.Description}\n")
                    ExpIndex += 1
            except Exception as e:
                print(f"Something went wrong while showing the experience for user {user.Username}\n{e}")
    except Exception as e:
        print(f"Something went wrong while showing the profile for user {user.Username}\n{e}")

    print()

