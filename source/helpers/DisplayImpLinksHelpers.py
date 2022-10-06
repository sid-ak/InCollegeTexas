from helpers.MenuHelpers import MenuHelpers
from model.User import User, UserHelpers

class DisplayImpLinksHelpers:

    def PrintCopyrightNotice():
        print("\nCopyright:")
        print("\n© Team Texas, Inc\n")

    def PrintAbout():
        print("\nAbout:")
        print("\nTeam Texas consists of five hardworking Computer Science and Engineering majors"
            + "\nwho aim to make this application a seamless experience for you, the user."
            + "\nWe have two developers, two testers and one scrum master"
            + "\nto keep this application working\n")

    def PrintAccessibility():
        print("\nAccessibility:")
        print("\nWe are currently working to make this app accessible across all platforms and"
            + "\nversions of android, iOS and Windows. Hold on tight!\n")

    def PrintUserAgreement():
        print("\nUser Agreement:")
        print("\nWelcome!"
            + "\nWhen you are using our application, you are agreeing to InCollege's Privacy,"
            + "\nCookie, Copyright and Brand Policy.\n")
    
    def PrintPrivacyPolicy(loggedUser: User = None):
        while True:
            try:
                print("\nPrivacy Policy:")
                print("\nWe make sure that your passwords are protected safely!\n"
                    + "\nAdditional options:"
                    + "\n1 - Guest Controls")
                
                decision: int = MenuHelpers.InputOptionNo()

                if decision == -1: break

                elif decision == 1:
                    DisplayImpLinksHelpers.ShowGuestControls(loggedUser)

            except:
                print("\nAn unexpected error ocurred.")


    def PrintCookiePolicy():
        print("\nCookie Policy:")
        print("\nNo cookies are used to use this application!"
            + "\nThis will be updated timely when we do."
            + "\nEnjoy the app till then!\n")

    def PrintCopyrightPolicy():
        print("\nCopyright Policy:")
        print("\nYou may not share, distribute, or reproduce in any way any"
            + "\ncopyrighted material, trademarks, or"
            + "\nother proprietary information belonging to others without"
            + "\nobtaining the prior written consent of the owner of such proprietary rights\n")

    def PrintBrandPolicy():
        print("\nBrand Policy:")
        print("\n1 - Provide ease of use."
            + "\n2 - Have a seamless user experience."
            + "\n3 - Store data effectively.\n")
    
    # Allows a user to toggle certain notification preferences.
    def ShowGuestControls(loggedUser: User = None):
        while True:
            print("\nGuest Controls:")

            if loggedUser == None:
                print("You must be logged in to modify guest controls")
                break
            
            print("\nSelect an option to toggle it on or off")
            MenuHelpers.DisplayOptions(["InCollege Email", "SMS", "Targeted Advertising"])
            
            decision: int = MenuHelpers.InputOptionNo()

            if decision == -1: break
            
            elif decision == 1: UserHelpers.ToggleEmailEnabled(loggedUser)
            elif decision == 2: UserHelpers.ToggleSmsEnabled(loggedUser)
            elif decision == 3: UserHelpers.ToggleTargetedAdvertEnabled(loggedUser)

            else:
                print("Unexpected exception ocurred, invalid input.\n"
                    + "Please enter a number between 1 and 3.\n")

    # TODO: Finish method.
    def ShowLanguagePreferences(loggedUser: User = None):
        print("\nLanguage Preference:")
        MenuHelpers.PrintUnderConstruction()