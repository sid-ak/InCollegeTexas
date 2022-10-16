from model.User import User, UserHelpers
from actions.FindSomeone import FindSomeoneAction
from actions.JobInternshipSearch import FindJobInternshipAction
from actions.LearnNewSkill import PresentSkillsAction
from actions.DisplayImpLinks import DisplayImpLinks
from helpers.MenuHelpers import MenuHelpers
from actions.DisplayImpLinks import DisplayImpLinks
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from actions.ShowMyNetwork import ShowMyNetwork
from actions.DisplayPendingRequests import DisplayPendingRequests
from actions.SearchUsers import SearchUsers


# this function will check if the username and password exists 
# if it does, the user is directed to login functionalities of the app
def LoginUser(collection: str= "Users"):
    # this variable will indicate if the login has been successful
    loginSuccess: bool = False
    try:
        username = input("\nPlease enter your username: ")
        password = input("Please enter your password: ")
        
        userId = UserHelpers.CreateUserId(username, password)
        users = UserHelpers.GetAllUsers(collection=collection)
        
        if (users == None):
            raise Exception()

        for user in users:
            if user.Id == userId:
                print("\nYou have successfully logged in.")
                DisplayLoginMenu(user)
                loginSuccess = True

        if not loginSuccess:
            print("\nIncorrect username/password, please try again.")
    except:
        print("\nError! Something went wrong when connecting to database!")


def DisplayLoginMenu(loggedUser: User):
            # if the user logged in, continue with additional options
            print(f"\n\nWelcome to your account, {loggedUser.Username}!")

            # this variable will help us find out if we want to end the session of the user
            terminateSession: bool = False

            while True:
                print("\n\nPlease enter one of the following options to continue:")
                options = ["Search for a job or internship",
                    "Find someone that you know",
                    "Learn a new skill",
                    "Display important links",
                    "Display useful links",
                    "Search Users",
                    "Display pending requests", 
                    "Show my network"]

                while True:
                    try:
                        MenuHelpers.DisplayOptions(options)

                        decision = MenuHelpers.InputOptionNo()

                        if decision == 1:
                            print("SEARCH FOR JOB OR INTERNSHIP SELECTED")
                            FindJobInternshipAction(loggedUser)
                            break
                        elif decision == 2:
                            print("FINDING SOME THAT YOU KNOW SELECTED")
                            FindSomeoneAction()
                            break
                        elif decision == 3:
                            print("LEARNING A NEW SKILL SELECTED")
                            PresentSkillsAction()
                            break
                        elif decision == 4:
                            print("DISPLAY OF IMPORTANT LINKS SELECTED")
                            DisplayImpLinks(loggedUser=loggedUser)
                            break
                        elif decision == 5:
                            print("DISPLAY OF USEFUL LINKS SELECTED")
                            DisplayUsefulLinks()
                        elif decision == 6:
                            print("SEARCH OF USERS SELECTED")
                            SearchUsers(loggedUser)
                        elif decision == 7:
                            print("DISPLAY OF PENDING REQUESTS SELECTED")
                            DisplayPendingRequests(loggedUser)
                        elif decision == 8: 
                            print("SHOW OF MY NETWORK SELECTED")
                            ShowMyNetwork(loggedUser) 
                        elif decision == -1:
                            print("LOG OUT SELECTED")
                            terminateSession = True
                            break
                        else:
                            print("\nError! Invalid Entry!")
                    except:
                        print("\nError! Invalid entry!")
                        break

                if terminateSession:
                    break

            if terminateSession:
                print(f"\nGoodbye, {loggedUser.Username}.\n")