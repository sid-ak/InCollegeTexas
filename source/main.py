from importlib.metadata import entry_points
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser
from model.User import User, UserHelpers
from actions.SearchUser import SearchUser
from actions.PlayVideo import PlayVideo
from actions.DisplayImpLinks import DisplayImpLinks
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from helpers.MenuHelpers import MenuHelpers

# this is the main run file
class Main:
    
    # This variable will help us identify if the user logged out of his/her account
    userLoggedOut: bool = False

    entryMessage = "\n--------------------------------------------------------------------------------------------------------"
    entryMessage += "\n\nWelcome to InCollege!\n"
    entryMessage += "\n77% of users found InCollegeTexas to be really helpful in making new connection and in finding a job."
    entryMessage += "\nGopal, one of our users was able to get an internship with XYZ corporation using our platform."

    print(entryMessage)

    while True:
        if userLoggedOut:
            print(entryMessage)
        print("\n\nPlease select an option to continue:")
        MenuHelpers.DisplayOptions(
            ["Log In",
            "Sign Up",
            "Play an Informational Video",
            "Search User",
            "Display Important Links",
            "Display Useful Links"]
        ) 
        try:
            decision: int = MenuHelpers.InputOptionNo()
            
            if decision == 1:
                print("LOGIN SELECTED")
                LoginUser()
                userLoggedOut = True

            elif decision == 2:
                print("SIGNUP SELECTED")
                if UserHelpers.IsUserLimitMet():
                    print("\nFailure! We have not been able to create a new account for you.")
                else:
                    if RegisterNewUser():
                        print("\nSuccess! You have successfully created a new account.\n")
                    else:
                        print("\nFailure! We have not been able to create a new account for you.")
            
            elif decision == 3:
                print("VIDEO SELECTED")
                PlayVideo()

            elif decision == 4:
                print("SEARCH USER SELECTED")
                SearchUser()
            
            elif decision == 5:
                print("IMPORTANT LINKS SELECTED")
                DisplayImpLinks()

            elif decision == 6:
                print("USEFUL LINKS SELECTED")
                DisplayUsefulLinks()
            
            elif decision == -1:
                print("EXIT SELECTED\n")
                break
            
            else:
                print("Invalid entry! Please try again.")
        except:
            print("Invalid entry! Please try again.")