from authentication.Signup import ValidatePassword
from actions.LearnNewSkill import DisplaySkills
from actions.FindSomeone import FindSomeoneAction
from actions.PlayVideo import PlayVideo
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from actions.SearchUsers import SearchUsers,FriendRequest
from actions.DisplayPendingRequests import DisplayPendingRequests
from actions.ShowMyNetwork import ShowMyNetwork
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from helpers.ProfileHelpers import ProfileHelpers
from testInputs.testInputs import set_keyboard_input
from testInputs.testInputs import get_display_output
from helpers.UserHelpers import UserHelpers
from model.User import User

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
                    "Enter the option number of the user you want to send a friend request to: ",
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
