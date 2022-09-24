import pytest
from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser, CheckDBSize
from authentication.Signin import LoginUser
from model.User import User, UserHelpers

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
def test_RegisterNewUser_Success():
    queryResults = database.child('Users').get()
    if len(queryResults.each()) < 5:
        assert RegisterNewUser("testUser", "testPwd2@") == True
    else:
        queryResults = database.child('Users').get()  # User branch
        userInfo = [(query.val()['username'], query.val()['password']) for query in queryResults.each()]
        temp_username, temp_password = userInfo[4][0], userInfo[4][1]
        for query in queryResults.each():
            if query.val()['username'] == temp_username:
                database.child('Users').child(query.key()).remove()
                print(f"\nremoved {temp_username}")

        assert RegisterNewUser("testUser", "testPwd2@") == True

        queryResults = database.child('Users').get()
        for query in queryResults.each():
            if query.val()['username'] == "testUser":
                database.child('Users').child(query.key()).remove()

        database.child('Users').push({
            "username": temp_username,
            "password": temp_password
        })
        print(f"added {temp_username}")

'''Test to test if Log In works'''
def test_LogInUser():
    assert LoginUser("obasit", "0s@masPwd") == True