from io import StringIO
import sys
from authentication.Signup import ValidatePassword
from actions.LearnNewSkill import DisplaySkills
from actions.FindSomeone import FindSomeoneAction
from actions.PlayVideo import PlayVideo
from actions.DisplayUsefulLinks import DisplayUsefulLinks
from helpers.DisplayUsefulLinksHelpers import DisplayUsefulLinksHelpers
from testInputs.testInputs import set_keyboard_input
from testInputs.testInputs import get_display_output

# Tests below worked on for EPIC 2 - MM/DD/YYYY by XXXX
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

# Test to see if all Useful link works below
def test_UsefulLinksDisplay():
    # capturedOutput = StringIO()
    # sys.stdout = capturedOutput
    # DisplayUsefulLinks(onTest=True, testInput=1)
    # sys.stdout = sys.__stdout__
    # assertOutput = ["Please select one of the following links to display its content:","1 - Sign Up","2 - Help Center","3 - About","4 - Press","5 - Blog","6 - Careers","7 - Developers"]
    # for assertItem in assertOutput:
        # assert assertItem in capturedOutput.getvalue()
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
#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=1)
#     sys.stdout = sys.__stdout__
#     assert "\nSignup Selected." in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=2)
#     sys.stdout = sys.__stdout__
#     assert "\nWe"re here to help" in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=3)
#     sys.stdout = sys.__stdout__
#     assertOutput = ["\nIn College:"
#         + "\nWelcome to In College, the world's largest college student network"
#         + "\nwith many users in many countries and territories worldwide"]
#     for assertItem in assertOutput:
#         assert assertItem in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=4)
#     sys.stdout = sys.__stdout__
#     assertOutput = ["\nIn College Pressroom:"
#         + "\nStay on top of the latest news, updates, and reports"]
#     for assertItem in assertOutput:
#         assert assertItem in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=5)
#     sys.stdout = sys.__stdout__
#     assert "under construction\n" in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=6)
#     sys.stdout = sys.__stdout__
#     assert "under construction\n" in capturedOutput.getvalue()
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

#     capturedOutput = StringIO()
#     sys.stdout = capturedOutput
#     DisplayUsefulLinksHelpers.General(onTest=True, testInput=7)
#     sys.stdout = sys.__stdout__
#     assert "under construction\n" in capturedOutput.getvalue()
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