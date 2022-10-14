from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
#something for DisconnectWithFriend function

# we will show the logged in user's network and display an option to disconnect with friends at the end
def ShowMyNetwork(loggedUser: User):
    while True:
        try:
            print("Your network:\n")

            #wait for the below function to be merged and edit the output accordingly
            friends = UserHelpers.GetFriends(loggedUser) # this function will print the friends of the logged in user 

            if (len(friends) == 0):
                print("You have no friends yet.\n")
                break

            counter = 1
            for user in friends:
                print("{}. {} {}\n".format(counter, user.FirstName, user.LastName))
                counter += 1

            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["Do you want to disconnect with a friend?"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to disconnect with a friend.")
                UserHelpers.DeleteFriend(loggedUser) #calling Osama's function - param what?
                break
            elif decision == -1:
                break
            else:
                print("Please enter 1 to disconnect with a friend or -1 to go back.")
        except:
            print("Unexpected error ocurred\n")