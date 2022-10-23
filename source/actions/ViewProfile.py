from model.User import User


# non-return function to print the profile of a user
def ViewProfile(loggedUser: User):
    print(f"\n{loggedUser.FirstName} {loggedUser.LastName}")
    print("Title: ", loggedUser.Profile.Title)
    print("University: ", loggedUser.Profile.University)
    print("Major: ", loggedUser.Profile.University)
    print("About: ", loggedUser.Profile.About)
    
    indexer: int = 1
    for i in range(len(loggedUser.Profile.EducationList)):
        print()