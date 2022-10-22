from model.User import User
from helpers.UserHelpers import UserHelpers
from firebaseSetup.Firebase import database

class FriendHelpers:
    
    # takes User as parameter whose friends we need to find
    # returns a list of User (list[User]) of all of the userToFind's friends
    def GetFriends(userNameToFind: str, collection: str= "Users") -> list[User]:
        friends = []
        try:
            usersResponse = database.child(collection).get()
        except:
            print("Error reaching out to the DB!")
            return None
        try:
            for user in usersResponse.each():
                if user == None:
                    continue
                elif (user.val()["Username"] == userNameToFind):
                    try:
                        try:
                            friends_dict = user.val()["Friends"]
                        except:
                            return []

                        if len(friends_dict) == 0:
                            return friends

                        usersResponse2 = database.child(collection).get()
                        for friend in friends_dict:
                            for user2 in usersResponse2.each():
                                if user2.val()["Username"] == friend and friends_dict[friend] == True:
                                    friends.append(User.HydrateUser(user2))
                    except:
                        print("\nSomething went wrong accessing your friends!\n")
        except:
            print("\nOh no! An exception occurred. Report to admin\n")

        return friends

    # Gets pending friends of a user
    def GetPendingRequests(userName: str, collection: str = "Users") -> list[User]:
        pendingRequests = []
        try:
            usersResponse = database.child(collection).get()
        except:
            print("Error reaching to the DB!")
            return None
        for user in usersResponse.each():
            if user == None:
                continue
            elif (user.val()["Username"] == userName):
                try:
                    user = User.HydrateUser(user)
                    friends_dict = user.Friends
                    if len(friends_dict) == 0:
                        return []
                    users = UserHelpers.GetAllUsers(collection)
                    for friend in friends_dict:
                        for u in users:
                            if u.Username == friend and friends_dict[friend] == False:
                                pendingRequests.append(u)
                    return pendingRequests
                except:
                    print("Something went wrong")
                    return []

    # Sends friend request from sender to receiver
    # adds senders username to receivers friends dictionary as pending(False)
    def SendFriendRequest(sender: User, receiver: User, collection: str = "Users") -> bool:
        isPresent = UserHelpers.CheckUserPresenceInDB(receiver, collection)
        if not isPresent:
            print("Receiving user is not a registered user. Friend request can't be sent")
            return False

        if sender.Username in receiver.Friends:
            print("\nYou've already sent a request to this user!\n")
            return False

        try:
            friendResponse = database.child("Users").child(receiver.Id).get()
            receiver.Friends[sender.Username] = False
            new_dict = receiver.Friends
            try:
                friendResponse.val()['Friends']
            except:
                database.child(collection).child(receiver.Id).child("Friends").set(new_dict)

            database.child(collection).child(receiver.Id).child("Friends").set(new_dict)

            print(f"\nFriend request sent to: {receiver.Username}")
            return True

        except:
            print("\nException occurred. Friend request could not be sent\n")
            return False

    # function accepts User class object as param
    # and adds userToAdd user to their friends list
    # and adds user to userToAdd's friend list (2-way update)
    def AcceptFriendRequest(user: User, userToAdd: User, collection: str = "Users") -> bool:
        # check is user to add in DB
        isPresent = UserHelpers.CheckUserPresenceInDB(userToAdd, collection)
        if not isPresent:
            print("Receiving user is not a registered user. Friend request can't be sent")
            return False
        # check if userToAdd in users friend list
        if userToAdd.Username not in user.Friends:
            print(f"\nUh Oh! Something went wrong. {userToAdd.Username} couldn't be found\n")
            return False
        # check if userToAdd in users friend list and already accepted
        elif user.Friends[userToAdd.Username] == True:
            print(f"\nLooks like you're already friends with {userToAdd.Username}!\n")
            return False

        try:
            # add userToAdds username to user's friends dict in db
            user.Friends[userToAdd.Username] = True
            new_dict = user.Friends
            database.child(collection).child(user.Id).child("Friends").set(new_dict)
            # add user's username to userToAdd's friend dict in db
            userToAdd.Friends[user.Username] = True
            new_dict = userToAdd.Friends
            database.child(collection).child(userToAdd.Id).child("Friends").set(new_dict)

            print(f"\nSuccess! {userToAdd.Username} has been added as your friend!\n")
            return True

        except:
            print("\nOh No! Something went wrong while adding friends!\n")
            return False

    # rejecting a userToReject user by removing it from user User's Friend list
    def RejectFriendRequest(user: User, userToReject: User, collection: str = "Users") -> bool:
        # check if userToReject in DB
        isPresent = UserHelpers.CheckUserPresenceInDB(userToReject, collection)
        if not isPresent:
            print("Receiving user is not a registered user. Friend request can't be sent")
            return False

        # check if userToAdd in users friend list
        if userToReject.Username not in user.Friends:
            print(f"\nUh Oh! {userToReject.Username} isn't a friend\n")
            return False
        # check if userToReject iis already accepted
        elif user.Friends[userToReject.Username] == True:
            print(f"Can't reject {userToReject.Username}. {userToReject.Username} is an accepted friend!\n")
            return False

        try:
            #  remove userToRejects username from user's friends dict in db
            del user.Friends[userToReject.Username]
            new_dict = user.Friends
            database.child(collection).child(user.Id).child("Friends").set(new_dict)
            print(f"\nYou rejected {userToReject.Username}'s friend request.\n")
            return True
        except:
            print(f"\nUh Oh, there seemed to be an error rejecting {userToReject.Username}'s request.\n")
            return False

    # Deletes a friend by following a similar implementation to rejection of a friend.
    def DeleteFriend(user: User, userToDelete: User, collection: str = "Users") -> bool:

        isPresent = UserHelpers.CheckUserPresenceInDB(userToDelete, collection)
        if not isPresent:
            print("Receiving user is not a registered user. Friend request can't be sent")
            return False
        # check if user to delete is a friend
        if userToDelete.Username not in user.Friends:
            print(f"\n{userToDelete.Username} is not a friend of yours!\n")
            return False
        # check if user to delete is still on pending
        elif user.Friends[userToDelete.Username] == False:
            print(f"\n{userToDelete.Username}'s request is still pending!\n")
            return False

        try:
            del user.Friends[userToDelete.Username]
            new_dict = user.Friends
            database.child(collection).child(user.Id).child("Friends").set(new_dict)
            del userToDelete.Friends[user.Username]
            new_dict = userToDelete.Friends
            database.child(collection).child(userToDelete.Id).child("Friends").set(new_dict)

            print(f"\nYou successfully removed {userToDelete.Username} as a friend\n")
            return True

        except:
            print(f"\nUh Oh! There seemed to be an issue with removing {userToDelete.Username}\n")
            return False
