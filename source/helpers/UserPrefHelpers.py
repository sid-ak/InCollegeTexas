from enums.UserTierEnum import UserTierEnum
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
