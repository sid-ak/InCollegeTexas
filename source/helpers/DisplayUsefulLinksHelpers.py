from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayGeneralLinksHelpers import DisplayGeneralLinksHelpers
from authentication.Signup import RegisterNewUser, CheckDBSize
from model.User import User

class DisplayUsefulLinksHelpers:

    def General(onTest: bool = False, testInput: int = -1, loggedUser: User = None):
        while True:
            print("\nPlease select one of the following links to display its content:")

            MenuHelpers.DisplayOptions(
                [
                    "Sign Up",
                    "Help Center",
                    "About",
                    "Press",
                    "Blog",
                    "Careers",
                    "Developers"
                ]
            )

            try:
        
                optionNo: int = -1

                if not onTest:
                    optionNo = MenuHelpers.InputOptionNo()
                
                else:
                    optionNo = testInput

                if optionNo == -1: break

                elif optionNo == 1:
                    print("SIGNUP SELECTED")
                    if not CheckDBSize():
                        print("\nFailure! We have not been able to create a new account for you.")
                    else:
                        if RegisterNewUser():
                            print("\nSuccess! You have successfully created a new account.\n")
                        else:
                            print("\nFailure! We have not been able to create a new account for you.")

                elif optionNo == 2:
                    DisplayGeneralLinksHelpers.ShowHelpCenter()

                elif optionNo == 3:
                    DisplayGeneralLinksHelpers.ShowAbout()

                elif optionNo == 4:
                    DisplayGeneralLinksHelpers.ShowPress()

                elif optionNo == 5:
                    DisplayGeneralLinksHelpers.ShowBlog()

                elif optionNo == 6:
                    DisplayGeneralLinksHelpers.ShowCareers()

                elif optionNo == 7:
                    DisplayGeneralLinksHelpers.ShowDevelopers()

                else:
                    print("Unexpected exception ocurred, invalid input.\n"
                    + "Please enter a number between 1 and 7.\n")

            
            except:
                print("Unexpected exception ocurred, invalid input.\n"
                + "Please enter a number between 1 and 7.\n")

            if onTest:
                break

    def BrowseInCollege():
        MenuHelpers.PrintUnderConstruction()

    def BusinessSolutions():
        MenuHelpers.PrintUnderConstruction()
    
    def Directories():
        MenuHelpers.PrintUnderConstruction()