from authentication.Signup import validatePassword

# get the password
password = input("Enter password: ")

# now call the validate method and store the operation result in a variable
result_operation = validatePassword(password=password)