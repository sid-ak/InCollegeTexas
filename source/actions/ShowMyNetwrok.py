from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers, GetFriends
from helpers.MenuHelpers import MenuHelpers
#something for DisconnectWithFriend function

# we will show the logged in user's network and display an option to disconnect with friends at the end
def ShowMyNetwork(loggedUser: User):
    while True:
        try:
            print("Your network:\n")

            #wait for the below function to be merged and edit the output accordingly
            GetFriends(loggedUser) # this function will print the friends of the logged in user 

            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["1 - Do you want to disconnect with a friend?"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to disconnect with a friend.")
                DisconnectWithFriend(loggedUser) #calling Osama's function
                break
            elif decision == -1:
                break
            else:
                print("Please enter 1 to disconnect with a friend or -1 to go back.")
        except:
            print("Unexpected error ocurred\n")