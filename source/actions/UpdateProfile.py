from cmath import exp
from operator import index
from model.Profile import Profile, Education, Experience
from helpers.MenuHelpers import MenuHelpers
from firebaseSetup.Firebase import database
from model.User import User
from helpers.UserHelpers import UserHelpers
from helpers.ProfileHelpers import ProfileHelpers


# returns the formatted string with the displays of education
def HelpPrintEducationList(profile: Profile) -> str:
    if len(profile.EducationList) != 0:
        output: str = "\n"
        indexer: int = 1
        for i in range(len(profile.EducationList)):
            item = Education.EducationToDict(profile.EducationList[i])
            output += f"\n{indexer}) \nSchool Name: {item['SchoolName']}\nDegree: {item['Degree']}\nYears Attended: {item['YearsAttended']}\n"
            indexer += 1
        return output
    else:
        return ""


# returns the formatted string with the displays of experience
def HelpPrintExperienceList(profile: Profile) -> str:
    if len(profile.ExperienceList) != 0:
        output: str = "\n"
        indexer: int = 1
        for i in range(len(profile.ExperienceList)):
            item = Experience.ExpToDict(profile.ExperienceList[i])
            output += f"\n{indexer}) \nTitle: {item['Title']}\nEmployer: {item['Employer']}\nDate Started: {item['DateStarted']}\nDate Ended: {item['DateEnded']}\nLocation: {item['Location']}\nDescription: {item['Description']}\n"
            indexer += 1
        return output
    else:
        return ""

def ProfileExists(user: User) -> bool:
    try:
        if (user.Profile != None and user.Profile != Profile()):
            return True
        else:
            return False
    except:
        return False


# this function will help format an input string to title of each word
def ToTitleFormat(input: str) -> str:
    words = input.split(" ")
    wordsFormated = []

    for word in words:
        wordsFormated.append(word.title())

    return " ".join(wordsFormated)


# this function will push the changes to the profile to db if the user decides
def ConfirmChanges(loggedUser: User, profile: Profile) -> bool:
    while True:
        try:
            print("\nSelect if you would like to save the changes to your profile: ")
            MenuHelpers.DisplayOptions(["Yes", "No"])
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                # now we try to update profile of the user
                loggedUser.Profile = profile
                if UserHelpers.UpdateUser(loggedUser):
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


# this function will collect data relevant to create a profile
def EditProfile(userLoggedIn: User) -> bool:
    profile: Profile = None

    # if the user already has a profile, we fetch the exisitng one and update if necessary
    if ProfileExists(userLoggedIn):
        profile = userLoggedIn.Profile
    else:
        profile = Profile()

    while True:
        try:
            print("\nPlease select one of the following fields to be updated: ")
            options = ["Title: " + str(profile.Title),
                        "University: " + str(profile.University), 
                        "Major: " + str(profile.Major), 
                        "About: " + str(profile.About), 
                        "Education (Can add more than 1): " + HelpPrintEducationList(profile=profile), 
                        "Experience (Can add up to 3): " + HelpPrintExperienceList(profile=profile)]

            MenuHelpers.DisplayOptions(options=options)
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("\nYou have selected to update a title")
                title = input("Please enter your title: ")
                profile.Title = title
            elif decision == 2:
                print("\nYou have selected to update a university")
                university = ToTitleFormat(input("Please enter your university's name: "))
                profile.University = university
            elif decision == 3:
                print("\nYou have selected to update a major")
                major = ToTitleFormat(input("Please enter your major: "))
                profile.Major = major
            elif decision == 4:
                print("\nYou have selected to update about section")
                about = input("Please enter about yourself: ")
                profile.About = about
            elif decision == 5:
                print("\nYou have selected to add education")
                try:
                    education = Education()
                    education.SchoolName = ToTitleFormat(input("Enter the name of your school: "))
                    education.Degree = ToTitleFormat(input("Enter your degree: "))
                    education.YearsAttended = int(input("Enter the years attended: "))
                    profile.EducationList.append(education)
                except:
                    print("\nError! Invalid input.")
            elif decision == 6:
                print("\nYou have selected to add experience")
                try:
                    if ProfileHelpers.IsProfileExpLimitMet(user=userLoggedIn):
                        print("\nError! You already have added 3 experiences.")
                    else: 
                        experience = Experience()
                        experience.Title = ToTitleFormat(input("Enter title: "))
                        experience.Employer = ToTitleFormat(input("Enter Employer: "))
                        experience.DateStarted = input("Enter date started: ")
                        experience.DateEnded = input("Enter date ended: ")
                        experience.Location = ToTitleFormat(input("Enter location: "))
                        experience.Description = input("Enter description: ")
                        profile.ExperienceList.append(experience)
                except:
                    print("\nError! Invalid input")
            elif decision == -1:
                print("You have selected to quit.")
                break
        
        except:
            print("\nError! Something went wrong when trying to create a profile.")


    return ConfirmChanges(loggedUser=userLoggedIn, profile=profile)
    