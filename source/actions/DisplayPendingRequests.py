from dataclasses import dataclass
import hashlib
from firebaseSetup.Firebase import database
from model.User import User, UserHelpers
from helpers.MenuHelpers import MenuHelpers
#import: GetPendingRequests, AcceptRequest, RejectRequest

# we will be showing the pending requests the logged in user has
# and display an option to accept or reject the requests at the end

def DisplayPendingRequests(loggedUser: User):
    while True:
        try:
            print("Your pending requests:\n")
            GetPendingRequests(loggedUser) # calling Osama's function
            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["1 - accept a request", "2 - reject a request"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to accept a request.\nEnter the username of the user you want to accept the request from.")
                AcceptRequest(loggedUser) #calling Osama's function

            elif decision == 2:
                print("You have selected to reject a request.\nEnter the username of the user you want to reject the request from.")
                RejectRequest(loggedUser) #calling Osama's function

            elif decision == -1:
                break

            else:
                print("Please enter 1 to accept a request, 2 to reject a request or -1 to go back.")
        except:
            print("Unexpected error ocurred\n")