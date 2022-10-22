from cmath import exp
import profile
from helpers.ProfileHelpers import ProfileHelpers
from model.Profile import Profile, Education, Experience
from helpers.MenuHelpers import MenuHelpers
from firebaseSetup.Firebase import firebase
from model.User import User

# this function will check the database to see if the profile for the current user already created
def checkIfProfileAlreadyCreated(userLoggedIn: User) -> bool:
    # try:
    pass



# this function will help format an input string to uppercase
def helpFormat(input: str) -> str:
    words = input.split(" ")
    wordsFormated = []

    for word in words:
        wordsFormated.append(word.upper())

    return "".join(wordsFormated)


# this function will collect data relevant to create a profile
def createProfile(userLoggedIn: User) -> bool:
    newProfile = Profile()

    _experiencesLimit = 3

    options = ["Add a title", "Add a university", "Add major", "Add about",
        "Add education", "Add experience"]

    while True:
        try:
            print("\nPlease select one of the following: ")
            MenuHelpers.DisplayOptions(options=options)
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("\nYou have selected to add a title")
                title = input("Please enter your title: ")
                newProfile.Title = title
            elif decision == 2:
                print("\nYou have selected to add a university")
                university = helpFormat(input("Please enter your university's name: "))
                newProfile.University = university
            elif decision == 3:
                print("\nYou have selected to add a major")
                major = helpFormat(input("Please enter your major: "))
                newProfile.Major = major
            elif decision == 4:
                print("\nYpu have selected to add about section")
                about = input("Please enter about yourself: ")
                newProfile.About = about
            elif decision == 5:
                print("\nYou have selected to add education")
                try:
                    education = Education()
                    education.SchoolName = helpFormat(input("Enter the name of your school: "))
                    education.Degree = helpFormat(input("Enter your degree: "))
                    education.YearsAttended = int(input("Enter the years attended: "))
                    newProfile.EducationList.append(education)
                except:
                    print("\nError! Invalid input.")
            elif decision == 6:
                print("\nYou have selected to add experience")
                try:
                    if len(newProfile.ExperienceList) == _experiencesLimit:
                        print("\nError! You already have added 3 experiences.")
                    else: 
                        experience = Experience()
                        experience.Title = helpFormat(input("Enter title: "))
                        experience.Employer = helpFormat(input("Enter Employer: "))
                        experience.DateStarted = input("Enter date started: ")
                        experience.DateEnded = input("Enter date ended: ")
                        experience.Location = helpFormat(input("Enter location: "))
                        experience.Description = input("Enter description: ")
                        newProfile.ExperienceList.append(experience)
                except:
                    print("\nError! Invalid input")
            elif decision == -1:
                print("You have selected to quit.")
                break
        
        except:
            print("\nError! Something went wrong when trying to create a profile.")

    