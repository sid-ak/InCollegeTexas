from model.Profile import Profile, Education, Experience
from helpers.MenuHelpers import MenuHelpers
from model.User import User
from helpers.UserHelpers import UserHelpers
from helpers.ProfileHelpers import ProfileHelpers


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
    if ProfileHelpers.ProfileExists(userLoggedIn):
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
                        "Education (Can add more than 1): " +  ProfileHelpers.HelpPrintEducationList(profile=profile), 
                        "Experience (Can add up to 3): " + ProfileHelpers.HelpPrintExperienceList(profile=profile)]

            MenuHelpers.DisplayOptions(options=options)
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("\nYou have selected to update a title")
                title = input("Please enter your title: ")
                profile.Title = title

            elif decision == 2:
                print("\nYou have selected to update a university")
                university = ProfileHelpers.ToTitleFormat(input("Please enter your university's name: "))
                profile.University = university

            elif decision == 3:
                print("\nYou have selected to update a major")
                major = ProfileHelpers.ToTitleFormat(input("Please enter your major: "))
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
                            education.SchoolName = ProfileHelpers.ToTitleFormat(input("Enter the name of your school: "))
                            education.Degree = ProfileHelpers.ToTitleFormat(input("Enter your degree: "))
                            education.YearsAttended = int(input("Enter the years attended: "))
                            if education != Education():
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
                                    profile.EducationList[educationIndex-1] = ProfileHelpers.HelpEditEducationAttributes(education=profile.EducationList[educationIndex-1])
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
                                experience.Title = ProfileHelpers.ToTitleFormat(input("Enter title: "))
                                experience.Employer = ProfileHelpers.ToTitleFormat(input("Enter Employer: "))
                                experience.DateStarted = input("Enter date started: ")
                                experience.DateEnded = input("Enter date ended: ")
                                experience.Location = ProfileHelpers.ToTitleFormat(input("Enter location: "))
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
                                    profile.ExperienceList[experienceIndex-1] = ProfileHelpers.HelpEditExperienceAttributes(experience=profile.ExperienceList[experienceIndex-1])
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
    