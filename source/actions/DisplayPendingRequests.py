from model.User import User
from helpers.MenuHelpers import MenuHelpers
from helpers.FriendHelpers import FriendHelpers

# we will be showing the pending requests the logged in user has
# and display an option to accept or reject the requests at the end
def DisplayPendingRequests(loggedUser: User = None, collection: str = "Users"):
    while True:
        try:
            print("Your pending requests:\n")
            pendingRequests = FriendHelpers.GetPendingRequests(loggedUser.Username, collection=collection)
            if (len(pendingRequests) == 0):
                print("You have no pending requests.\n")
                break
            for i, user in enumerate(pendingRequests):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))
            print("\nPlease select one of the following options: \n")
            MenuHelpers.DisplayOptions(["Accept a request", "Reject a request"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to accept a request.\nEnter the option number of the user you want to accept the request from: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(pendingRequests) + 1):
                    FriendHelpers.AcceptFriendRequest(loggedUser, pendingRequests[option-1])
                else:
                    print("Invalid input.\n")
                    continue

            elif decision == 2:
                print("You have selected to reject a request.\nEnter the option number of the user you want to reject the request from: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(pendingRequests)+1):
                    FriendHelpers.RejectFriendRequest(loggedUser, pendingRequests[option-1])
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
