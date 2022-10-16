from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers

# we will be showing the pending requests the logged in user has
# and display an option to accept or reject the requests at the end

def DisplayPendingRequests(loggedUser: User = None):
    while True:
        try:
            pendingRequests = UserHelpers.GetPendingRequests(loggedUser.Username) 
            if (len(pendingRequests) == 0):
                print("You have no pending requests.\n")
                break
            
            print("Your pending requests:\n")
            for i, user in enumerate(pendingRequests):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))
            print("\nPlease select one of the following options: \n")
            MenuHelpers.DisplayOptions(["Accept a request", "Reject a request"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to accept a request.\nEnter the option number of the user you want to accept the request from: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(pendingRequests) + 1):
                    UserHelpers.AcceptFriendRequest(loggedUser, pendingRequests[option-1])
                else:
                    print("Invalid input.\n")
                    continue

            elif decision == 2:
                print("You have selected to reject a request.\nEnter the option number of the user you want to reject the request from: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(pendingRequests)+1):
                    UserHelpers.RejectFriendRequest(loggedUser, pendingRequests[option-1])
                else:
                    print("Invalid input.\n")
                    continue

            elif decision == -1:
                break

            else:
                print("Invalid input.\n")
        except:
            print("Unexpected error ocurred\n")
            break
