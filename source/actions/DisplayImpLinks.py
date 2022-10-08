from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayImpLinksHelpers import DisplayImpLinksHelpers
from model.User import User

# Displays the following important links:
# A Copyright Notice, About, Accessibility, User Agreement, 
# Privacy Policy, Cookie Policy, Copyright Policy, Brand Policy, 
# Guest Controls, and Languages.
# the parameters "onTest" and "testInput" are used for test purposes only
def DisplayImpLinks(onTest: bool = False, testInput: int = -1, loggedUser: User = None):
    while True:
        # we display the menu selections if not on test
        if not onTest:
            print("\nPlease select one of the following links to display its content:")
            MenuHelpers.DisplayOptions(
                ["Copyright Notice",
                "About",
                "Accessibility",
                "User Agreement",
                "Privacy Policy",
                "Cookie Policy",
                "Copyright Policy",
                "Brand Policy",
                "Languages"]
            )

        try:
            optionNo: int = -1
            # if not onTest, the function is not being tested - so we ask for user input
            if not onTest:
                optionNo = MenuHelpers.InputOptionNo()
            # otherwise, the function is being tested
            else:
                optionNo = testInput

            if optionNo == -1: break

            elif optionNo == 1:
                DisplayImpLinksHelpers.PrintCopyrightNotice()
            elif optionNo == 2:
                DisplayImpLinksHelpers.PrintAbout()
            elif optionNo == 3:
                DisplayImpLinksHelpers.PrintAccessibility()
            elif optionNo == 4:
                DisplayImpLinksHelpers.PrintUserAgreement()
            elif optionNo == 5:
                DisplayImpLinksHelpers.PrintPrivacyPolicy(onTest=onTest, loggedUser=loggedUser)
            elif optionNo == 6:
                DisplayImpLinksHelpers.PrintCookiePolicy()
            elif optionNo == 7:
                DisplayImpLinksHelpers.PrintCopyrightPolicy()
            elif optionNo == 8:
                DisplayImpLinksHelpers.PrintBrandPolicy()
            elif optionNo == 9:
                DisplayImpLinksHelpers.ShowLanguagePreferences(onTest=onTest, loggedUser=loggedUser)
            else:
                print("Unexpected exception ocurred, invalid input.\n"
                    + "Please enter a number between 1 and 10.\n")
        
        except:
            print("Unexpected exception ocurred, invalid input.\n"
            + "Please enter a number between 1 and 10.\n")
        
        if onTest:
            break

