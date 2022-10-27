from helpers.DisplayJobTitlesHelper import JobTitleHelper 
from helpers.MenuHelpers import MenuHelpers

def DisplayJobTitle():
    while True:
        print("\nPlease select if you want to filter the Job:\n")
        MenuHelpers.DisplayOptions(["Yes", "No"])

        try:
            optionNo: int = MenuHelpers.InputOptionNo()

            if optionNo == -1: break
            
            elif optionNo == 1:
                JobTitleHelper.FilterJobTitles()
            
            elif optionNo == 2:
                JobTitleHelper.GetAllJobTitles()

            else:
                print("Invalid entry! Please try again.\n")

        except:
            print("Invalid entry! Please try again.\n")
            break

