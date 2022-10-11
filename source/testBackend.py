from unicodedata import name
import pytest
from io import StringIO
import sys
from firebaseSetup.Firebase import database
from authentication.Signup import RegisterNewUser, CheckDBSize
from authentication.Signin import LoginUser
from model.User import User, UserHelpers
from model.Job import Job, JobHelpers
from testInputs.testInputs import set_keyboard_input
from actions.DisplayImpLinks import DisplayImpLinks

USER_LIMIT = 10
JOB_LIMIT = 5

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

    if JobHelpers.IsLimitMet():
        assert JobHelpers.CreateJob(first_job, "TestJobs") == False
    else:
        assert JobHelpers.CreateJob(first_job, "TestJobs") == True
        JobHelpers.DeleteJob(first_job, "TestJobs")


def test_JobLimit():
    if len(JobHelpers.GetAllJobs()) >= JOB_LIMIT :
        assert JobHelpers.IsLimitMet() == True
    else:
        assert JobHelpers.IsLimitMet() == False

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
'''tests whether it can limit to 5 functions '''
def test_CheckDBSize():
    # make 5 test accounts
    users = UserHelpers.GetAllUsers()
    if users == None:
        assert CheckDBSize() == True
    elif len(users) >= USER_LIMIT:
        assert CheckDBSize() == False
    else:
        assert CheckDBSize() == True


'''Test to see if account is added successfully'''
def test_RegisterNewUser_Success(monkeypatch):
    set_keyboard_input(["testID", "Mypassword3!", "Test", "Account"])
    user = User(UserHelpers.CreateUserId("testID", "Mypassword3!"), "testID", "Test", "Account")
    result = RegisterNewUser(collection="TestUsers")
    assert result == True
    UserHelpers.DeleteUserAccount(user, "TestUsers")


'''Test to test if Log In works'''
def test_LogInUser():
    set_keyboard_input(["obasit2", "Mypassword3!", "-1"])
    assert LoginUser("TestUsers") == User("4819ac977d1fa72098663c88cbd1c1fdd5da8691a0a07285cc92d05288daf9a9", "obasit2",
                                          "Osama2", "Basit2", True, True, True, "English")
