import pytest
from authentication.Signup import ValidatePassword
from loggedInActions.LearnNewSkill import PresentSkillsAction
from loggedInActions.JobInternshipSearch import FindJobInternshipAction
from loggedInActions.FindSomeone import FindSomeoneAction

def test_ValidatePassword():
    good_pwd = ["Test123@", "Testing1234@"]
    for pwd in good_pwd:
        assert ValidatePassword(pwd) == True

    bad_pwd = ["Test123", "test123@", "Test@One", "Test123@test1"]
    for pwd in bad_pwd:
        assert ValidatePassword(pwd) == False

def test_LearnNewSkill(capfd):
    PresentSkillsAction()
    out, err = capfd.readouterr()
    assert out == "1. communication\n2. marketing\n3. python programming\n4. web development\n5. public speaking\n"

def test_JobInternshipSearch(capfd):
    FindJobInternshipAction()
    out, err = capfd.readouterr()
    assert out == "under construction\n"

def test_FindSomeone(capfd):
    FindSomeoneAction()
    out, err = capfd.readouterr()
    assert out == "under construction\n"