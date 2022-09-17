import pytest
import time
from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser
from authentication.Signin import LoginUser

""""tests whether it can limit to 5 functions """
def test_RegisterNewUserLimit():
    # make 5 test accounts
    testAccounts = ["testAccount1", "testAccount2", "testAccount3", "testAccount4", "testAccount6"]
    testPwds = ["testPwd1", "testPwd2", "testPwd3", "testPwd4", "testPwd5"]

    print("\nMaking 5 new account's")
    for i in range(len(testAccounts)):
        database.child('Users').push(
            {
                "username": testAccounts[i],
                "password": testPwds[i],
            }
        )
    # check if 6th can be added
    assert RegisterNewUser("testAccount6", "testPwd6!") == False

    #delete the additional accounts
    print("Removing temporary accounts made now")
    queryResults = database.child('Users').get()
    for query in queryResults.each():
        if query.val()['username'] in testAccounts:
            database.child('Users').child(query.key()).remove()

""""Test to see if account is added successfully"""
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


"""Test to test if Log In works"""
def test_LogInUser():
    assert LoginUser("obasit", "0s@masPwd") == True