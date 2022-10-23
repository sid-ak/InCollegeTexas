from cmath import exp
from tkinter import Menu
from model.Profile import Profile, Education, Experience
from helpers.MenuHelpers import MenuHelpers
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


# this function will help with the edition of each individual attribute of education
def helpEditEducationAttributes(education: Education) -> Education:
    
    while True:
        try:
            print("\nSelect one of the following parts of education to edit: ")
            options = ["Name of School: " + str(education.SchoolName),
                        "Degree: " + str(education.Degree),
                        "Years Attended: " + str(education.YearsAttended)]

            MenuHelpers.DisplayOptions(options=options)
            decision: int = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("You have selected to edit Name of School")
                education.SchoolName = ToTitleFormat(input("Enter the new name of the school: "))
                print("Successfully updated the school name.\n")
            
            elif decision == 2:
                print("You have selected to edit Degree")
                education.Degree = ToTitleFormat(input("Enter the new degree: "))
                print("Successfully updated degree.\n")
            
            elif decision == 3:
                print("You have selected to edit Years Attended")
                education.YearsAttended = ToTitleFormat(input("Enter the new years attended: "))
                print("Successfully updated the years attended")
            
            elif decision == -1:
                print("You have selected to quit edition of education")
                return education

            else:
                print("\nError! Could not edit due to invalid input on attribute index.")
        
        except:
            print("\nError! Could not edit due to invalid input on attribute index.")


# this function will help with the edition of each individual attribute of experience
def helpEditExperienceAttributes(experience: Experience) -> Experience:
    
    while True:
        try:
            print("\nSelect one of the following parts of experience to edit: ")
            options = ["Title: " + str(experience.Title),
                        "Employer: " + str(experience.Employer),
                        "Date Started: " + str(experience.DateStarted),
                        "Date Ended: " + str(experience.DateEnded),
                        "Location: " + str(experience.Location),
                        "Description: " + str(experience.Description)]

            MenuHelpers.DisplayOptions(options=options)
            decision: int = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("You have selected to edit Title")
                experience.Title = ToTitleFormat(input("Enter new title: "))
                print("Successfully updated title")
            
            elif decision == 2:
                print("You have selected to edit Employer")
                experience.Employer = ToTitleFormat(input("Enter the new employer: "))
                print("Successfully updated employer")
            
            elif decision == 3:
                print("You have selected to edit Date Started")
                experience.DateStarted = input("Enter the new date started: ")
                print("Successfully updated date started")

            elif decision == 4:
                print("You have selected to edit Date Ended")
                experience.DateEnded = input("Enter the new date ended: ")
                print("Successfully updated date ended")

            elif decision == 5:
                print("You have selected to edit Location")
                experience.Location = ToTitleFormat(input("Enter the new location: "))
                print("Successfully updated location")

            elif decision == 6:
                print("You have selected to edit Description")
                experience.Description = input("Enter the new description: ")
                print("Successfully updated description")   

            elif decision == -1:
                print("You have selected to quit edition of experience")
                return experience

            else:
                print("\nError! Could not edit experience due to invalid entry.")
        
        except:
            print("\nError! Could not edit due to invalid input on attribute index.")


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
                print("\nError! Could not confirm changes due to invalid input.")
        
        except:
            print("\nError! Could not confirm changes due to invalid input.")


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
                print("\nYou have selected to update education")

                try:
                    print("Would you like to add or edit education?")
                    MenuHelpers.DisplayOptions(["Add", "Edit"])
                    updateDecisionEducation: int = MenuHelpers.InputOptionNo()

                    if updateDecisionEducation == 1:
                        print("You have selected to add education")
                        try:
                            education = Education()
                            education.SchoolName = ToTitleFormat(input("Enter the name of your school: "))
                            education.Degree = ToTitleFormat(input("Enter your degree: "))
                            education.YearsAttended = int(input("Enter the years attended: "))
                            profile.EducationList.append(education)
                        except:
                            print("\nError! Could not add education due to invalid input.")
                    
                    elif updateDecisionEducation == 2:
                        print("You have selected to edit education")
                        # check to see if the user has any education
                        if len(profile.EducationList) == 0:
                            print("\nError! Could not edit education due to empty list of education.")
                        else:
                            print("\nSelect the index of the education to edit: ")
                            try:
                                educationIndex: int = MenuHelpers.InputOptionNo()
                                if educationIndex in range(1, len(profile.EducationList) + 1):
                                    profile.EducationList[educationIndex-1] = helpEditEducationAttributes(education=profile.EducationList[educationIndex-1])
                                    print("\nSuccess! Edited education.")
                                else:
                                    print("\nError! Could not edit education becuase entry is out of education list size.")
                            except:
                                print("\nError! Could not edit education due to invalid input on the education index.")
                    else:
                        print("\nError! Could not update education due to invalid input.")

                except:
                    print("\nError! Could not update education due to invalid input.")

            elif decision == 6:
                print("\nYou have selected to update experience")

                try:
                    print("Would you like to add or edit experience?")
                    MenuHelpers.DisplayOptions(["Add", "Edit"])
                    updateDecisionExperience: int = MenuHelpers.InputOptionNo()

                    if updateDecisionExperience == 1:
                        print("You have selected to add experience")
                        try:
                            if ProfileHelpers.IsProfileExpLimitMet(profile=userLoggedIn.Profile):
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
                            print("\nError! Could not add experience due to invalid input.")

                    elif updateDecisionExperience == 2:
                        print("You have selected to edit experience")
                        
                        if len(profile.ExperienceList) == 0:
                            print("\nError! Could not edit experience due to empty list of experience.")
                        else:
                            print("Select the index of the experience to edit: ")
                            try:
                                experienceIndex: int = MenuHelpers.InputOptionNo()
                                if experienceIndex in range(1, len(profile.ExperienceList) + 1):
                                    profile.ExperienceList[experienceIndex-1] = helpEditExperienceAttributes(experience=profile.ExperienceList[experienceIndex-1])
                                    print("\nSuccess! Edited experience.")
                                else:
                                    print("\nError! Could not edit experience because entry is out of experience list size.")
                            except:
                                print("\nError! Could not edit experience due to invalid input on the experience index.")
                    else:
                        print("\nError! Could not update education due to invalid input.")
                
                except:
                    print("\nError! Could not update education due to invalid input.")

            elif decision == -1:
                print("You have selected to quit.")
                break
        
        except:
            print("\nError! Something went wrong when trying to update a profile.")


    return ConfirmChanges(loggedUser=userLoggedIn, profile=profile)
    