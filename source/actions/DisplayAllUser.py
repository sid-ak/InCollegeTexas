from model.User import User
from helpers.UserHelpers import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
 
def DisplayEveryUser(loggedUser: User, collection: str = "Users"):
        allUser = UserHelpers.GetAllUsers(collection)
        allUsers = list(map(lambda x: x.Username, allUser))
        displayU = list(filter(lambda user: user != loggedUser.Username, allUsers))
        
        while True:
            print("\nSelect one of the user to send a message\n")
            MenuHelpers.DisplayOptions(displayU)

            try:
                optionNo: int = MenuHelpers.InputOptionNo()

                if optionNo == -1: break

                elif optionNo in range(1, len(displayU) + 1):
                    print("hi")
            except:
                print("None")


            