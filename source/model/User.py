from dataclasses import dataclass, field
from typing import Dict
import hashlib
from firebaseSetup.Firebase import database
from enums.LanguageEnum import LanguageEnum


# A User entity.
@dataclass
class User:
    Id: str
    Username: str
    FirstName: str = ""
    LastName: str = ""
    EmailEnabled: bool = True
    SmsEnabled: bool = True
    TargetedAdvertEnabled: bool = True
    LanguagePreference: LanguageEnum = LanguageEnum.English
    Friends: Dict[str, bool] = field(default_factory=dict)
    University: str = ""
    Major: str = ""

    # Hydrates a User entity using a pyrebase response value and returns it.
    def HydrateUser(user, collection: str = "Users"):
        try:
            friends = user.val()["Friends"]
        except:
            friends = {}

        return User(
                Id = user.val()["Id"],
                Username = user.val()["Username"],
                FirstName = user.val()["FirstName"],
                LastName = user.val()["LastName"],
                EmailEnabled = user.val()["EmailEnabled"],
                SmsEnabled = user.val()["SmsEnabled"],
                TargetedAdvertEnabled = user.val()["TargetedAdvertEnabled"],
                LanguagePreference = user.val()["LanguagePreference"],
                Friends = friends,
                University = user.val()["University"],
                Major = user.val()["Major"]
            )

class UserHelpers:
    _userLimit: int = 10

    # Converts this entity into a dictionary
    def UserToDict(user: User) -> dict:
        return {
            'Id': str(user.Id),
            'Username': str(user.Username),
            'FirstName': str(user.FirstName),
            'LastName': str(user.LastName),
            'EmailEnabled': str(user.EmailEnabled),
            'SmsEnabled': str(user.SmsEnabled),
            'TargetedAdvertEnabled': str(user.TargetedAdvertEnabled),
            'LanguagePreference': str(user.LanguagePreference),
            'Friends': user.Friends,
            'University': str(user.University),
            'Major': str(user.Major)
        }

    # Gets a PyreResponse of all users from the DB and returns
    # a list of User entities after constructing it.
    def GetAllUsers(collection: str = "Users") -> list[User]:
        try:
            usersResponse = database.child(collection).get()
            if usersResponse == None: return None

            userResponseList: list = usersResponse.each()
            if (userResponseList == None): return None

            users: list[User] = []
            for user in usersResponse.each():
                if user == None: continue
                else: users.append(User.HydrateUser(user))

            return users
        except:
            return None

    # Gets a specific User from the database based on the user object provided.
    def GetUser(user: User, collection: str = "Users") -> User:
        try:
            user: User = User.HydrateUser(
                database.child(collection).child(user.Id).get())
            
            if user == None:
                raise Exception(
                    f"Could not get the specified user with username: {user.Username}")
            
            return user
        except:
            print(f"Could not get the specified user with username: {user.Username}")

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

    # Creates the specified user in the DB.
    # Takes an optional argument for the child node in the DB.
    # Return true if creation was successful.
    def UpdateUser(user: User, collection: str = "Users") -> bool:
        try:
            if (UserHelpers.IsUserLimitMet(collection)):
                return False

            database.child(collection).child(
                user.Id).set(UserHelpers.UserToDict(user))
            return True
        except:
            return False

    # Creates a sha256 hash using the username and password.
    # Used as a unique UserId.
    def CreateUserId(username: str, password: str) -> str:
        return hashlib.sha256(
            str.encode(username.join(password))).hexdigest()

    # Deletes a user account.
    def DeleteUserAccount(user: User, collection: str = "Users") -> bool:
        users = UserHelpers.GetAllUsers(collection=collection)
        if (users != None):
            # now check that the username is unique
            for dbUser in users:
                if user.Username == dbUser.Username:
                    database.child(collection).child(user.Id).remove()
                    return True
        else:
            return False

    # Toggles the email preference for a user.
    def ToggleEmailEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.EmailEnabled = not user.EmailEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nEmail Enabled: {user.EmailEnabled}")
        except:
            print("Exception occurred. Email preference could not be toggled.")

    # Toggles the sms preference for a user.
    def ToggleSmsEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.SmsEnabled = not user.SmsEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nSMS Enabled: {user.SmsEnabled}")
        except:
            print("Exception occurred. SMS preference could not be toggled.")

    # Toggles the advertising preference for a user.
    def ToggleTargetedAdvertEnabled(user: User, collection: str = "Users"):
        try:
            if user == None: return

            user.TargetedAdvertEnabled = not user.TargetedAdvertEnabled
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nTargeted Advertising Enabled: {user.TargetedAdvertEnabled}")
        except:
            print("Exception occurred. Targeted Advertising preference could not be toggled.")

    # Sets the preferred language for a user as specified.
    def SetLangPreference(user: User, language: LanguageEnum, collection: str = "Users"):
        try:
            if user == None: return

            user.LanguagePreference = language
            updatedUser: bool = UserHelpers.UpdateUser(user, collection)

            if updatedUser == True:
                print(f"\nPreferred language set to: {user.LanguagePreference.name}")
        except:
            print("Exception occurred. Targeted Advertising preference could not be toggled.")

    # helper to check if a given user is present in the db
    def CheckUserPresenceInDB(userToCheck: User, collection: str = "Users") -> bool:
        dbusers = UserHelpers.GetAllUsers(collection)
        for user in dbusers:
            if userToCheck.Username == user.Username:
                return True
        return False

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
            print(f"\nUh Oh! {userToReject.Username} isn't a friend friend\n")
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

    # Checks if the maximum number of jobs have been posted.
    def IsUserLimitMet(collection: str = "Users") -> bool:
        allUsers: list[User] = UserHelpers.GetAllUsers(collection)
        
        if allUsers == ([] or None):
            return False
        
        return True if len(allUsers) == UserHelpers._userLimit else False
    
    def SearchByAttribute(attribute: str, value: str, collection: str = "Users") -> list:
        try:
            users = UserHelpers.GetAllUsers(collection)
            results = []
            for user in users:
                if getattr(user, attribute) == value:
                    results.append(user)
            return results
        except:
            print("\nUh Oh! Something went wrong while searching for users\n")
            return []
