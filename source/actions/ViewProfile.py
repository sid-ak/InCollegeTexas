from helpers.UserHelpers import UserHelpers
from model.User import User
from model.Profile import Education, Experience


# non-return function to print the profile of a user
def ViewProfile(loggedUser: User, userToSearch: User = None):

    if userToSearch == None:
        PrintProfile(loggedUser)
    else:
        PrintProfile(userToSearch)


# Prints a profile.
def PrintProfile(user: User):
    try:

        # Get user from DB so saved changes are reflected.
        user = UserHelpers.GetUserById(user.Id)

        print(f"\n========== {user.FirstName} {user.LastName} ==========\n")

        # Print Profile Details.
        print(f"\nPrimary Details:"
            + f"\n\tTitle: {user.Profile.Title}"
            + f"\n\tUniversity: {user.Profile.University}"
            + f"\n\tMajor: {user.Profile.Major}"
            + f"\n\tAbout: {user.Profile.About}\n")

        print(f"\n========== {user.FirstName}'s EDUCATION ==========\n")

        # Print Education List.
        PrintEducationList(user.Profile.EducationList)

        print(f"\n========== {user.FirstName}'s EXPERIENCE ==========\n")
        
        # Print Experience List.
        PrintExperienceList(user.Profile.ExperienceList)

        print("\n========================================\n")
    
    except Exception as e:
        print(f"Something went wrong while showing the profile for user {user.Username}\n{e}\n")


# Prints the list of educations under the profile of a user.
def PrintEducationList(educationList: list[Education]):
    if educationList == None or educationList == []:
        print("Education: No education to show.")
    else:
        try:
            eduIndex = 1
            for education in educationList:
                print(f"Education #{eduIndex}:"
                    + f"\n\tSchool: {education.SchoolName}"
                    + f"\n\tDegree: {education.Degree}"
                    + f"\n\tYears Attended: {education.YearsAttended}\n")
                eduIndex += 1
        except Exception as e:
            raise Exception(f"Something went wrong while showing education.\n{e}\n")


# Prints the list of experiences under the profile of a user.
def PrintExperienceList(experienceList: list[Experience]):
    if experienceList == None or experienceList == []:
        print("Experience: No experience to show.")
    else:
        try:
            expIndex = 1
            for experience in experienceList:
                print(f"Experience #{expIndex}:"
                    + f"\n\tTitle: {experience.Title}"
                    + f"\n\tEmployer: {experience.Employer}"
                    + f"\n\tLocation: {experience.Location}"
                    + f"\n\tDate Started: {experience.DateStarted}"
                    + f"\n\tDescription: {experience.Description}\n")
                expIndex += 1
        except Exception as e:
            raise Exception(f"Something went wrong while showing experience.\n{e}\n")
