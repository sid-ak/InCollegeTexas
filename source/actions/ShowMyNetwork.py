from helpers.MessageHelpers import MessageHelpers
from model.Message import Message
from model.User import User
from helpers.MenuHelpers import MenuHelpers
from helpers.FriendHelpers import FriendHelpers
from actions.ViewProfile import ViewProfile

# we will show the logged in user's network and display an option to disconnect with friends at the end
def ShowMyNetwork(loggedUser: User = None):
    while True:
        try:
            print("\nYour network:\n")
            
            # this function will print the friends of the logged in user 
            friends = FriendHelpers.GetFriends(loggedUser.Username)

            if (len(friends) == 0):
                print("You have no friends yet.\n")
                break

            for i, user in enumerate(friends):
                print("{}. {} {}\n".format(i + 1, user.FirstName, user.LastName))

            print("\nPlease select one of the following options:\n")
            MenuHelpers.DisplayOptions([
                "View a friend's profile.",
                "Disconnect with a friend.",
                "Send a message to a friend."])
            decision = MenuHelpers.InputOptionNo()

            if decision == 1:
                print("You have selected to view a friend's profile.")
                if len(friends) == 1:
                    ViewProfile(loggedUser, friends[0])
                else:
                    print("Select the friend number you want to view the profile of: ")
                    option = MenuHelpers.InputOptionNo()
                    if option in range(1, len(friends) + 1):
                        ViewProfile(loggedUser, friends[option - 1])

            elif decision == 2:
                print("You have selected to disconnect with a friend.")
                if len(friends) == 1:
                    FriendHelpers.DeleteFriend(loggedUser, friends[0])
                else:
                    print("Enter the option number of the friend you want to disconnect with: ")
                    option = MenuHelpers.InputOptionNo()
                    if option in range(1, len(friends) + 1):
                        FriendHelpers.DeleteFriend(loggedUser, friends[option-1])
                    else:
                        print("Invalid input.\n")
            
            elif decision == 3:
                print("\nYou have selected to send a message to a friend."
                    + "\n\nEnter the option number of the friend to send a message to: ")
                
                option: int = int(input()) - 1
                if option in range(0, len(friends)):
                    
                    friendId: User = friends[option].Id
                    messageSent: bool = MessageHelpers.SendMessage(loggedUser.Id, friendId)

                    if not messageSent: raise Exception()
                
                else:
                    print("Invalid input.\n")

            elif decision == -1:
                break
            else:
                print("Invalid input.\n")
        except Exception as e:
            print(f"Unexpected error ocurred\n{e}")
            break