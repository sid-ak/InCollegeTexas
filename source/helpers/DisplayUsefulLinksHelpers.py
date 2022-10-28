from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayGeneralLinksHelpers import DisplayGeneralLinksHelpers
from authentication.Signup import RegisterNewUser
from model.User import User
from helpers.UserHelpers import UserHelpers

class DisplayUsefulLinksHelpers:

    def General():
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


                optionNo = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo == 1:
                    print("\nSignup Selected.")
                    if UserHelpers.IsUserLimitMet():
                        print("\nAll permitted accounts have been created, please come back later!")
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


    def BrowseInCollege():
        MenuHelpers.PrintUnderConstruction()

    def BusinessSolutions():
        MenuHelpers.PrintUnderConstruction()
    
    def Directories():
        MenuHelpers.PrintUnderConstruction()