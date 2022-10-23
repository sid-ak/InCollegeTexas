from model.Profile import Experience, Profile, Education
from model.User import User
from helpers.MenuHelpers import MenuHelpers


class ProfileHelpers:
    _experiencesLimit: int = 3

    # Checks if the maximum number of experiences have been entered for a user profile.
    def IsProfileExpLimitMet(profile: Profile) -> bool:
        if profile == None or profile == Profile():
            return False

        experiences: list[Experience] = profile.ExperienceList

        if  experiences == None or experiences == []:
            return False
        
        return True if len(experiences) > ProfileHelpers._experiencesLimit else False

    

    # returns the formatted string with the displays of education
    def HelpPrintEducationList(profile: Profile) -> str:

        if len(profile.EducationList) != 0:
            output: str = "\n"
            indexer: int = 1
            for i in range(len(profile.EducationList)):
                item = Education.EducationToDict(profile.EducationList[i])
                output += f"\n{indexer}) \nSchool Name: {item['SchoolName']}\nDegree: {item['Degree']}\nYears Attended: {item['YearsAttended']}\n"
                indexer += 1
            return output

        else:
            return ""

    
    # returns the formatted string with the displays of experience
    def HelpPrintExperienceList(profile: Profile) -> str:

        if len(profile.ExperienceList) != 0:
            output: str = "\n"
            indexer: int = 1
            for i in range(len(profile.ExperienceList)):
                item = Experience.ExpToDict(profile.ExperienceList[i])
                output += f"\n{indexer}) \nTitle: {item['Title']}\nEmployer: {item['Employer']}\nDate Started: {item['DateStarted']}\nDate Ended: {item['DateEnded']}\nLocation: {item['Location']}\nDescription: {item['Description']}\n"
                indexer += 1
            return output

        else:
            return ""


    # checks if the user has a profile node
    def ProfileExists(user: User) -> bool:
        try:
            if (user.Profile != None and user.Profile != Profile()):
                return True
            else:
                return False
        except:
            return False


    # this function will help format an input string to title of each word
    def ToTitleFormat(input: str) -> str:
        words = input.split(" ")
        wordsFormated = []

        for word in words:
            wordsFormated.append(word.title())

        return " ".join(wordsFormated)


    # this function will help with the edition of each individual attribute of education
    def HelpEditEducationAttributes(education: Education) -> Education:
        
        while True:
            try:
                print("\nSelect one of the following parts of education to edit: ")
                options = ["Name of School: " + str(education.SchoolName),
                            "Degree: " + str(education.Degree),
                            "Years Attended: " + str(education.YearsAttended)]

                MenuHelpers.DisplayOptions(options=options)
                decision: int = MenuHelpers.InputOptionNo()

                if decision == 1:
                    print("You have selected to edit Name of School")
                    education.SchoolName = ToTitleFormat(input("Enter the new name of the school: "))
                    print("Successfully updated the school name.\n")
                
                elif decision == 2:
                    print("You have selected to edit Degree")
                    education.Degree = ToTitleFormat(input("Enter the new degree: "))
                    print("Successfully updated degree.\n")
                
                elif decision == 3:
                    print("You have selected to edit Years Attended")
                    education.YearsAttended = ToTitleFormat(input("Enter the new years attended: "))
                    print("Successfully updated the years attended")
                
                elif decision == -1:
                    print("You have selected to quit edition of education")
                    return education

                else:
                    print("\nError! Could not edit due to invalid input on attribute index.")
            
            except:
                print("\nError! Could not edit due to invalid input on attribute index.")


    # this function will help with the edition of each individual attribute of experience
    def HelpEditExperienceAttributes(experience: Experience) -> Experience:
        
        while True:
            try:
                print("\nSelect one of the following parts of experience to edit: ")
                options = ["Title: " + str(experience.Title),
                            "Employer: " + str(experience.Employer),
                            "Date Started: " + str(experience.DateStarted),
                            "Date Ended: " + str(experience.DateEnded),
                            "Location: " + str(experience.Location),
                            "Description: " + str(experience.Description)]

                MenuHelpers.DisplayOptions(options=options)
                decision: int = MenuHelpers.InputOptionNo()

                if decision == 1:
                    print("You have selected to edit Title")
                    experience.Title = ToTitleFormat(input("Enter new title: "))
                    print("Successfully updated title")
                
                elif decision == 2:
                    print("You have selected to edit Employer")
                    experience.Employer = ToTitleFormat(input("Enter the new employer: "))
                    print("Successfully updated employer")
                
                elif decision == 3:
                    print("You have selected to edit Date Started")
                    experience.DateStarted = input("Enter the new date started: ")
                    print("Successfully updated date started")

                elif decision == 4:
                    print("You have selected to edit Date Ended")
                    experience.DateEnded = input("Enter the new date ended: ")
                    print("Successfully updated date ended")

                elif decision == 5:
                    print("You have selected to edit Location")
                    experience.Location = ToTitleFormat(input("Enter the new location: "))
                    print("Successfully updated location")

                elif decision == 6:
                    print("You have selected to edit Description")
                    experience.Description = input("Enter the new description: ")
                    print("Successfully updated description")   

                elif decision == -1:
                    print("You have selected to quit edition of experience")
                    return experience

                else:
                    print("\nError! Could not edit experience due to invalid entry.")
            
            except:
                print("\nError! Could not edit due to invalid input on attribute index.")