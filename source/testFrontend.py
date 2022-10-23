from io import StringIO
import sys
from authentication.Signup import ValidatePassword
from actions.LearnNewSkill import DisplaySkills
from actions.FindSomeone import FindSomeoneAction
from actions.PlayVideo import PlayVideo
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from actions.SearchUsers import SearchUsers,FriendRequest
from actions.DisplayPendingRequests import DisplayPendingRequests
from actions.ShowMyNetwork import ShowMyNetwork
from actions.UpdateProfile import ToTileFormat, EditProfile
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from testInputs.testInputs import set_keyboard_input
from testInputs.testInputs import get_display_output
from model.User import User, UserHelpers
from testBackend import test_UserProfile_CreateProfile

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
    set_keyboard_input(["1", "-1"])
    DisplayUsefulLinks(True, 1, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers"]

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
    set_keyboard_input(["1", "-1"])
    DisplayUsefulLinksHelpers.General(True, 1, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nSignup Selected.",
                        "\nPlease enter your username: ",
                        "\nPlease enter your password: ",
                        "\nError! Your password does not meet one or some of the standards!",
                        "\nFailure! We have not been able to create a new account for you."
                      ]

    set_keyboard_input(["2", "-1"])
    DisplayUsefulLinksHelpers.General(True, 2, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nWe're here to help"
                      ]

    set_keyboard_input(["3", "-1"])
    DisplayUsefulLinksHelpers.General(True, 3, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nIn College:\nWelcome to In College, the world's largest college student network\nwith many users in many countries and territories worldwide"
                      ]

    set_keyboard_input(["4", "-1"])
    DisplayUsefulLinksHelpers.General(True, 4, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "\nIn College Pressroom:\nStay on top of the latest news, updates, and reports"
                      ]

    set_keyboard_input(["5", "-1"])
    DisplayUsefulLinksHelpers.General(True, 5, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "under construction"
                      ]

    set_keyboard_input(["6", "-1"])
    DisplayUsefulLinksHelpers.General(True, 6, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "under construction"
                      ]

    set_keyboard_input(["7", "-1"])
    DisplayUsefulLinksHelpers.General(True, 7, None)
    output = get_display_output()
    assert output == ["\nPlease select one of the following links to display its content:",
                        "1 - Sign Up",
                        "2 - Help Center",
                        "3 - About",
                        "4 - Press",
                        "5 - Blog",
                        "6 - Careers",
                        "7 - Developers",
                        "under construction"
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
  
  set_keyboard_input(["2","University of South Florida" , "-1"])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by university.\nEnter the university of the user you want to search for: ",
                    "1. Osama Basit\n",
                    "2. Prerna Yarehalli\n",
                    "3. Sidharth Anandkumar\n",
                    "4. Anshika Bhowmick\n",
                    "Enter the option number of the user you want to send a friend request to: ",
                    "\nEnter (-1 to exit current menu): ",
                    "\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                  ]

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
  
  set_keyboard_input(["3", "Computer Science" , "-1"])
  SearchUsers()
  output = get_display_output()
  assert output == ["\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "You have selected to search by major.\nEnter the major of the user you want to search for: ",
                    "1. Osama Basit\n",
                    "2. Prerna Yarehalli\n",
                    "3. Sidharth Anandkumar\n",
                    "4. Anshika Bhowmick\n",
                    "Enter the option number of the user you want to send a friend request to: ",
                    "\nEnter (-1 to exit current menu): ",
                    "\nPlease select one of the following options:\n",
                    "1 - Search by last name",
                    "2 - Search by university",
                    "3 - Search by major",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                  ]


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
  users = UserHelpers.GetAllUsers()
  for user in users:
    if user.Username == "Sid":
      DisplayPendingRequests(user)
  output = get_display_output()
  assert output == ["Your pending requests:\n",
                    "You have no pending requests.\n",
                    ]

  set_keyboard_input(["2", "-1"])
  users = UserHelpers.GetAllUsers()
  for user in users:
    if user.Username == "Sid":
      DisplayPendingRequests(user)
  output = get_display_output()
  assert output == ["Your pending requests:\n",
                    "You have no pending requests.\n",
                    ]


def test_ShowYourNetwork():
  set_keyboard_input([])
  users = UserHelpers.GetAllUsers()
  for user in users:
    if user.Username == "Sid":
      ShowMyNetwork(user)
  output = get_display_output()
  assert output == ["Your network:\n",
                    "1. Anshika Bhowmick\n",
                    "2. Prerna Yarehalli\n",
                    "3. Osama Basit\n",
                    "\nPlease select one of the following options:\n",
                    "1 - Do you want to disconnect with a friend?",
                    "\nEnter (-1 to exit current menu): ",
                    "Unexpected error ocurred\n"
                    ]

# Tests below worked on for EPIC 5 - 10/23/22 by Anshika

# checking if university and major are displayed in title case
def test_TitleCaseUniversity():
  output = ToTileFormat("university of south florida")
  assert output == "University Of South Florida"

  output = ToTileFormat("computer science")
  assert output == "Computer Science"

# Ensure that a user can add up-to three job experiences.
def test_JobExperienceLimit():
  test_UserProfile_CreateProfile(deleteTestUser: bool = False)
  set_keyboard_input(["6", "Title01", "Employer01", "10/25/2018", "10/25/2022", "Location01", "Exp01"])
  EditProfile()
  set_keyboard_input(["6", "Title02", "Employer02", "10/28/2015", "10/28/2021", "Location02", "Exp02"])
  EditProfile()
  set_keyboard_input(["6", "Title03", "Employer02", "10/21/2017", "10/21/2020", "Location03", "Exp03"])
  EditProfile()
  set_keyboard_input(["6", "Title04", "Employer02", "10/21/2017", "10/21/2020", "Location04", "Exp04"])
  EditProfile()
  output = get_display_output()
  assert output == ["\nError! You already have added 3 experiences."]
  UserHelpers.DeleteUserAccount()

# Ensure that a user can see the profiles of their friends/networks
#def test_ViewFriendProfile():
  # there should be user -> select friend -> view profile

# Ensure that a user cannot see the profiles of their friends, if friend doesn't have a profile
#def test_ViewFriendProfileNoProfile():
  # there should be user -> select friend -> view profile -> no profile