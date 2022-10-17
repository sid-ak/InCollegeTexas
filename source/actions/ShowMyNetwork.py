from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers


# we will show the logged in user's network and display an option to disconnect with friends at the end
def ShowMyNetwork(loggedUser: User = None):
    while True:
        try:
            #wait for the below function to be merged and edit the output accordingly
            # this function will print the friends of the logged in user 
            friends = UserHelpers.GetFriends(loggedUser.Username) 

            if (len(friends) == 0):
                print("\nYou have no friends yet.\n")
                break

            print("\n\nYour network:\n")
            for i, user in enumerate(friends):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))

            print("\nPlease select one of the following options:")
            MenuHelpers.DisplayOptions(["Disconnect with a friend"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("FRIEND DISONNECT SELECTED")
                print("\n\nPlease select the option number of the friend you want to disconnect with: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(friends) + 1):
                    UserHelpers.DeleteFriend(loggedUser, friends[option-1]) 
                else:
                    print("Invalid input.\n")
            elif decision == -1:
                break
            else:
                print("Invalid input.\n")
        except:
            print("Unexpected error ocurred\n")
            break