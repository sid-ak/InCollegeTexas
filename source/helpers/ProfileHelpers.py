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


    # returns the formatted string with the displays of education
    def HelpPrintEducationList(educationList: list[Education]) -> str:
        try:
            if educationList == None or educationList == []:
                return ""

            output: str = "\n"
            indexer: int = 1

            for education in educationList:
                output += f"\n{indexer})"
                output += f"\nSchool Name: {education.SchoolName}\n" 
                output += f"Degree: {education.Degree}\n"
                output += f"Years Attended: {education.YearsAttended}\n"
                
                indexer += 1
            
            return output
        
        except Exception as e:
            raise Exception(f"Could not display education list\n{e}")

    
    # returns the formatted string with the displays of experience
    def HelpPrintExperienceList(experienceList: list[Experience]) -> str:
        try:
            if experienceList == None or experienceList == []:
                return ""

            output: str = "\n"
            indexer: int = 1

            for experience in experienceList:
                output += f"\n{indexer})" 
                output += f"\nTitle: {experience.Title}\n"
                output += f"Employer: {experience.Employer}\n"
                output += f"Date Started: {experience.DateStarted}\n"
                output += f"Date Ended: {experience.DateEnded}\n"
                output += f"Location: {experience.Location}\n"
                output += f"Description: {experience.Description}\n"

                indexer += 1
            
            return output
        
        except Exception as e:
            raise Exception(f"Could not display experience list\n{e}")


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
                    education.SchoolName = ProfileHelpers.ToTitleFormat(input("Enter the new name of the school: "))
                    print("Successfully updated the school name.\n")
                
                elif decision == 2:
                    print("You have selected to edit Degree")
                    education.Degree = ProfileHelpers.ToTitleFormat(input("Enter the new degree: "))
                    print("Successfully updated degree.\n")
                
                elif decision == 3:
                    print("You have selected to edit Years Attended")
                    education.YearsAttended = ProfileHelpers.ToTitleFormat(input("Enter the new years attended: "))
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
                    experience.Title = ProfileHelpers.ToTitleFormat(input("Enter new title: "))
                    print("Successfully updated title")
                
                elif decision == 2:
                    print("You have selected to edit Employer")
                    experience.Employer = ProfileHelpers.ToTitleFormat(input("Enter the new employer: "))
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
                    experience.Location = ProfileHelpers.ToTitleFormat(input("Enter the new location: "))
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


    # Updates an education list by adding to it or editing a specific education.
    def UpdateEducation(educationList: list[Education]) -> list[Education]:
        try:
            print("Would you like to add or edit education?")
            MenuHelpers.DisplayOptions(["Add", "Edit"])
            decision: int = MenuHelpers.InputOptionNo()
            
            if decision == 1:
                print("You have selected to add education")
                educationList = ProfileHelpers.AddEducation(educationList)
                return educationList
            
            elif decision == 2:
                print("You have selected to edit education")
                educationList = ProfileHelpers.EditEducation(educationList)
                return educationList
        
        except Exception as e:
            raise Exception(f"Could not update education.\n{e}")


    # Adds an education to the specified education list using user input.
    def AddEducation(educationList: list[Education]) -> list[Education]:
        try:
            education = Education()
            education.SchoolName = ProfileHelpers.ToTitleFormat(input("Enter the name of your school: "))
            education.Degree = ProfileHelpers.ToTitleFormat(input("Enter your degree: "))
            education.YearsAttended = int(input("Enter the years attended: "))
            
            if education != Education():
                educationList.append(education)
            
            return educationList
        
        except Exception as e:
            raise Exception(f"\nError! Could not add education.\n{e}")


    # Edits a specific education from the specified education index from the user.
    def EditEducation(educationList: list[Education]) -> list[Education]:
        try:
            if educationList == None or educationList == []:
                raise Exception("No education found to edit. Please add education first.")
            
            print("\nEnter the index of the education you would like to edit.\nEducation list:")
            print(ProfileHelpers.HelpPrintEducationList(educationList))
            educationIndex: int = MenuHelpers.InputOptionNo()
            educationIndex -= 1
            
            try:
                education = educationList[educationIndex]
                education = ProfileHelpers.HelpEditEducationAttributes(education)
                educationList[educationIndex] = education
                return educationList

            except Exception as e:
                raise Exception(
                    f"Could not edit specified education at index {educationIndex}.\n{e}")
        
        except Exception as e:
            raise Exception(f"\nError! Could not edit education.\n{e}")


    # Updates an experience list by adding to it or editing a specific experience.
    def UpdateExperience(experienceList: list[Experience]) -> list[Experience]:
        try:
            print("Would you like to add or edit experience?")
            MenuHelpers.DisplayOptions(["Add", "Edit"])
            decision: int = MenuHelpers.InputOptionNo()
            
            if decision == 1:
                print("You have selected to add experience")
                experienceList = ProfileHelpers.AddExperience(experienceList)
                return experienceList
            
            elif decision == 2:
                print("You have selected to edit experience")
                experienceList = ProfileHelpers.EditExperience(experienceList)
                return experienceList
        
        except Exception as e:
            raise Exception(f"Could not update experience.\n{e}")


    # Adds an experience to the specified experience list using user input.
    def AddExperience(experienceList: list[Experience]) -> list[Experience]:
        try:
            if len(experienceList) == 3:
                raise Exception("\nError! You can only enter a maximum of 3 experiences.")
            
            experience = Experience()
            experience.Title = ProfileHelpers.ToTitleFormat(input("Enter title: "))
            experience.Employer = ProfileHelpers.ToTitleFormat(input("Enter Employer: "))
            experience.DateStarted = input("Enter date started: ")
            experience.DateEnded = input("Enter date ended: ")
            experience.Location = ProfileHelpers.ToTitleFormat(input("Enter location: "))
            experience.Description = input("Enter description: ")
            
            if experience != Experience():
                experienceList.append(experience)
            
            return experienceList
        
        except Exception as e:
            raise Exception(f"\nError! Could not add experience.\n{e}")


    # Edits a specific experience from the specified experience index from the user.
    def EditExperience(experienceList: list[Experience]) -> list[Experience]:
        try:
            if experienceList == None or experienceList == []:
                raise Exception("No experience found to edit. Please add experience first.")
            
            print("\nEnter the index of the experience you would like to edit.\nExperience list:")
            print(ProfileHelpers.HelpPrintExperienceList(experienceList))
            experienceIndex: int = MenuHelpers.InputOptionNo()
            experienceIndex -= 1
            
            try:
                experience = experienceList[experienceIndex]
                experience = ProfileHelpers.HelpEditExperienceAttributes(experience)
                experienceList[experienceIndex] = experience
                return experienceList
                                    
            except Exception as e:
                raise Exception(
                    f"Could not edit specified experience at index {experienceIndex}.\n{e}")
        
        except Exception as e:
            raise Exception(f"\nError! Could not edit experience.\n{e}")
