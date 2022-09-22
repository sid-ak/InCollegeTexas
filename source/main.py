from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser
from authentication.Signup import CheckDBSize
from actions.FindSomeone import FindSomeoneAction
from actions.JobInternshipSearch import FindJobInternshipAction
from actions.LearnNewSkill import PresentSkillsAction
from model.User import User, UserHelpers


# this is the main run file
class Main:
    
    # this variable will let us know if the user logged in or no
    flagLoggedin = False
    # this dictionary will store the username and password of a logged in user
    loggedUser: User

    print("\n77% of users found InCollegeTexas to be really helpful in making new connection and in finding a job.\n" + "Gopal, one of our users was able to get an internship with XYZ corporation using our platform.\n")

    print('Welcome!\nPlease, select:\n"1" to login your account\n"2" to sign up with a new account\n"3" to play the informational video')

    while True:
        try:
            decision = int(input("\nEnter (-1 to Exit): "))
            if decision == 1:
                print("\nLogin Selected.")
                username = input("\nPlease enter your username: ")
                password = input("Please enter your password: ")
                if LoginUser(username=username, password=password):
                        # change the attribute of flag to True
                        flagLoggedin = True
                        loggedUserId = UserHelpers.CreateUserId(username, password)
                        loggedUser = User(loggedUserId, username)
                else:
                    print("Failure! Incorrect credentials.")
            elif decision == 2:
                print("\nSignup Selected.")
                if not CheckDBSize():
                    print("\nFailure! We have not been able to create a new account for you.")
                else:
                    username = input("\nPlease enter your username: ")
                    password = input("Please enter your password: ")
                    if RegisterNewUser(username=username, password=password):
                        print("\nSucess! You have sucessfully created a new account.\n")
                    else:
                        print("\nFailure! We have not been able to create a new account for you.")
            elif decision == 3:
                print("\nVideo Selected")
                playVideo()
            elif decision == -1:
                print("\nExit selected.\n")
                break
            else:
                print("Invalid entry! Please try again.")
        except:
            print("Invalid entry! Please try again.")
   
        if flagLoggedin:
            # if the user logged in, continue with additional options
            print(f"\nWelcome to your account, {loggedUser.Username}!")

            # this variable will help us find out if we want to end the session of the user
            terminateSession = False

            while True:
                print("\nPlease enter one of the following options to continue:")
                options = '"1" - to search for a job or internship\n"2" - to find someone that you know\n"3" - to learn a new skill\n"-1" - to log out of your account'

                while True:
                    try:
                        print(options)
                        decision = int(input("\nEnter (-1 to Log Out): "))

                        if decision == 1:
                            print("\nYou have selected to search for job or internship.")
                            FindJobInternshipAction()
                            break
                        elif decision == 2:
                            print("\nYou have selected to find someone you know.")
                            FindSomeoneAction()
                            break
                        elif decision == 3:
                            print("\nYou have selected to learn a new skill.")
                            action_response = PresentSkillsAction()
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
                break

