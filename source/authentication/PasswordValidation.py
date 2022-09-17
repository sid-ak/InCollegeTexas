# this function will validate the password and return True, if it is valid, False otherwise
def validatePassword(password: str) -> bool:
    checkLength = False
    checkUpperCase = False
    checkDigit = False
    checkSpecialCharacter = False
    if len(password) >= 8 and len(password) <= 12:
        checkLength = True

    for charCheck in password:
        if charCheck.isupper():
            checkUpperCase = True
        elif charCheck.isdigit():
            checkDigit = True
        elif charCheck.islower() == False:
            checkSpecialCharacter = True
    
    if checkDigit and checkLength and checkSpecialCharacter and checkUpperCase:
        return True
    else:
        False