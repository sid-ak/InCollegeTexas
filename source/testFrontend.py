from authentication.Signup import ValidatePassword
from loggedInActions.LearnNewSkill import DisplaySkills
from loggedInActions.JobInternshipSearch import FindJobInternshipAction
from loggedInActions.FindSomeone import FindSomeoneAction

def test_LearnNewSkill(capfd):
    skills = ['communication', 'marketing', 'python programming', 'web development', 'public speaking']
    DisplaySkills(skills)
    out, err = capfd.readouterr()
    assert out == "1. Communication\n2. Marketing\n3. Python Programming\n4. Web Development\n5. Public Speaking\n"

def test_JobInternshipSearch(capfd):
    FindJobInternshipAction()
    out, err = capfd.readouterr()
    assert out == "\nunder construction\n"

def test_FindSomeone(capfd):
    FindSomeoneAction()
    out, err = capfd.readouterr()
    assert out == "\nunder construction\n"