from authentication.Signup import RegisterNewUser, CheckDBSize
from authentication.Signin import LoginUser
from model.User import User
from actions.SearchUser import SearchUser
from actions.PlayVideo import PlayVideo
from actions.DisplayImpLinks import DisplayImpLinks
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from helpers.MenuHelpers import MenuHelpers

# this is the main run file
class Main:
    
    # The user that is currently logged in.
    loggedUser: User = None

    print("\nWelcome to InCollege!")
    print("\n77% of users found InCollegeTexas to be really helpful in making new connection and in finding a job.\n"
        + "Gopal, one of our users was able to get an internship with XYZ corporation using our platform.\n")

    while True:
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
                loggedUser = LoginUser()
            
            elif decision == 2:
                print("\n\nSignup Selected.")
                if not CheckDBSize():
                    print("\nFailure! We have not been able to create a new account for you.")
                else:
                    if RegisterNewUser():
                        print("\nSuccess! You have successfully created a new account.\n")
                    else:
                        print("\nFailure! We have not been able to create a new account for you.")
            
            elif decision == 3:
                print("\n\nVideo Selected")
                PlayVideo()

            elif decision == 4:
                print("\n\nSearch User Selected")
                SearchUser()
            
            elif decision == 5:
                print("\n\nImportant Links Selected")
                DisplayImpLinks(loggedUser=loggedUser)

            elif decision == 6:
                print("\n\nUseful Links Selected")
                DisplayUsefulLinks()
            
            elif decision == -1:
                print("\n\nExit selected.\n")
                break
            
            else:
                print("Invalid entry! Please try again.")
        except:
            print("Invalid entry! Please try again.")