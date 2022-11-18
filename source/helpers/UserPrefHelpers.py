from enums.UserTierEnum import UserTierEnum
from helpers.MenuHelpers import MenuHelpers
from model.User import User
from helpers.UserHelpers import UserHelpers
from enums.LanguageEnum import LanguageEnum

class UserPrefHelpers:
    # Toggles the email preference for a user.
    def ToggleEmailEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.EmailEnabled = not user.EmailEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nEmail Enabled: {user.EmailEnabled}")
        except:
            print("Exception occurred. Email preference could not be toggled.")

    # Toggles the sms preference for a user.
    def ToggleSmsEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.SmsEnabled = not user.SmsEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nSMS Enabled: {user.SmsEnabled}")
        except:
            print("Exception occurred. SMS preference could not be toggled.")

    # Toggles the advertising preference for a user.
    def ToggleTargetedAdvertEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.TargetedAdvertEnabled = not user.TargetedAdvertEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nTargeted Advertising Enabled: {user.TargetedAdvertEnabled}")
        except:
            print("Exception occurred. Targeted Advertising preference could not be toggled.")

    # Sets the preferred language for a user as specified.
    def SetLangPreference(user: User, language: LanguageEnum, collection: str = "Users"):
        try:
            if user == None: return

            user.LanguagePreference = language
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nPreferred language set to: {user.LanguagePreference.name}")
        except:
            print("Exception occurred. Language preference could not be set.")

    # Displays options for the user to set a tier for their account.
    def ShowTierPreferences(loggedUser: User, collection: str = "Users"):
        try:
            while True:
                print("\nTier Preference:\n")

                if loggedUser == None:
                    raise Exception(f"\nArgument null exception: {loggedUser}")

                print("\nSelect an option to set your preferred tier:")
                
                options: list[str] = [UserTierEnum.Standard.name, UserTierEnum.Plus.name]
                MenuHelpers.DisplayOptions(options)
                
                decision: int = MenuHelpers.InputOptionNo()
                
                if decision == -1: break

                elif decision == 1: UserPrefHelpers.SetTierPreference(
                    loggedUser, UserTierEnum.Standard, collection)

                elif decision == 2: UserPrefHelpers.SetTierPreference(
                    loggedUser, UserTierEnum.Plus, collection)

                else:
                    print("\nUnexpected input, please select option 1 or 2.")

        except Exception as e:
            raise Exception(f"\nUnexpected exception occurred. Could not set tier preference.\n{e}")


    # Sets the preferred tier for a user as specified.
    def SetTierPreference(user: User, userTier: UserTierEnum, collection: str = "Users"):
        try:
            if user == None: return

            user.TierEnum = userTier
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nPreferred tier set to: {user.TierEnum.name}")

                if user.TierEnum == UserTierEnum.Standard:
                    print("\nYou will be using the app for free.")
                
                elif user.TierEnum == UserTierEnum.Plus:
                    print("\nYou will now be charged $10/month.")
            
        except Exception as e:
            print(f"Exception occurred. Tier preference could not be set.\n{e}")
