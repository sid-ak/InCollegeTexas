from authentication.Signup import ValidatePassword
from authentication.Signin import DisplayLoginMenu
from actions.LearnNewSkill import DisplaySkills
from actions.FindSomeone import FindSomeoneAction
from actions.PlayVideo import PlayVideo
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from actions.SearchUsers import SearchUsers,FriendRequest
from actions.DisplayPendingRequests import DisplayPendingRequests
from actions.ShowMyNetwork import ShowMyNetwork
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from helpers.ProfileHelpers import ProfileHelpers
from helpers.FriendHelpers import FriendHelpers
from testInputs.testInputs import set_keyboard_input
from testInputs.testInputs import get_display_output
from helpers.UserHelpers import UserHelpers
from model.User import User
from model.Job import Job
from helpers.JobHelpers import JobHelpers
from helpers.JobTitleHelper import JobTitleHelper
from actions.DisplayAllUser import DisplayEveryUser
from helpers.MessageHelpers import MessageHelpers
from model.Message import Message
from actions.ShowInbox import ShowInbox
from helpers.UserNotificationHelpers import UserNotificationHelpers


# Tests below worked on for EPIC 2
def test_PlayVideo(capfd):
    PlayVideo()
    out, err = capfd.readouterr()
    assert out == "Video is now playing!\n"

# Tests below worked on for EPIC 1 - 9/19/22 by Anshika
def test_ValidatePassword():
    good_pwd = ["Test123@", "Testing1234@"]
    for pwd in good_pwd:
        assert ValidatePassword(pwd) == True

    bad_pwd = ["Test123", "test123@", "Test@One", "Test123@test1"]
    for pwd in bad_pwd:
        assert ValidatePassword(pwd) == False

def test_DisplaySkills(capfd):
    skills = ['communication', 'marketing', 'python programming', 'web development', 'public speaking']
    DisplaySkills(skills)
    out, err = capfd.readouterr()
    assert out == "1. Communication\n2. Marketing\n3. Python Programming\n4. Web Development\n5. Public Speaking\n"

def test_FindSomeone(capfd):
    FindSomeoneAction()
    out, err = capfd.readouterr()
    assert out == "under construction\n"

# TESTS BELOW FOR EPIC 3 BY AOUN - 10/08/2022

# Test to see if all Useful link works below
def test_UsefulLinksDisplay():
    set_keyboard_input(["-1"])
    DisplayUsefulLinks()
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - General",
                        "2 - Browse InCollege",
                        "3 - Business Solutions",
                        "4 - Directories",
                        "\nEnter (-1 to exit current menu): "
                      ]

    set_keyboard_input(["2", "-1"])
    DisplayUsefulLinks()
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): ",
                     "under construction",
                     "\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): "]

    set_keyboard_input(["3", "-1"])
    DisplayUsefulLinks()
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): ",
                     "under construction",
                     "\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): "]

    set_keyboard_input(["4", "-1"])
    DisplayUsefulLinks()
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): ",
                     "under construction",
                     "\nPlease select one of the following links to display its content:",
                     "1 - General",
                     "2 - Browse InCollege",
                     "3 - Business Solutions",
                     "4 - Directories",
                     "\nEnter (-1 to exit current menu): "]

def test_GeneralSetting():
    set_keyboard_input(["1", "o", "o", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    if UserHelpers.IsUserLimitMet():
      assert output == ["\nPlease select one of the following links to display its content:",
                          "1 - Sign Up",
                          "2 - Help Center",
                          "3 - About",
                          "4 - Press",
                          "5 - Blog",
                          "6 - Careers",
                          "7 - Developers",
                          "\nEnter (-1 to exit current menu): ",
                          "\nSignup Selected.",
                          "\nAll permitted accounts have been created, please come back later!",
                          "\nPlease select one of the following links to display its content:",
                          "1 - Sign Up",
                          "2 - Help Center",
                          "3 - About",
                          "4 - Press",
                          "5 - Blog",
                          "6 - Careers",
                          "7 - Developers",
                          "\nEnter (-1 to exit current menu): ",
                          "Unexpected exception ocurred, invalid input.\nPlease enter a number between 1 and 7.\n",
                          "\nPlease select one of the following links to display its content:",
                          "1 - Sign Up",
                          "2 - Help Center",
                          "3 - About",
                          "4 - Press",
                          "5 - Blog",
                          "6 - Careers",
                          "7 - Developers",
                          "\nEnter (-1 to exit current menu): ",
                          "Unexpected exception ocurred, invalid input.\nPlease enter a number between 1 and 7.\n",
                          "\nPlease select one of the following links to display its content:",
                          "1 - Sign Up",
                          "2 - Help Center",
                          "3 - About",
                          "4 - Press",
                          "5 - Blog",
                          "6 - Careers",
                          "7 - Developers",
                          "\nEnter (-1 to exit current menu): "
                        ]
    else:
      assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nEnter (-1 to exit current menu): ",
                        "\nSignup Selected.",
                        "\nPlease enter your username: ",
                        "\nPlease enter your password: ",
                        "\nError! Your password does not meet one or some of the standards!",
                        "\nFailure! We have not been able to create a new account for you.",
                        "\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nEnter (-1 to exit current menu): "
                      ]

    set_keyboard_input(["2", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nEnter (-1 to exit current menu): ",
                        "\nWe're here to help",
                        "\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nEnter (-1 to exit current menu): "
                      ]

    set_keyboard_input(["3", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ['\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): ',
                         '\n'
                         'In College:\n'
                         "Welcome to In College, the world's largest college student network\n"
                         'with many users in many countries and territories worldwide',
                         '\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): '
                      ]

    set_keyboard_input(["4", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ['\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): ',
                         '\n'
                         'In College Pressroom:\n'
                         'Stay on top of the latest news, updates, and reports',
                         '\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): '
                      ]

    set_keyboard_input(["5", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ['\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): ',
                         'under construction',
                         '\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): '
                      ]

    set_keyboard_input(["6", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ['\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): ',
                         'under construction',
                         '\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): '
                      ]

    set_keyboard_input(["7", "-1"])
    DisplayUsefulLinksHelpers.General()
    output = get_display_output()
    assert output == ['\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): ',
                         'under construction',
                         '\nPlease select one of the following links to display its content:',
                         '1 - Sign Up',
                         '2 - Help Center',
                         '3 - About',
                         '4 - Press',
                         '5 - Blog',
                         '6 - Careers',
                         '7 - Developers',
                         '\nEnter (-1 to exit current menu): '
                      ]

def test_SearchUsersLastName():
  set_keyboard_input(["1" ])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by last name.\nEnter the last name of the user you want to search for: ",
                    "Unexpected error ocurred\n",
                    ]

def test_SearchUsersLastName2():
  set_keyboard_input(["1", "Bhowmick"])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by last name.\nEnter the last name of the user you want to search for: ",
                    "1. Anshika Bhowmick\n",
                    "Enter the option number of the user you want to send a friend request to: ",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                  ]

def test_SearchUsersUniversity():
  set_keyboard_input(["2"])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by university.\nEnter the university of the user you want to search for: ",
                    "Unexpected error ocurred\n",
                  ]
  
  set_keyboard_input(["2","TestUniversity", "-1"])
  testUser = User(Id='testId',Username='testUsername',FirstName='TestFirstName',LastName='TestLastName',
                  University='TestUniversity', Major='major')
  UserHelpers.UpdateUser(testUser, collection="TestUsers")
  SearchUsers(collection="TestUsers")
  output = get_display_output()
  assert output == ['\nPlease select one of the following options:\n',
                     '1 - Search by last name',
                     '2 - Search by university',
                     '3 - Search by major',
                     '\nEnter (-1 to exit current menu): ',
                     'You have selected to search by university.\n'
                     'Enter the university of the user you want to search for: ',
                     '1. TestFirstName TestLastName\n',
                     'Enter the option number of the user you want to send a friend request to: ',
                     '\nEnter (-1 to exit current menu): ',
                     '\nPlease select one of the following options:\n',
                     '1 - Search by last name',
                     '2 - Search by university',
                     '3 - Search by major',
                     '\nEnter (-1 to exit current menu): ',
                     'Unexpected error ocurred\n'
                  ]
  UserHelpers.DeleteUserAccount(testUser, collection="TestUsers")

def test_SearchUsersMajor():
  set_keyboard_input(["3", "-1"])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by major.\nEnter the major of the user you want to search for: ",
                    "Enter the option number of the user you want to send a friend request to: ",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n",
                  ]
  
  set_keyboard_input(["3", "major", "-1"])
  testUser = User(Id='testId', Username='testUsername', FirstName='TestFirstName', LastName='TestLastName',
                  University='TestUniversity', Major='major')
  UserHelpers.UpdateUser(testUser, collection="TestUsers")
  SearchUsers(collection="TestUsers")
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by major.\nEnter the major of the user you want to search for: ",
                    '1. TestFirstName TestLastName\n',
                    'Enter the option number of the user you want to send a friend request to: ',
                    "\nEnter (-1 to exit current menu): ",
                    "\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                  ]
  UserHelpers.DeleteUserAccount(testUser, collection="TestUsers")

def test_sendFriendRequest():
  set_keyboard_input(["1", "-1"])
  FriendRequest()
  output = get_display_output()
  assert output == ["Do you want to send a friend request?:\n",
                    "1 - Yes",
                    "2 - No",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                    ]

  set_keyboard_input(["2", "-1"])
  FriendRequest()
  output = get_display_output()
  assert output == ["Do you want to send a friend request?:\n",
                    "1 - Yes",
                    "2 - No",
                    "\nEnter (-1 to exit current menu): ",
                    ]

def test_DisplayPendingRequest():
  set_keyboard_input(["1"])
  testUser = User(Id='testId', Username='testUsername', FirstName='TestFirstName', LastName='TestLastName',
                  University='TestUniversity', Major='major')
  UserHelpers.UpdateUser(testUser, collection="TestUsers")
  users = UserHelpers.GetAllUsers(collection="TestUsers")

  for user in users:
    if user.Username == "testUsername":
      DisplayPendingRequests(user, collection="TestUsers")
  output = get_display_output()
  assert output == ["Your pending requests:\n",
                    "You have no pending requests.\n"]

  set_keyboard_input(["2", "-1"])
  users = UserHelpers.GetAllUsers(collection="TestUsers")
  for user in users:
      if user.Username == "testUsername":
          DisplayPendingRequests(user, collection="TestUsers")
  output = get_display_output()
  assert output == ["Your pending requests:\n",
                    "You have no pending requests.\n"]

  UserHelpers.DeleteUserAccount(testUser, collection="TestUsers")

def test_ShowYourNetwork():
  set_keyboard_input([])
  testUser = User(Id='testId', Username='testUsername', FirstName='TestFirstName', LastName='TestLastName',
                  University='TestUniversity', Major='major')
  UserHelpers.UpdateUser(testUser, collection="TestUsers")
  users = UserHelpers.GetAllUsers(collection="TestUsers")

  for user in users:
    if user.Username == "testUsername":
      ShowMyNetwork(user)
  output = get_display_output()
  assert output == ['\nYour network:\n', 'You have no friends yet.\n']

  UserHelpers.DeleteUserAccount(testUser, collection="TestUsers")

# checking if university and major are displayed in title case
def test_TitleCaseUniversity():
  output = ProfileHelpers.ToTitleFormat("university of south florida")
  assert output == "University Of South Florida"

  output = ProfileHelpers.ToTitleFormat("computer science")
  assert output == "Computer Science"

# EPIC 6 - Test for displaying jobs - by Osama Basit
def test_DisplayJobTitle():
    testUser = User(Id='testId', Username='testUsername', FirstName='TestFirstName', LastName='TestLastName',
                    University='TestUniversity', Major='major')
    UserHelpers.UpdateUser(testUser, "testUsers")

    title = "testTitle"
    employer = "testEmployer"
    desc = "testDecsription"
    loc = "testLocation"
    salary = "100000"
    job_id = JobHelpers.CreateJobId(title, employer, desc, loc, salary)
    test_job = Job(job_id, title, employer, desc, loc, salary, testUser.Id)
    JobHelpers.CreateJob(test_job, collection="testJobs")

    # testing view all jobs titles option inside display job menu
    set_keyboard_input(["2", "-1", "-1"])
    JobTitleHelper.DisplayJobTitle(testUser, "testJobs")
    output = get_display_output()

    assert output == ['\nPlease select if you want to filter the Job:\n',
                      '1 - Yes',
                      '2 - No',
                      '\nEnter (-1 to exit current menu): ',
                      '\nSelect one of the following jobs to continue:\n',
                      '1 - testTitle',
                      '\nEnter (-1 to exit current menu): ',
                      '\nPlease select if you want to filter the Job:\n',
                      '1 - Yes',
                      '2 - No',
                      '\nEnter (-1 to exit current menu): '
                    ]

    # testing select a job option (apply, save and delete) menu inside Display Job Titles
    set_keyboard_input(["2", "1", "-1", "-1", "-1"])
    JobTitleHelper.DisplayJobTitle(testUser, "testJobs", "testUsers")
    output = get_display_output()
    assert output == ['\nPlease select if you want to filter the Job:\n',
                         '1 - Yes',
                         '2 - No',
                         '\nEnter (-1 to exit current menu): ',
                         '\nSelect one of the following jobs to continue:\n',
                         '1 - testTitle',
                         '\nEnter (-1 to exit current menu): ',
                         '\nJob Title: testTitle',
                         'Job Description: testDecsription',
                         'Employer: testEmployer',
                         'Job Location: testLocation',
                         'Job Salary: 100000\n',
                         '\nPlease select one of the following options:\n',
                         '1 - Apply for the job',
                         '2 - Save the job',
                         '3 - Unsave the job',
                         '4 - Delete job',
                         '\nEnter (-1 to exit current menu): ',
                         '\nSelect one of the following jobs to continue:\n',
                         '1 - testTitle',
                         '\nEnter (-1 to exit current menu): ',
                         '\nPlease select if you want to filter the Job:\n',
                         '1 - Yes',
                         '2 - No',
                         '\nEnter (-1 to exit current menu): '
                      ]

    # testing filter option inside Dsiplay job menu
    set_keyboard_input(["1", "-1", "-1"])
    JobTitleHelper.DisplayJobTitle(testUser, "testJobs")
    output = get_display_output()

    assert output == ['\nPlease select if you want to filter the Job:\n',
                         '1 - Yes',
                         '2 - No',
                         '\nEnter (-1 to exit current menu): ',
                         '\nPlease select one of the following options:\n',
                         '1 - Show applied jobs',
                         '2 - Show unapplied jobs',
                         '3 - Show saved Jobs',
                         '\nEnter (-1 to exit current menu): ',
                         '\nPlease select if you want to filter the Job:\n',
                         '1 - Yes',
                         '2 - No',
                         '\nEnter (-1 to exit current menu): '
                      ]

    JobHelpers.DeleteJob(test_job, collection="testJobs")
    UserHelpers.DeleteUserAccount(testUser, "testUsers")

# EPIC 7 - 10/06/2022 by Amir Aslamov
# test the list of friends
def test_DisplayListFriends():
  # first create 2 test user friends
  testFriend1 = User(Id='testIdEpic7Friend1', Username='testFriend1', FirstName='TestFirstNameFriend1', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  testFriend2 = User(Id='testIdEpic7Friend2', Username='testFriend2', FirstName='TestFirstNameFriend2', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  UserHelpers.UpdateUser(testFriend1, collection="TestUsers")
  UserHelpers.UpdateUser(testFriend2, collection="TestUsers")
  testFriendsUsernameList: list[str] = ["testFriend1", "testFriend2"]

  # now create the test user and assign the above users as its friends
  testUser = User(Id='testIdEpic7', Username='testUsernameEpic7', FirstName='TestFirstName', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  testFriends: dict[str, bool] = {"testFriend1": True, "testFriend2": True}
  testUser.Friends = testFriends
  UserHelpers.UpdateUser(testUser, collection="TestUsers")

  # get the list of test friends
  testFriendsList: list[User] = FriendHelpers.GetFriends(userNameToFind="testUsernameEpic7", collection="TestUsers")
  # ensure each of them in the pre-determined list of friend users
  for friend in testFriendsList:
    assert friend.Username in testFriendsUsernameList
    # get rid of the user account in the DB
    assert True == UserHelpers.DeleteUserAccount(user=friend, collection="TestUsers")

  assert True == UserHelpers.DeleteUserAccount(user=testUser, collection="TestUsers")


# test the list of all users
def test_DisplayListUsers():
  # create a couple dummy users
  testLoggedUser = User(Id='testLoggedUserEpic7', Username='testLoggedUsernameEpic7', FirstName='TestFirstNameUser1', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  testUser1 = User(Id='testIdEpic7User1', Username='testUser1Epic7', FirstName='TestFirstNameUser1', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  testUser2 = User(Id='testIdEpic7User2', Username='testUser2Epic7', FirstName='TestFirstNameUser2', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  # push to DB
  UserHelpers.UpdateUser(user=testLoggedUser, collection="TestUsers")
  assert True == UserHelpers.UpdateUser(user=testLoggedUser, collection="TestUsers")
  assert True == UserHelpers.UpdateUser(user=testUser1, collection="TestUsers")
  assert True == UserHelpers.UpdateUser(user=testUser2, collection="TestUsers")

  set_keyboard_input(["-1"])
  DisplayEveryUser(loggedUser=testLoggedUser, userCollection="TestUsers")
  output = get_display_output()
  assert output == ["\nSelect one of the user to send a message\n", "1 - testUser1Epic7", "2 - testUser2Epic7", "\nEnter (-1 to exit current menu): "]

  # # get rid of the dummy users from DB
  assert True == UserHelpers.DeleteUserAccount(user=testLoggedUser, collection="TestUsers")
  assert True == UserHelpers.DeleteUserAccount(user=testUser1, collection="TestUsers")
  assert True == UserHelpers.DeleteUserAccount(user=testUser2, collection="TestUsers")


# test the messaging
def test_Messaging():
  # create a couple test users
  testUser1 = User(Id='testIdEpic7User1', Username='testUser1Epic7', FirstName='TestFirstNameUser1', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  testUser2 = User(Id='testIdEpic7User2', Username='testUser2Epic7', FirstName='TestFirstNameUser2', LastName='TestLastName',
                    University='TestUniversity', Major='major')
  # push to DB
  UserHelpers.UpdateUser(user=testUser1, collection="TestUsers")
  UserHelpers.UpdateUser(user=testUser2, collection="TestUsers")

  # now create a message from test user 1 to test user 2
  testMessageContent: str = "Testing a message from testUser1 to testUser2"
  testMessage = Message(
    Id="testMessageEic7", 
    SenderId=testUser1.Id,
    ReceiverId=testUser2.Id,
    Content=testMessageContent)

  MessageHelpers.UpdateMessage(message=testMessage, collection="testMessages")

  # test the inbox
  set_keyboard_input(["-1"])
  ShowInbox(loggedUser=testUser2, userCollection="TestUsers", messageCollection="testMessages")
  output = get_display_output()

  assert output == ["\n1. From: TestFirstNameUser1 TestLastName (Unread)", 
  "\nEnter a message number to display it:", "\nEnter (-1 to exit current menu): ",
  ]

  # test the message
  set_keyboard_input([])
  MessageHelpers.DisplayMessage(message=testMessage, userCollection="TestUsers", messageCollection="testMessages")
  output = get_display_output()

  assert output == ["===============================================", 
    "\nFrom: TestFirstNameUser1 TestLastName\nTo: TestFirstNameUser2 TestLastName\n\nContent:\nTesting a message from testUser1 to testUser2\n",
     "==============================================="]

  # get rid of the test users
  assert True == UserHelpers.DeleteUserAccount(user=testUser1, collection="TestUsers")
  assert True == UserHelpers.DeleteUserAccount(user=testUser2, collection="TestUsers")
  # get rid of the test message
  assert True == MessageHelpers.DeleteMessageById(messageId=testMessage.Id, collection="testMessages")

# EPIC8: Testing if a user gets notification if tthey have not created their Profile
def test_UserProfileNotification():
    user1 = User(UserHelpers.CreateUserId("testUser1", "testPass2!"), "testUserID1", "test1", "test1")
    UserHelpers.UpdateUser(user1, "testUsers")
    output1 =  ProfileHelpers.ProfileExists(user1)
    assert output1 == False

    set_keyboard_input(["-1"])
    UserNotificationHelpers.NotifyIfProfileNotCreated(user1)
    
    output = get_display_output()

    assert output == ["\nDon't forget to create a profile"]

    assert True == UserHelpers.DeleteUserAccount(user1, collection="testUsers") 

