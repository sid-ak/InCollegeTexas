from firebase.Firebase import database
from authentication.Signin import LoginUser

# get username and password from input
username = input("Enter username: ")
password = input("Enter password: ")

# call the Login method
# resultoperation will be a boolean: True if it successfully logged in, False otherwise
result_operation = LoginUser(username=username, password=password)

print("\nResult of operation: ", result_operation)
