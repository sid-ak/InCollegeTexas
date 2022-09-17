import pytest
from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser

def test_RegisterNewUser():
    # make 5 test accounts
    testAccounts = ["testAccount1", "testAccount2", "testAccount3", "testAccount4", "testAccount6"]
    testPwds = ["testPwd1", "testPwd2", "testPwd3", "testPwd4", "testPwd5"]
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
    queryResults = database.child('Users').get()
    for query in queryResults.each():
        if query.val()['username'] in testAccounts:
            database.child('Users').child(query.key()).remove()
