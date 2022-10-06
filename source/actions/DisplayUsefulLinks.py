from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from model.User import User

# Displays the following important links:
# A General option (which leads to “Sign Up”, “Help Center”, “About”, “Press”, “Blog”, “Careers”, and “Developers”)
# Browse InCollege, Business Solutions, and Directories

def DisplayUsefulLinks(loggedUser: User = None):
    while True:
        print ("\nPlease select one of the following links to display its content:"
            + "\n1 - General"
            + "\n2 - Browse InCollege"
            + "\n3 - Business Solutions"
            + "\n4 - Directories")

        try:
            optNo: int = MenuHelpers.InputOptionNo()

            if optNo == -1: break

            elif optNo == 1:
                DisplayUsefulLinksHelpers.General() # will lead to more options

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
            print("Unexpected exception ocurred, invalid input.\n"
            + "Please enter a number between 1 and 4.\n")
                    