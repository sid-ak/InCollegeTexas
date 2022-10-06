from helpers.MenuHelpers import MenuHelpers
from helpers.DisplayImpLinksHelpers import DisplayImpLinksHelpers
from model.User import User

# Displays the following important links:
# A Copyright Notice, About, Accessibility, User Agreement, 
# Privacy Policy, Cookie Policy, Copyright Policy, Brand Policy, 
# Guest Controls, and Languages.
def DisplayImpLinks(loggedUser: User = None):
    while True:
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
            optionNo: int = MenuHelpers.InputOptionNo()

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
                DisplayImpLinksHelpers.PrintPrivacyPolicy(loggedUser)
            elif optionNo == 6:
                DisplayImpLinksHelpers.PrintCookiePolicy()
            elif optionNo == 7:
                DisplayImpLinksHelpers.PrintCopyrightPolicy()
            elif optionNo == 8:
                DisplayImpLinksHelpers.PrintBrandPolicy()
            elif optionNo == 9:
                DisplayImpLinksHelpers.ShowLanguagePreferences(loggedUser)
            else:
                print("Unexpected exception ocurred, invalid input.\n"
                    + "Please enter a number between 1 and 10.\n")
        
        except:
            print("Unexpected exception ocurred, invalid input.\n"
            + "Please enter a number between 1 and 10.\n")

