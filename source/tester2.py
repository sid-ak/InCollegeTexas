import pytest
from Valid import validatePassword
from smth import ShowMessage
from smth import DisplayMenu
from smth import LearnNewSkill

def test_validatePassword():
    good_pwd = ["Test123@", "Testing1234@"]
    for pwd in good_pwd:
        assert validatePassword(pwd) == True

    bad_pwd = ["Test123", "test123@", "Test@One", "Test123@test1"]
    for pwd in bad_pwd:
        assert validatePassword(pwd) == False

def test_showMessage(capfd):
    ShowMessage()
    out, err = capfd.readouterr()
    assert out == "Under Construction\n"

def test_displayMenu(capfd):
    DisplayMenu()
    out, err = capfd.readouterr()
    assert out == "1. Search for a job\n2. Find someone that they know\n3. Learn a new skill\n"

def test_learnNewSkill(capfd):
    LearnNewSkill()
    out, err = capfd.readouterr()
    assert out == "1. Skill1\n2. Skill2\n3. Skill3\n4. Skill4\n5. Skill5\n"