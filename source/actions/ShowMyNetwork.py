from model.User import User
from helpers.MenuHelpers import MenuHelpers
from helpers.FriendHelpers import FriendHelpers

# we will show the logged in user's network and display an option to disconnect with friends at the end
def ShowMyNetwork(loggedUser: User = None):
    while True:
        try:
            print("Your network:\n")
            
            # this function will print the friends of the logged in user 
            friends = FriendHelpers.GetFriends(loggedUser.Username)

            if (len(friends) == 0):
                print("You have no friends yet.\n")
                break

            for i, user in enumerate(friends):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))

            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions(["Do you want to disconnect with a friend?"])
            decision = MenuHelpers.InputOptionNo()
            if decision == 1:
                print("You have selected to disconnect with a friend.")
                print("Enter the option number of the friend you want to disconnect with: ")
                option = MenuHelpers.InputOptionNo()
                if option in range(1, len(friends) + 1):
                    FriendHelpers.DeleteFriend(loggedUser, friends[option-1]) 
                else:
                    print("Invalid input.\n")
            elif decision == -1:
                break
            else:
                print("Invalid input.\n")
        except:
            print("Unexpected error ocurred\n")
            break