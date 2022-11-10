from actions.ShowInbox import ShowInbox
from helpers.UserPrefHelpers import UserPrefHelpers
from model.User import User
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
from helpers.UserHelpers import UserHelpers
from actions.UpdateProfile import EditProfile
from actions.ViewProfile import ViewProfile
from actions.DisplayAllUser import DisplayEveryUser
from helpers.NotificationHelpers import NotificationHelpers

# this function will check if the username and password exists 
# and returns True if so, False otherwise
def LoginUser(collection: str= "Users") -> User:
    try:
        print("\nLogin Selected.")
        
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
                return user
            else:
                continue

        print("\nIncorrect username/password, please try again.")
        return None
    except:
        print("\nError! Something went wrong when connecting to database!")
        return None

def DisplayLoginMenu(loggedUser: User):
            # if the user logged in, continue with additional options
            print(f"\nWelcome to your account, {loggedUser.Username}!")

            # this variable will help us find out if we want to end the session of the user
            terminateSession: bool = False

            while True:
                
                # Display notifications that need to be displayed in the log in menu. 
                NotificationHelpers.DisplayLoginNotifications(loggedUser)

                # Update the last time the user logged in after all notifications are displayed.
                UserHelpers.UpdateLastLogin(loggedUser)
                
                print("\nPlease enter one of the following options to continue:\n")
                options = [
                    "Search for a job or internship",
                    "Find someone that you know",
                    "Learn a new skill",
                    "Display important links",
                    "Display useful links",
                    "Search Users",
                    "Display pending requests", 
                    "Show my network",
                    "Update my profile",
                    "View my profile",
                    "Update my tier",
                    "Show my inbox",
                    "Show all Users"
                    ]

                while True:
                    try:
                        
                        MenuHelpers.DisplayOptions(options)

                        decision = MenuHelpers.InputOptionNo()

                        if decision == 1:
                            print("\nYou have selected to search for job or internship.")
                            FindJobInternshipAction(loggedUser = loggedUser)
                            break

                        elif decision == 2:
                            print("\nYou have selected to find someone you know.")
                            FindSomeoneAction()
                            break

                        elif decision == 3:
                            print("\nYou have selected to learn a new skill.")
                            PresentSkillsAction()
                            break

                        elif decision == 4:
                            print("\nYou have selected to display important links.")
                            DisplayImpLinks(loggedUser=loggedUser)
                            break

                        elif decision == 5:
                            print("\nYou have selected to display useful links.")
                            DisplayUsefulLinks()

                        elif decision == 6:
                            print("\nYou have selected to search users.")
                            SearchUsers(loggedUser)

                        elif decision == 7:
                            print("\nYou have selected to display pending requests.")
                            DisplayPendingRequests(loggedUser)

                        elif decision == 8: 
                            print("\nYou have selected to show my network.")
                            ShowMyNetwork(loggedUser) 

                        elif decision == 9:
                            print("\nYou have selected to update profile.")
                            EditProfile(userLoggedIn=loggedUser)

                        elif decision == 10:
                            print("\nYou have selected to view profile.")
                            ViewProfile(loggedUser)

                        elif decision == 11:
                            print("\nYou have selected to update your tier."
                                + f"\nCurrent tier: {loggedUser.TierEnum.name}")
                            tierSet: bool = UserPrefHelpers.ShowTierPreferences(loggedUser)
                            if not tierSet:
                                raise Exception("\nTier could not be set due to an unexpected exception.")
                        
                        elif decision == 12:
                            print("\nYou have selected to show your inbox.")
                            ShowInbox(loggedUser)
                            break

                        elif decision == 13:
                            print("\nYou have selected to see all the users.")
                            DisplayEveryUser(loggedUser)
                        
                        elif decision == -1:
                            print("\nYou have selected to log out of your account.")
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
