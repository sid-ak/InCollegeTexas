import pytest
from io import StringIO
import sys
import os
from firebaseSetup.Firebase import database
from authentication.Signin import LoginUser
from model.User import User
from model.Job import Job
from helpers.JobHelpers import JobHelpers
from testInputs.testInputs import set_keyboard_input, get_display_output
from actions.DisplayImpLinks import DisplayImpLinks
from helpers.UserHelpers import UserHelpers
from helpers.FriendHelpers import FriendHelpers
from helpers.AppliedJobHelpers import AppliedJobHelpers
from helpers.SavedJobHelpers import SavedJobHelpers
from model.Profile import Education, Experience, Profile
from model.AppliedJob import AppliedJob
from model.SavedJob import SavedJob
from model.Message import Message
from helpers.MessageHelpers import MessageHelpers
from helpers.UserNotificationHelpers import UserNotificationHelpers
from helpers.JobNotificationHelpers import JobNotificationHelpers
from helpers.APIHelpers import  getCurrentPath
from apis.outputAPIs import UserAPI, UserProfileAPI
from apis.inputAPIs import usersInputAPI
from apis.outputAPIs import createOutputDirectory
from apis.inputAPIs import jobsInputAPI

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
    first_job = Job(job_id, "Test Software Engineer", "Aramark", "coding", "Atlanta", "60000", poster.Id)
    
    assert True == JobHelpers.CreateJob(first_job, "TestJobs")
    
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
    assert True == UserHelpers.DeleteUserAccount(user, "TestUsers")

'''Test to test if Log In works'''
def test_LogInUser():
    set_keyboard_input(["Sid", "Sidharth@7", "-1"])
    loggedInUser = LoginUser()
    assert loggedInUser != None

# EPIC 4: Tests that no more than 10 users can sign up.
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
        assert True == UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user is initialized with a list of empty friends.
def test_UserFriends_InitializedToEmpty():
    # Arrange
    username: str = "testUsername"
    password: str = "testPassword@0"
    userId: str = UserHelpers.CreateUserId(username, password)
    testUser: User = User(userId, username)

    # Act and Assert
    assert testUser.Friends == {}

# EPIC 4: Ensures that a user has pending requests if a friend request is sent.
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
            assert True == UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can accept a friend request as expected.
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
            assert True == UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can reject a friend request as expected.
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
            assert True == UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 4: Ensures that a user can delete a friend as expected.
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
        assert True == UserHelpers.DeleteUserAccount(user, testCollection)

# EPIC 5: Ensures the user can create a profile as expected.
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
        assert True == UserHelpers.DeleteUserAccount(testUser, testCollection)

# EPIC 5: Ensures that user can have a maximum of 3 profile experiences.
def test_UserProfile_ProfileExperiencesLimit():
    testCollection: str = "TestUserProfile"

    # Arrange: Create a user with a profile. Contains one experience.
    test_UserProfile_CreateProfile(deleteTestUser = False)
    username: str = "testUsername0"
    password: str = "testPass0"
    userId: str = UserHelpers.CreateUserId(username, password)
    user: User = User(userId, username)
    testUser: User = UserHelpers.GetUser(user, testCollection)
    assert testUser != None
    assert 1 == len(testUser.Profile.ExperienceList)
    
    # Arrange: Create 2 additional experiences.
    experiences: list[Experience] = []
    i: int = 2 # Initialized to 2 because one experience already exists. 
    while (i < 4):
        experience: Experience = Experience(
            Title = f"Test Title {i}",
            Employer = f"Test Employer {i}",
            DateStarted = f"10/25/2018",
            DateEnded = f"10/25/2018",
            Location = f"Test Location {i}",
            Description = f"Test Description {i}"
        )
        experiences.append(experience)
        i += 1
    
    # Arrange: Update the user with 3 total experiences.
    testUser.Profile.ExperienceList.extend(experiences)
    assert 3 == len(testUser.Profile.ExperienceList)
    assert True == UserHelpers.UpdateUser(testUser, testCollection)

    # Arrange: Make the fourth experience.
    i: int = 4
    fourthExp: Experience = Experience(
        Title = f"Test Title {i}",
        Employer = f"Test Employer {i}",
        DateStarted = f"10/25/2018",
        DateEnded = f"10/25/2018",
        Location = f"Test Location {i}",
        Description = f"Test Description {i}"
    )

    # Assert: Updating the user with fourth profile experience should fail.
    testUser.Profile.ExperienceList.append(fourthExp)
    assert 4 == len(testUser.Profile.ExperienceList)
    assert False == UserHelpers.UpdateUser(testUser, testCollection)

    # Destroy: Delete the test user after the test run.
    assert True == UserHelpers.DeleteUserAccount(testUser, testCollection)

# EPIC 5: Ensures that user can edit a profile as expected.
def test_UserProfile_EditProfile():
    testCollection: str = "TestUserProfile"

    # Arrange: Create a user with a profile. Contains one experience.
    test_UserProfile_CreateProfile(deleteTestUser = False)
    username: str = "testUsername0"
    password: str = "testPass0"
    userId: str = UserHelpers.CreateUserId(username, password)
    user: User = User(userId, username)
    testUser: User = UserHelpers.GetUser(user, testCollection)

    # Arrange: Create some properties needed for the user profile.
    i: int = 1
    title: str = f"Test Title"
    university: str = f"Test University"
    educationList: list[Education] = [Education(
        SchoolName = f"Test School Name {i}",
        Degree = f"Test Degree {i}",
        YearsAttended = 1
    )]

    # Assert: Ensure current properties are as expected.
    assert title == testUser.Profile.Title
    assert university == testUser.Profile.University
    assert educationList == testUser.Profile.EducationList

    # Act: Modify the current properties and update user.
    title = f"Test Title Has Changed"
    university = f"Test University Has Changed"
    educationList = [Education(
        SchoolName = f"Test School Name Has Changed {i}",
        Degree = f"Test Degree Has Changed {i}",
        YearsAttended = 1
    )]
    testUser.Profile.Title = title
    testUser.Profile.University = university
    testUser.Profile.EducationList = educationList
    assert True == UserHelpers.UpdateUser(testUser, testCollection)

    # Assert: Ensure the updated user profile matches with the recent changes.
    testUser = UserHelpers.GetUser(testUser, testCollection)
    assert title == testUser.Profile.Title
    assert university == testUser.Profile.University
    assert educationList == testUser.Profile.EducationList

    # Destroy: Delete the test user after the test run.
    assert True == UserHelpers.DeleteUserAccount(testUser, testCollection)

# EPIC 6: Ensures that user can delete a profile as expected.
def test_DeleteJob():
    #create a job
    poster = User(UserHelpers.CreateUserId("testID", "testPass1!"), "testID", "Test1", "Account1")
    job_id = JobHelpers.CreateJobId("Test IT Intern", "Cummins", "learn the job", "Columbus", "80000")
    first_job = Job(job_id, "Test IT Intern", "Cummins", "learn the job", "Columbus", "80000", poster.Id)
    
    assert True == JobHelpers.CreateJob(first_job, "TestJobs")

    #delete the job
    assert True == JobHelpers.DeleteJob(first_job, "TestJobs")

# EPIC 6: Ensures that user can save a job as expected.
def test_SaveJobs(): 
    #create a job - poster will be different from the user who saves the job
    job_id = JobHelpers.CreateJobId("Test IT Intern", "Cummins", "learn the job", "Columbus", "80000")
    user = User(UserHelpers.CreateUserId("testUserID", "testPass2!"), "testUserID", "Test2", "Account2") #user saving the job
    to_save_job = SavedJob(SavedJobHelpers.CreateSaveJobId(job_id, user.Id), job_id, user.Id)

    #save the job to the user - function call (assert)
    assert True == SavedJobHelpers.CreateSavedJob(to_save_job, user, "TestSavedJobs") #first time saving a job
    assert False == SavedJobHelpers.CreateSavedJob(to_save_job, user, "TestSavedJobs") #saving the job for the second time

    #delete the saved job node
    assert True == SavedJobHelpers.DeleteSavedJob(to_save_job, "TestSavedJobs")

#EPIC 6: Ensures that user can apply to a job as expected.
def test_ApplyForJob():
    #create a job 
    job_id = JobHelpers.CreateJobId("Test IT Intern", "Cummins", "learn the job", "Columbus", "80000")
    user = User(UserHelpers.CreateUserId("testUserID", "testPass2!"), "testUserID", "Test2", "Account2") #user applying
    to_apply_job = AppliedJob(user.Id, job_id, "Test IT Intern", "Cummins", "12/11/22", "01/11/23", "love to work")

    #apply for job - function call (assert)
    assert True == AppliedJobHelpers.CreateAppliedJob(to_apply_job, user, "TestAppliedJobs") #first time applying for the job
    assert False == AppliedJobHelpers.CreateAppliedJob(to_apply_job, user, "TestAppliedJobs") #second time applying for the same job

    #delete the applied job node
    assert True == AppliedJobHelpers.DeleteAppliedJob(to_apply_job, "TestAppliedJobs")

# EPIC 7: Testing receiving and sending message backend functionality
def test_SendMessage():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    user2 = User(UserHelpers.CreateUserId("testUser2", "testPass2!"), "testUserID2", "test2", "test2")
    UserHelpers.UpdateUser(user1, "testUsers")
    UserHelpers.UpdateUser(user2, "testUsers")
    msgId = 1
    test_message = Message(Id=msgId, SenderId=user1.Id, ReceiverId=user2.Id , Content="Hello from the other side!")
    MessageHelpers.UpdateMessage(message=test_message, collection="testMessages", userCollection="testUsers")

    # check if message sent by sender is same as message received by receiver in DB
    retrieved_message = MessageHelpers.GetMessageById(msgId, collection="testMessages")
    assert  test_message == retrieved_message
    # DB clean up
    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    assert True == UserHelpers.DeleteUserAccount(user2, collection="testUsers")
    assert True == MessageHelpers.DeleteMessageById(msgId, collection="testMessages")

# EPIC7: tests the GetAllReceivedMessages function
def test_GetReceivedMessages():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    user2 = User(UserHelpers.CreateUserId("testUser2", "testPass2!"), "testUserID2", "test2", "test2")
    UserHelpers.UpdateUser(user1, "testUsers")
    UserHelpers.UpdateUser(user2, "testUsers")
    sent_messages = []
    for i in range(2):
        test_message = Message(Id=i+1, SenderId=user1.Id, ReceiverId=user2.Id, Content=f"Hello from the other side!{i}")
        MessageHelpers.UpdateMessage(message=test_message, collection="testMessages", userCollection="testUsers")
        sent_messages.append(test_message)

    received_messages = MessageHelpers.GetAllReceivedMessages(user2.Id, messageCollection="testMessages")
    # check if messages sent by sender are same as messages received by receiver in DB
    assert sent_messages == received_messages
    # DB clean up
    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    assert True == UserHelpers.DeleteUserAccount(user2, collection="testUsers")
    for i in range(2):
        assert True == MessageHelpers.DeleteMessageById(i+1, collection="testMessages")

# EPIC8: Testing if a user gets notification if the job they applied to is deleted
def test_DeleteJobNotification():
    poster = User(UserHelpers.CreateUserId("testID", "testPass1!"), "testID", "Test1", "Account1")
    job_id = JobHelpers.CreateJobId("Test IT Intern", "Cummins", "learn the job", "Columbus", "80000")
    first_job = Job(job_id, "Test IT Intern", "Cummins", "learn the job", "Columbus", "80000", poster.Id)

    job_id2 = JobHelpers.CreateJobId("Test IT Intern2", "Cummins2", "learn the job2", "Columbus2", "80001")
    second_job = Job(job_id2, "Test IT Intern2", "Cummins2", "learn the job2", "Columbus2", "80001", poster.Id)

    user2 = User(UserHelpers.CreateUserId("testUser2", "testPass2!"), "testUserID2", "test2", "test2")
    to_apply_job = AppliedJob(user2.Id, job_id, "Test IT Intern", "Cummins", "12/11/22", "01/11/23", "love to work")

    assert True == AppliedJobHelpers.CreateAppliedJob(to_apply_job, user2, "TestAppliedJobs") 
    assert True == JobHelpers.CreateJob(first_job, "TestJobs")
    assert True == JobHelpers.CreateJob(second_job, "TestJobs")
    assert True == JobHelpers.DeleteJob(first_job, "TestJobs")

    set_keyboard_input(["-1"])
    JobNotificationHelpers.NotifyIfAppliedJobsDeleted(user2, appliedJobsCollection="TestAppliedJobs",
    allJobsCollection="TestJobs")
    output = get_display_output()

    assert output == ["\nAttention! Among the jobs you have applied for some have been deleted.",
                      "\nHere they are: \n",
                      "1. Test IT Intern from Cummins",
                      "\nYour applications for these jobs are revoked.\n"]

    assert True == JobHelpers.DeleteJob(second_job, "TestJobs")                                 

#Epic 8: Testing if all the users get a notification when a new user signs up
def test_NewUserNotification():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    UserHelpers.UpdateUser(user1, "testUsers")
    
    user2 = User(UserHelpers.CreateUserId("testUser2", "testPass2!"), "testUserID2", "test2", "test2")
    UserHelpers.UpdateUser(user2, "testUsers")

    output1 = user2._SignUpTimestamp > user1._LastLoginTimestamp
    assert output1 == True

    set_keyboard_input("-1")
    UserNotificationHelpers.NotifyIfNewUsers(user1, collection="testUsers")
    output = get_display_output()

    assert output == ["\ntest2 test2 has joined InCollege."]

    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    assert True == UserHelpers.DeleteUserAccount(user2, collection="testUsers")

#Epic 9: Testing User API function
def test_UserAPI():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    UserHelpers.UpdateUser(user1, "testUsers")
    
    user2 = User(UserHelpers.CreateUserId("testUser2", "testPass2!"), "testUserID2", "test2", "test2")
    UserHelpers.UpdateUser(user2, "testUsers")

    set_keyboard_input("-1")
    
    createOutputDirectory()
    UserAPI(userCollection="testUsers")
    outputDir = os.path.join(getCurrentPath(), "output")
    outputFile = os.path.join(outputDir, "MyCollege_users.txt")

    with open(outputFile, "r") as file:
        output = [line.strip() for line in file]

    
    assert output == ["testUserID1, Standard",
                      "testUserID2, Standard"] 

    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    assert True == UserHelpers.DeleteUserAccount(user2, collection="testUsers")
    os.remove(outputFile)

#function to test UserInputApiFile
def test_UserInputAPI():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    UserHelpers.UpdateUser(user1, "testUsers")

    testInput = os.path.join(getCurrentPath(), "input", "testStudentAccounts.txt")
    with open(testInput, "w") as file:
        file.write("TestUserFile, TestFirstFile, TestLastFile\n")
        file.write("Test123!\n")
        file.write("=====\n")
    
    set_keyboard_input("-1")
    usersInputAPI(userCollection="testUsers", onTest=True)

    outputList = []
    outputList= UserHelpers.GetAllUsers(collection="testUsers")

    output = list(map(lambda user: user.Username, outputList))

    assert output == ["testUserID1",
                      "TestUserFile"] 
    
    
    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    assert True == UserHelpers.DeleteUserAccount(outputList[1], collection="testUsers")
    os.remove(testInput)

#Testing User Profile API function
def test_UserProfileAPI():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    UserHelpers.UpdateUser(user1, "testUsers")
    i: int = 1
    profile: Profile = Profile(
        Id = user1.Id,
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

    user1.Profile = profile
    assert True == UserHelpers.UpdateUser(user1, "testUsers")

    testUserUpdated: User = UserHelpers.GetUser(user1, "testUsers")
    assert testUserUpdated != None
    assert testUserUpdated.Profile == profile

    set_keyboard_input("-1")

    UserProfileAPI(userCollection="testUsers")

    outputFile = os.path.join(getCurrentPath() , "output", "MyCollege_profiles.txt")

    with open(outputFile, "r") as file:
        output = [line.strip() for line in file]

    assert output == ["Test Title",
                      "Test Major",
                      "Test University",
                      "Test About",
                      "Experience:",
                      "1)",
                      "Title: Test Title 1",
                      "Employer: Employer 1",
                      "Date Started: 10/25/2018",
                      "Date Ended: 10/25/2022",
                      "Location: Test Location 1",
                      "Description: Test Description 1",
                      "Education:",
                      "1)",
                      "School Name: Test School Name 1",
                      "Degree: Test Degree 1",
                      "Years Attended: 1",
                      "====="] 

    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers")
    os.remove(outputFile)

# EPIC 10: Tests that the input API for jobs works as expected.
def test_JobsInputAPI():

    # Set the test collection nodes.
    testJobsCollection: str = "TestJobsInputApi"
    testUsersCollection: str = "TestUsersJobsInputApi"

    # Create a test poster/user.
    username: str = "testUsername"
    password: str = "testPass@7"
    userId: str = UserHelpers.CreateUserId(username, password)
    firstName: str = "PosterFirstName"
    lastName: str = "PosterLastName"
    testPoster: User = User(
        userId, username, firstName, lastName)
    UserHelpers.UpdateUser(testPoster, testUsersCollection)

    # Create a test job.
    testJobTitle: str = "New Job Test Title"
    testJobDesc: str = " New Job Test Description"
    testJobPosterId: User = testPoster.Id
    testJobEmpl: str = "New Job Test Employer Name"
    testJobLoc: str = "New Job Test Location"
    testJobSal: str = "New Job Test Salary"
    testJobId: str = JobHelpers.CreateJobId(
        testJobTitle, testJobEmpl, testJobDesc, testJobLoc, testJobSal)
    testJob: Job = Job(
        testJobId, testJobTitle, testJobEmpl, testJobDesc, testJobLoc, testJobSal, testJobPosterId)

    # Set required paths.
    dirPath: str = os.path.join(getCurrentPath(), "input")
    filePath: str = os.path.join(dirPath, "newJobs.txt")

    # Create the appropriate directory if it does not exist.
    if not os.path.exists(dirPath): os.mkdir(dirPath)

    # Prepare the text that needs to be written to the file.
    newJobLines: list[str] = [f"{testJob.Title}\n"]
    newJobLines.append(f"{testJob.Description}\n")
    newJobLines.append("&&&\n")
    newJobLines.append(f"{testPoster.FirstName} {testPoster.LastName}\n")
    newJobLines.append(f"{testJob.Employer}\n")
    newJobLines.append(f"{testJobLoc}\n")
    newJobLines.append(f"{testJobSal}\n")
    newJobLines.append("=====\n")

    # Create, open and write to the file.
    with open(filePath, 'a') as newJobsFile:
        newJobsFile.writelines(newJobLines)
    
    # Call the method under test, input jobs API.
    assert True == jobsInputAPI(testJobsCollection, testUsersCollection)

    # Assert that the job was updated in the DB.
    testJobFromDb: Job = JobHelpers.GetJobByID(testJob.Id, testJobsCollection)

    # Need to compare each property because we want to ignore comparing timestamps.
    assert testJobFromDb.Title == testJob.Title
    assert testJobFromDb.Description == testJob.Description
    assert testJobFromDb.PosterId == testJob.PosterId
    assert testJobFromDb.Employer == testJob.Employer
    assert testJobFromDb.Location == testJob.Location
    assert testJobFromDb.Salary == testJob.Salary
    
    # Delete the lines that were just written to the file.
    with open(filePath, 'r') as newJobsFile:
        jobLines: str = newJobsFile.readlines()
    with open(filePath, 'w') as newJobsFile:
        for line in jobLines:
            if line not in newJobLines:
                newJobsFile.write(line)

    # Delete the test user and test jobs nodes in the DB.
    assert True == UserHelpers.DeleteUserAccount(testPoster, testUsersCollection)
    assert True == JobHelpers.DeleteJob(testJob, testJobsCollection)
