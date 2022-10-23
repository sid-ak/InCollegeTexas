import pytest
from io import StringIO
import sys
from firebaseSetup.Firebase import database
from authentication.Signin import LoginUser
from model.User import User
from model.Job import Job, JobHelpers
from testInputs.testInputs import set_keyboard_input
from actions.DisplayImpLinks import DisplayImpLinks
from helpers.UserHelpers import UserHelpers
from helpers.FriendHelpers import FriendHelpers
from model.Profile import Education, Experience, Profile

# Below Tests are for Epic 3 - 10/08/2022 by Amir
'''Test to see all "Important Links" are displayed'''
def test_ImportantLinksDisplay():
    # test that "Copyright" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=1)
    sys.stdout = sys.__stdout__
    assert "Copyright" in capturedOutput.getvalue()

    # test that "About" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=2)
    sys.stdout = sys.__stdout__
    assert "About" in capturedOutput.getvalue()

    # test that "Accessibility" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=3)
    sys.stdout = sys.__stdout__
    assert "Accessibility" in capturedOutput.getvalue()

    # test that "User Agreement" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=4)
    sys.stdout = sys.__stdout__
    assert "User Agreement" in capturedOutput.getvalue()

    # test that "Privacy Policy" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=5)
    sys.stdout = sys.__stdout__
    assert "Privacy Policy" in capturedOutput.getvalue()

    # test that "Cookie Policy" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=6)
    sys.stdout = sys.__stdout__
    assert "Cookie Policy" in capturedOutput.getvalue()

    # test that "Copyright Policy" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=7)
    sys.stdout = sys.__stdout__
    assert "Copyright Policy" in capturedOutput.getvalue()

    # test that "Brand Policy" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=8)
    sys.stdout = sys.__stdout__
    assert "Brand Policy" in capturedOutput.getvalue()

    # test that "Guest Controls" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=5)
    sys.stdout = sys.__stdout__
    assert "Guest Controls" in capturedOutput.getvalue()

    # test that "Language Preferences" link is displayed
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=9)
    sys.stdout = sys.__stdout__
    assert "Language Preference" in capturedOutput.getvalue()

'''Test ensure if Privacy Policy is selected, the user will be provided with an additional option: "Guest Controls'''
def test_GuestControlsAfterPrivacy():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=5)
    sys.stdout = sys.__stdout__
    assert "Additional options" in capturedOutput.getvalue() and "1 - Guest Controls" in capturedOutput.getvalue()

'''Test that Guest Controls will provide a user with the ability to individually turn off 
the InCollege Email, SMS, and Targeted Advertising features'''
def test_GuestControlsTogglers():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=5)
    sys.stdout = sys.__stdout__

    assertOutput = ["Select an option to toggle it on or off:", "InCollege Email", "SMS", "Targeted Advertising"]

    for assertItem in assertOutput:
        assert assertItem in capturedOutput.getvalue()

'''Test to ensure a new user has the settings ^ turned on'''
def test_NewUserControlsOn():
    # create a dummy new user
    newUser = User(Id="TestID", Username="TestUserName")

    assert newUser.EmailEnabled
    assert newUser.SmsEnabled
    assert newUser.TargetedAdvertEnabled

'''Test ensure if the user is logged in, selecting the Languages option will allow a 
user to select between English and Spanish'''
def test_LanguagePreferencesEnglishSpanish():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    DisplayImpLinks(onTest=True, testInput=9)
    sys.stdout = sys.__stdout__

    assertOutput = ["Select an option to set your preferred language:", "English", "Spanish"]

    for assertItem in assertOutput:
        assert assertItem in capturedOutput.getvalue()

'''Test to ensure a new user has language set to “English”'''
def test_NewUserEnglishSet():
    # create a dummy new user
    newUser = User(Id="TestID", Username="TestUserName")

    assert str(newUser.LanguagePreference.value) == '(1,)'

#Tests below worked on for EPIC 2
def test_CreateJob():
    poster = User(UserHelpers.CreateUserId("testID", "Mypassword3!"), "testID", "Test", "Account")
    job_id = JobHelpers.CreateJobId("Test Software Engineer", "Aramark", "coding", "Atlanta", "60000")
    first_job = Job(job_id, "Test Software Engineer", "Aramark", "coding", "Atlanta", "60000", poster)

    if JobHelpers.IsJobLimitMet():
        assert JobHelpers.CreateJob(first_job, "TestJobs") == False
    else:
        assert JobHelpers.CreateJob(first_job, "TestJobs") == True
        JobHelpers.DeleteJob(first_job, "TestJobs")

def test_JobLimit():
    if len(JobHelpers.GetAllJobs()) >= JobHelpers._jobLimit:
        assert JobHelpers.IsJobLimitMet() == True
    else:
        assert JobHelpers.IsJobLimitMet() == False

def test_GetAllJobs():
    dbJobsResponse = database.child("Jobs").get()
    dbJobs = []
    for job in dbJobsResponse.each():
        dbJobs.append(Job.HydrateJob(job))

    assert JobHelpers.GetAllJobs() == dbJobs

def test_GetAllUsers():
    dbUsersResponse = database.child("Users").get()
    dbUsers = []
    for user in dbUsersResponse.each():
        dbUsers.append(User.HydrateUser(user))

    assert UserHelpers.GetAllUsers() == dbUsers

# Tests below worked on for EPIC 1 - 9/19/22 by Osama
'''Test to see if account is added successfully'''
def test_RegisterNewUser_Success():
    user = User(UserHelpers.CreateUserId("testID", "Mypassword3!"), "testID")
    result = UserHelpers.UpdateUser(user, "TestUsers")
    assert result == True
    UserHelpers.DeleteUserAccount(user, "TestUsers")

'''Test to test if Log In works'''
def test_LogInUser():
    set_keyboard_input(["Sid", "Sidharth@7", "-1"])
    loggedInUser = LoginUser()
    assert loggedInUser != None

# EPIC 4: Tests that no more than 10 users can sign up. (Sid)
def test_UserLimit():
    # Arrange: Set collection to insert into an user limit.
    testCollection: str = "TestUsersOverLimit"
    users: list[User] = []
    userLimit: int = UserHelpers._userLimit
    
    # Arrange: Initialize required fields to create a user.
    i: int = 0
    while (i < userLimit):
        username: str = f"testUser{i}"
        password: str = f"testPassword@{i}"
        userId: str = UserHelpers.CreateUserId(username, password)
        firstName: str = f"testFirstName{i}"
        lastName: str = f"testLastName{i}"

        user: User = User(
            userId,
            username,
            firstName,
            lastName)
        
        # Act and Assert: Insert user until max count.
        assert True == UserHelpers.UpdateUser(user, testCollection)
        users.append(user)
        i += 1
    
    # Arrange: Create a user that is over the limit.
    exceededUserLimit = userLimit
    username: str = f"testUserOverLimit{exceededUserLimit}"
    password: str = f"testPassword@{exceededUserLimit}"

    userOverLimit: User = User(
        UserHelpers.CreateUserId(username, password),
        username,
        f"testFirstName{exceededUserLimit}",
        f"testLastName{exceededUserLimit}"
    )

    # Act and Assert: Inserting a user over the limit should fail.
    assert False == UserHelpers.UpdateUser(userOverLimit, testCollection)

    # Destroy: Delete all test users after the test run.
    for user in users:
        UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user is initialized with a list of empty friends. (Sid)
def test_UserFriends_InitializedToEmpty():
    # Arrange
    username: str = "testUsername"
    password: str = "testPassword@0"
    userId: str = UserHelpers.CreateUserId(username, password)
    testUser: User = User(userId, username)

    # Act and Assert
    assert testUser.Friends == {}

# EPIC 4: Ensures that a user has pending requests if a friend request is sent. (Sid)
def test_UserFriends_SendFriendRequest(deleteTestUsers: bool = True):
    # Arrange
    testCollection: str = "TestUsers"
    users: list[User] = []

    # Arrange: Create two users.
    i: int = 0
    while (i < 2):
        username: str = f"testUsername{i}"
        password: str = f"testPassword@{i}"
        userId: str = UserHelpers.CreateUserId(username, password)
        user: User = User(userId, username)

        UserHelpers.UpdateUser(user, testCollection)
        users.append(user)
        i += 1
    
    # Act and Assert: Ensure that the friend request gets sent successfully.
    user1: User = users[0]
    user2: User = users[1]
    assert FriendHelpers.SendFriendRequest(user1, user2, testCollection) == True

    # Act and Assert: Ensure that the friend request was received and is pending.
    testUser2: User = UserHelpers.GetUser(user2, testCollection)
    assert testUser2.Friends["testUsername0"] == False

    # Destroy: Delete all test users after the test run.
    if deleteTestUsers:
        for user in users:
            UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can accept a friend request as expected. (Sid)
def test_UserFriends_AcceptFriendRequest(deleteTestUsers: bool = True):
    testCollection: str = "TestUsers"

    # Arrange: Create test users and send a friend request.
    test_UserFriends_SendFriendRequest(deleteTestUsers=False)
    
    users: list[User] = UserHelpers.GetAllUsers(testCollection)
    for user in users:
        if user.Username == "testUsername0": user1: User = user
        if user.Username == "testUsername1": user2: User = user
    
    # Act and Assert: Ensure a user can accept a friend request successfully.
    assert FriendHelpers.AcceptFriendRequest(user2, user1, testCollection) == True

    # Assert: Ensure the receiver now has the receiver as a friend.
    testUser2: User = UserHelpers.GetUser(user2, testCollection)
    assert testUser2.Friends["testUsername0"] == True

    # Assert: Ensure that the sender has the receiver as a friend to confirm mutuality.
    testUser1: User = UserHelpers.GetUser(user1, testCollection)
    assert testUser1.Friends["testUsername1"] == True

    # Destroy: Delete all test users after the test run.
    if deleteTestUsers:
        for user in users:
            UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can reject a friend request as expected. (Sid)
def test_UserFriends_RejectFriendRequest():
    testCollection: str = "TestUsers"

    # Arrange: Create test users and send a friend request.
    test_UserFriends_SendFriendRequest(deleteTestUsers=False)
    
    users: list[User] = UserHelpers.GetAllUsers(testCollection)
    for user in users:
        if user.Username == "testUsername0": user1: User = user
        if user.Username == "testUsername1": user2: User = user
    
    # Act and Assert: Ensure a user can reject a friend request successfully.
    assert FriendHelpers.RejectFriendRequest(user2, user1, testCollection) == True

    # Assert: Accessing a rejected friend request should result in a key error.
    testUser2: User = UserHelpers.GetUser(user2, testCollection)
    with pytest.raises(KeyError): # Verify that a KeyError exception is raised.
        testUser2.Friends["testUsername0"]
    
    # Assert: Ensure mutuality.
    testUser1: User = UserHelpers.GetUser(user1, testCollection)
    with pytest.raises(KeyError): # Verify that a KeyError exception is raised.
        testUser1.Friends["testUsername1"] 

    # Destroy: Delete all test users after the test run.
        for user in users:
            UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can delete a friend as expected. (Sid)
def test_UserFriends_DeleteFriend():
    testCollection: str = "TestUsers"

    # Arrange: Create test users, send and accept a friend request.
    test_UserFriends_AcceptFriendRequest(deleteTestUsers=False)
    
    users: list[User] = UserHelpers.GetAllUsers(testCollection)
    for user in users:
        if user.Username == "testUsername0": user1: User = user
        if user.Username == "testUsername1": user2: User = user
    
    # Act and Assert: Ensure a user can delete a friend successfully.
    assert FriendHelpers.DeleteFriend(user2, user1, testCollection) == True

    # Assert: Accessing a deleted friend should result in a key error.
    testUser2: User = UserHelpers.GetUser(user2, testCollection)
    with pytest.raises(KeyError): # Verify that a KeyError exception is raised.
        testUser2.Friends["testUsername0"]

    # Assert: Ensure mutuality.
    testUser1: User = UserHelpers.GetUser(user1, testCollection)
    with pytest.raises(KeyError): # Verify that a KeyError exception is raised.
        testUser1.Friends["testUsername1"]

    # Destroy: Delete all test users after the test run.
    for user in users:
        UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 5: Ensures the user can create a profile as expected. (Sid)
def test_UserProfile_CreateProfile(deleteTestUser: bool = True):
    # Arrange: Create a user under the TestUserProfile node.
    testCollection: str = "TestUserProfile"
    username: str = "testUsername0"
    password: str = "testPass0"
    userId: str = UserHelpers.CreateUserId(username, password)
    user: User = User(userId, username)
    
    # Assert: Ensure default value of a profile on construction of a user is set to None.
    assert user.Profile == None
    assert True == UserHelpers.UpdateUser(user, testCollection)

    # Arrange: Get the user that was just created and pushed to the DB.
    testUser: User = UserHelpers.GetUser(user, testCollection)
    assert testUser != None

    # Arrange: Instantiate a profile.
    i: int = 1
    profile: Profile = Profile(
        Id = testUser.Id,
        Title = "Test Title",
        University = "Test University",
        Major = "Test Major",
        About = "Test About",
        EducationList = [Education(
            SchoolName = f"Test School Name {i}",
            Degree = f"Test Degree {i}",
            YearsAttended = 1
        )],
        ExperienceList = [Experience(
            Title = f"Test Title {i}",
            Employer = f"Employer {i}",
            DateStarted = "10/25/2018",
            DateEnded = "10/25/2022",
            Location = f"Test Location {i}",
            Description = f"Test Description {i}"
        )]
    )

    # Arrange: Assign the newly instantiated profile to the test user and update.
    testUser.Profile = profile
    assert True == UserHelpers.UpdateUser(testUser, testCollection)

    # Assert: Retrieve the user and confirm the profile changes match.
    testUserUpdated: User = UserHelpers.GetUser(testUser, testCollection)
    assert testUserUpdated != None
    assert testUserUpdated.Profile == profile

    # Destroy: Delete the test user after the test run.
    if (deleteTestUser):
        UserHelpers.DeleteUserAccount(testUser, testCollection)
