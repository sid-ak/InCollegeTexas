from model.User import User, Profile
from firebaseSetup.Firebase import database
from helpers.UserHelpers import UserHelpers


# this function will help with refreshing the passed User object with the updated DB User node
def HelpRefreshUser(userPassed: User) -> User:
    try:
        allUsers: list[User] = UserHelpers.GetAllUsers(collection="Users")
        for user in allUsers:
            if userPassed.Id == user.Id:
                return user
    except:
        return userPassed


# non-return function to print the profile of a user
def ViewProfile(loggedUser: User, userToSearch: User = None):
    # we can safely assume that only the username and password if the passed user objects will remain the same
    # during the program execution, while some other nodes may be updated in Firebase
    refreshedLoggedUser = HelpRefreshUser(userPassed=loggedUser)
    refreshedUserToSearch = HelpRefreshUser(userPassed=userToSearch)

    if not userToSearch:
        printProfile(refreshedLoggedUser)
    else:
        printProfile(refreshedUserToSearch)


def printProfile(user: User):
    print(f"\n{user.FirstName} {user.LastName}")
    print("Title: ", user.Profile.Title)
    print("University: ", user.Profile.University)
    print("Major: ", user.Profile.Major)
    print("About: ", user.Profile.About)
    try:
        index = 1
        for education in user.Profile.EducationList:
            print(f"Education #{index}:")
            print(f"   School: {'N/A' if education.SchoolName == '' else education.SchoolName}")
            print(f"   Degree: {'N/A' if education.Degree == '' else education.Degree}")
            print(f"   Years Attended: {'0' if education.YearsAttended == 0 else education.YearsAttended}\n")
            index += 1
    except:
        print("Education: No education to show")

    experienceList = user.Profile.ExperienceList

    try:
        index = 1
        for experience in experienceList:
            print(f"Experience #{index}:")
            print(f"   Title: {'N/A' if experience.Title == '' else experience.Title}")
            print(f"   Employer: {'N/A' if experience.Employer == '' else experience.Employer}")
            print(f"   Location: {'N/A' if experience.Location == '' else experience.Location}")
            print(f"   Date Started: {'N/A' if experience.DateStarted == '' else experience.DateStarted}")
            print(f"   Date Ended: {'N/A' if experience.DateEnded == '' else experience.DateEnded}")
            print(f"   Description: {'N/A' if experience.Description == '' else experience.Description}\n")
            index += 1
    except:
        print("Experience: No experience to show!")
    print()

