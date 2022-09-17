import pytest
from Valid import validatePassword

def test_validatePassword():
    good_pwd = ["Test123@", "Testing1234@"]
    for pwd in good_pwd:
        assert validatePassword(pwd) == True

    bad_pwd = ["Test123", "test123@", "Test@One", "Test123@test1"]
    for pwd in bad_pwd:
        assert validatePassword(pwd) == False