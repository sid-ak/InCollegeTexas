from cmath import exp
import profile
from helpers.ProfileHelpers import ProfileHelpers
from model.Profile import Profile, Education, Experience
from helpers.MenuHelpers import MenuHelpers
from firebaseSetup.Firebase import database
from model.User import User
from helpers.UserHelpers import UserHelpers
from helpers.ProfileHelpers import ProfileHelpers


# this function will help format an input string to title of each word
def HelpFormat(input: str) -> str:
    words = input.split(" ")
    wordsFormated = []

    for word in words:
        wordsFormated.append(word.title())

    return " ".join(wordsFormated)


# this function will collect data relevant to create a profile
def UpdateProfile(userLoggedIn: User) -> bool:
    profile: Profile = None
    profileAlreadyCreated = False

    # if the user already has a profile, we fetch the exisitng one and update if necessary
    try:
        users = UserHelpers.GetAllUsers()
        for user in users:
            if user.Id == userLoggedIn.Id:
                # if the user does not have a Profile node with the Id child node, 
                # the user hasn't created a profile yet
                try:
                    if (user.Profile['Id'] == ""):
                        pass
                    else:
                        profile = Profile.HydrateProfile(user.Profile)
                        profileAlreadyCreated = True
                except:
                    pass
    
    except:
        print("\nError! Something went wrong when trying to access the database.")
        return False

    if profileAlreadyCreated == False:
        # if the user doesn't have a profile, we initialie an empty profile object
        profile = Profile()

    _experiencesLimit = 3

    while True:
        try:
            print("\nPlease select one of the following fields to be updated: ")
            options = ["Title: " + str(profile.Title), "University: " + str(profile.University), 
                "Major: " + str(profile.Major), "About: " + str(profile.About), "Education: " + 
                str(profile.EducationList if len(profile.EducationList) != 0 else ""), "Experience: " + str(profile.ExperienceList if len(profile.ExperienceList) != 0 else "")]

            MenuHelpers.DisplayOptions(options=options)
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("\nYou have selected to update a title")
                title = input("Please enter your title: ")
                profile.Title = title
            elif decision == 2:
                print("\nYou have selected to update a university")
                university = HelpFormat(input("Please enter your university's name: "))
                profile.University = university
            elif decision == 3:
                print("\nYou have selected to update a major")
                major = HelpFormat(input("Please enter your major: "))
                profile.Major = major
            elif decision == 4:
                print("\nYou have selected to update about section")
                about = input("Please enter about yourself: ")
                profile.About = about
            elif decision == 5:
                print("\nYou have selected to add education")
                try:
                    education = Education()
                    education.SchoolName = HelpFormat(input("Enter the name of your school: "))
                    education.Degree = HelpFormat(input("Enter your degree: "))
                    education.YearsAttended = int(input("Enter the years attended: "))
                    profile.EducationList.append(education)
                except:
                    print("\nError! Invalid input.")
            elif decision == 6:
                print("\nYou have selected to add experience")
                try:
                    if len(profile.ExperienceList) == _experiencesLimit:
                        print("\nError! You already have added 3 experiences.")
                    else: 
                        experience = Experience()
                        experience.Title = HelpFormat(input("Enter title: "))
                        experience.Employer = HelpFormat(input("Enter Employer: "))
                        experience.DateStarted = input("Enter date started: ")
                        experience.DateEnded = input("Enter date ended: ")
                        experience.Location = HelpFormat(input("Enter location: "))
                        experience.Description = input("Enter description: ")
                        profile.ExperienceList.append(experience)
                except:
                    print("\nError! Invalid input")
            elif decision == -1:
                print("You have selected to quit.")
                break
        
        except:
            print("\nError! Something went wrong when trying to create a profile.")

    while True:
        try:
            print("\nSelect if you would like to save the changes to your profile: ")
            MenuHelpers.DisplayOptions(["Yes", "No"])
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                # now we try to update profile of the user
                if ProfileHelpers.UpdateProfile(username=userLoggedIn.Username, profile=profile):
                    print("\nSuccess! You have updated your profile.\n")
                    return True
                else:
                    print("\nFailure! We haven't been able to update your profile at this time.\n")
                    return False
            elif decision == 2:
                print("\nYour changes are successfully ignored.\n")
                return True
            elif decision == -1:
                print("\nYour changes are successfully ignored.\n")
                return True
            else:
                print("\nError! Invalid input.")
        
        except:
            print("\nError! Invalid input.")


    