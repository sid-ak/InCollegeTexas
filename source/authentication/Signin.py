from model.User import User, UserHelpers
from actions.FindSomeone import FindSomeoneAction
from actions.JobInternshipSearch import FindJobInternshipAction
from actions.LearnNewSkill import PresentSkillsAction
from actions.DisplayImpLinks import DisplayImpLinks
from helpers.MenuHelpers import MenuHelpers

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
                print("\nPlease enter one of the following options to continue:")
                options = ["Search for a job or internship",
                    "Find someone that you know",
                    "Learn a new skill",
                    "Display important links"]

                while True:
                    try:
                        MenuHelpers.DisplayOptions(options)

                        decision = MenuHelpers.InputOptionNo()

                        if decision == 1:
                            print("\nYou have selected to search for job or internship.")
                            FindJobInternshipAction(loggedUser)
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
                            DisplayImpLinks(loggedUser)
                            break
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