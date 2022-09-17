from firebase.Firebase import database
from authentication.Signup import RegisterNewUser

# get username and password from input
username = input("Enter username: ")
password = input("Enter password: ")

# now call the Register method and store the result in a variable
result_operation = RegisterNewUser(username=username, password=password)

print("\nResult of operation: ", result_operation)
