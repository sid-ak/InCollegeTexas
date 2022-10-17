from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
# import:SearchUsers, SendFriendRequest

# user will be able to serach for users in the system by their last name, university, or major

def SearchUsers(loggedUser: User = None):
    while True:
        try:
            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["Search by last name", "Search by university", "Search by major"])
            decision = MenuHelpers.InputOptionNo()
            searchedUsers = []
            if decision == 1:
                lastName = input("You have selected to search by last name.\nEnter the last name of the user you want to search for: ")
                searchedUsers = UserHelpers.SearchByAttribute('LastName', lastName)
            elif decision == 2:
                university = input("You have selected to search by university.\nEnter the university of the user you want to search for: ")
                searchedUsers = UserHelpers.SearchByAttribute('University', university)
            elif decision == 3:
                major = input("You have selected to search by major.\nEnter the major of the user you want to search for: ")
                searchedUsers = UserHelpers.SearchByAttribute('Major', major)
            elif decision == -1:
                break
            else:
                print("Invalid input.\n")
                continue
            for i, user in enumerate(searchedUsers):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))
            print("Enter the option number of the user you want to send a friend request to: ")
            option = MenuHelpers.InputOptionNo()
            if option in range(1 , len(searchedUsers) + 1 ):
                FriendRequest(loggedUser, searchedUsers[option-1])
            elif option == -1:
                continue
            else:
                print("Invalid input.\n")
        except:
            print("Unexpected error ocurred\n")
            break

def FriendRequest(loggedUser: User = None , receiver: User = None):
    while True:
        try:
            print("Do you want to send a friend request?:\n")
            MenuHelpers.DisplayOptions(["Yes", "No"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                UserHelpers.SendFriendRequest(loggedUser, receiver)
                break
            elif decision == 2 or decision == -1:
                break
            else:
                print("Invalid input.\n")
                continue
        except:
            print("Unexpected error ocurred\n")
            break