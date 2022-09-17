from authentication.Signup import ValidatePassword

# get the password
password = input("Enter password: ")

# now call the validate method and store the operation result in a variable
result_operation = ValidatePassword(password=password)