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
                        "Education (Can add more than 1): "
                            + ProfileHelpers.HelpPrintEducationList(
                                educationList = profile.EducationList), 
                        "Experience (Can add up to 3): " 
                            + ProfileHelpers.HelpPrintExperienceList(
                                experienceList = profile.ExperienceList)]

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
                try:
                    print("\nYou have selected to update education")
                    educationList: list[Education] = ProfileHelpers.UpdateEducation(
                        profile.EducationList)
                    profile.EducationList = educationList
                
                except Exception as e:
                    print(f"\nError! Could not update education.\n{e}")

            elif decision == 6:
                print("\nYou have selected to update experience")

                try:
                    experienceList: list[Experience] = ProfileHelpers.UpdateExperience(
                        profile.ExperienceList)
                    profile.ExperienceList = experienceList

                except Exception as e:
                    print(f"\nError! Could not update experience.\n{e}")

            elif decision == -1:
                print("You have selected to quit.")
                break
        
        except Exception as e:
            print(f"\nError! Something went wrong when trying to update a profile.\n{e}")
            break


    return ConfirmChanges(loggedUser=userLoggedIn, profile=profile)
    