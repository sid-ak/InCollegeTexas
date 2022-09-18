import pytest
from authentication.Signup import ValidatePassword

# Tests below worked on for EPIC 1 - 9/19/22 by Anshika
def test_validatePassword():
    good_pwd = ["Test123@", "Testing1234@"]
    for pwd in good_pwd:
        assert ValidatePassword(pwd) == True

    bad_pwd = ["Test123", "test123@", "Test@One", "Test123@test1"]
    for pwd in bad_pwd:
        assert ValidatePassword(pwd) == False
