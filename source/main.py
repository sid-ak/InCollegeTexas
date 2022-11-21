from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser
from model.User import User
from actions.SearchUser import SearchUser
from actions.PlayVideo import PlayVideo
from actions.DisplayImpLinks import DisplayImpLinks
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from helpers.MenuHelpers import MenuHelpers
from helpers.UserHelpers import UserHelpers
from apis.outputAPIs import RunOutputAPIs
from apis.inputAPIs import RunInputAPIS

# this is the main run file
class Main:

    if not RunInputAPIS(): 
        print("\nFailure in Input API's! Some possible reasons include the formatting in the input files, input files not existing, etc.\n")
    if not RunOutputAPIs(): 
        print("\nFailure in Output API's! Some possible reasons include the connection to database, etc.\n")

    print("\n77% of users found InCollegeTexas to be really helpful in making new connection and in finding a job.\n"
        + "Gopal, one of our users was able to get an internship with XYZ corporation using our platform.\n")

    while True:
        try:
            
            print("\nWelcome!\nPlease select an option to continue:")
            MenuHelpers.DisplayOptions(
                ["Log In",
                "Sign Up",
                "Play an Informational Video",
                "Search User",
                "Display Important Links",
                "Display Useful Links"]
            )

            decision: int = MenuHelpers.InputOptionNo()
            
            if decision == 1:
                loggedUser: User = LoginUser()
                if loggedUser == None:
                    print("Failure! Incorrect credentials.")
            
            elif decision == 2:
                print("\nSignup Selected.")
                if UserHelpers.IsUserLimitMet():
                    print("\nFailure! We have not been able to create a new account for you. The maximum number of users limit met.")
                else:
                    if RegisterNewUser():
                        print("\nSuccess! You have successfully created a new account.\n")
                    else:
                        print("\nFailure! We have not been able to create a new account for you.")
            
            elif decision == 3:
                print("\nVideo Selected")
                PlayVideo()

            elif decision == 4:
                print("\nSearch User Selected")
                SearchUser()
            
            elif decision == 5:
                print("\nImportant Links Selected")
                DisplayImpLinks()

            elif decision == 6:
                print("\nUseful Links Selected")
                DisplayUsefulLinks()
            
            elif decision == -1:
                print("\nExit selected.\n")
                break
            
            else:
                print("Invalid entry! Please try again.")
        
        except Exception as e:
            print(f"Invalid entry! Please try again.\n{e}")
