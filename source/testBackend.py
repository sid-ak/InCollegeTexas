import pytest
from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser, CheckDBSize
from authentication.Signin import LoginUser
from model.User import User, UserHelpers
from testInputs.testInputs import set_keyboard_input

#Tests below worked on for EPIC 2
def test_GetAllUsers():
    dbUsersResponse = database.child("Users").get()
    dbUsers = []
    for user in dbUsersResponse.each():
        dbUsers.append(User.HydrateUser(user))

    assert UserHelpers.GetAllUsers() == dbUsers


# Tests below worked on for EPIC 1 - 9/19/22 by Osama
'''tests whether it can limit to 5 functions '''
def test_CheckDBSize():
    # make 5 test accounts
    users = UserHelpers.GetAllUsers()
    if users == None:
        assert CheckDBSize() == True
    elif len(users) >= 5:
        assert CheckDBSize() == False
    else:
        assert CheckDBSize() == True


'''Test to see if account is added successfully'''
def test_RegisterNewUser_Success(monkeypatch):
    set_keyboard_input(["obasit2", "Mypassword3!", "Osama2", "Basit2"])
    RegisterNewUser(collection="TestUsers")
    set_keyboard_input(["testID", "Mypassword3!", "Test", "Account"])
    user = User(UserHelpers.CreateUserId("testID", "Mypassword3!"), "testID", "Test", "Account")
    result = RegisterNewUser(collection="TestUsers")
    assert result == True
    UserHelpers.DeleteUserAccount(user, "TestUsers")


'''Test to test if Log In works'''
def test_LogInUser():
    set_keyboard_input(["obasit2", "Mypassword3!", "-1"])
    assert LoginUser("TestUsers") == User("4819ac977d1fa72098663c88cbd1c1fdd5da8691a0a07285cc92d05288daf9a9", "obasit2",
                                          "Osama2", "Basit2")
