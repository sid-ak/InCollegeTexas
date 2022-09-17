from firebase.Firebase import database
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser
from loggedInActions.FindSomeone import FindSomeoneAction
from loggedInActions.JobInternshipSearch import FindJobInternshipAction
from loggedInActions.LearnNewSkill import PresentSkillsAction


# this is the main run file
class Main:
    
    # this variable will let us know if the user logged in or no
    flag_logged_in = False
    # this dictionary will store the username and password of a logged in user
    logged_user = {} 

    print('\nWelcome to InCollege! \nPlease, select "1" to login or "2" to sign up with a new account')

    while True:
        try:
            decision = int(input("\nEnter (-1 to Exit): "))
            if decision == 1:
                print("\nLogin Selected.")
                username = input("\nPlease enter your username: ")
                password = input("Please enter your password: ")
                if LoginUser(username=username, password=password):
                        # change the attribute of flag to True
                        flag_logged_in = True
                        logged_user["username"] = username
                        logged_user["password"] = password
                else:
                    print("Failure! Incorrect credentials.")
            elif decision == 2:
                print("\nSignup Selected.")
                username = input("\nPlease enter your username: ")
                password = input("Please enter your password: ")
                if RegisterNewUser(username=username, password=password):
                    print("\nSucess! You have sucessfully created a new account.\n")
                else:
                    print("\nFailure! We have not been able to create a new account for you.")
            elif decision == -1:
                print("\nExit selected.\n")
                break
            else:
                print("Invalid entry! Please try again.")
        except:
            print("Invalid entry! Please try again.")
   
        if flag_logged_in:
            # if the user logged in, continue with additional options
            print(f"\nWelcome to your account, {logged_user['username']}!")

            # this variable will help us find out if we want to end the session of the user
            terminate_session = False

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
                            terminate_session = True
                            break
                        else:
                            print("\nError! Invalid Entry!")
                    except:
                        print("\nError! Invalid entry!")
                        break

                if terminate_session:
                    break

            if terminate_session:
                print(f"\nGoodbye, {logged_user['username']}.\n")
                break


