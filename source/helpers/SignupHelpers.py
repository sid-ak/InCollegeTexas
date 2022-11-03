from enums.UserTierEnum import UserTierEnum
from helpers.UserPrefHelpers import UserPrefHelpers
from model.User import User
from helpers.MenuHelpers import MenuHelpers

class SignupHelpers:
    
    # Displays options for the user to set a tier for their account.
    def ShowTierPreferences(loggedUser: User, collection = "Users") -> bool:
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
