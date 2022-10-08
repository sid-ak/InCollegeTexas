from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from model.User import User

# Displays the following important links:
# A General option (which leads to “Sign Up”, “Help Center”, “About”, “Press”, “Blog”, “Careers”, and “Developers”)
# Browse InCollege, Business Solutions, and Directories

def DisplayUsefulLinks(onTest: bool = False, testInput: int = -1, loggedUser: User = None):
    while True:

        if not onTest:
            print("\nPlease select one of the following links to display its content:")
            MenuHelpers.DisplayOptions(
                [
                    "General",
                    "Browse InCollege",
                    "Business Solutions",
                    "Directories"
                ]
            )

        try:
            optNo: int = -1

            if not onTest:
                optNo = MenuHelpers.InputOptionNo()
            
            else:
                optNo = testInput

            if optNo == -1: break

            elif optNo == 1:
                DisplayUsefulLinksHelpers.General(onTest=onTest,testInput = 2,loggedUser=loggedUser) # will lead to more options

            elif optNo == 2:
                DisplayUsefulLinksHelpers.BrowseInCollege()

            elif optNo == 3:
                DisplayUsefulLinksHelpers.BusinessSolutions()

            elif optNo == 4:
                DisplayUsefulLinksHelpers.Directories()

            else :
                print("Unexpected exception ocurred, invalid input.\n"
                    + "Please enter a number between 1 and 4.\n")
    
        except:
            print("Unexpected error ocurred\n")

        if onTest:
            break
                