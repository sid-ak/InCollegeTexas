from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers, GetFriends
from helpers.MenuHelpers import MenuHelpers
# import:SearchUsers, SendFriendRequest

# user will be able to serach for users in the system by their last name, university, or major

def SearchUsers():
    while True:
        try:
            print("Please select one of the following options:\n")
            MenuHelpers.DisplayOptions(["1 - Search by last name", "2 - Search by university", "3 - Search by major"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to search by last name.\nEnter the last name of the user you want to search for.")
                # query into the database to search for the user by last name
                FriendRequest()
            elif decision == 2:
                print("You have selected to search by university.\nEnter the university of the user you want to search for.")
                # query into the database to search for the user by university
                FriendRequest()
            elif decision == 3:
                print("You have selected to search by major.\nEnter the major of the user you want to search for.")
                # query into the database to search for the user by major
                FriendRequest()
            elif decision == -1:
                break
            else:
                print("Please enter 1 to search by last name, 2 to search by university, 3 to search by major or -1 to go back.")
        except:
            print("Unexpected error ocurred\n")

def FriendRequest():
    while True:
        try:
            print("Do you want to send a friend request?:\n")
            MenuHelpers.DisplayOptions(["1 - Yes", "-1 - Go back"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                SendFriendRequest() #somethingin () #Osama's function being called
            #elif decision == -1:
                #break
            else:
                print("Please enter 1 to send a friend request or 2 to go back.")
        except:
            print("Unexpected error ocurred\n")