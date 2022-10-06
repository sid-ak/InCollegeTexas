from typing import List
from helpers.MenuHelpers import MenuHelpers

# this global variable will store the list of "made-up" skills
SkillsList = ['communication', 'marketing', 'python programming', 'web development', 'public speaking']

def DisplaySkills(skills):
    index = 1
    for i in range(len(skills)):
        print(f'{str(index)}. {skills[i].title()}')
        index += 1

# this function will present a list of 5 skills and ask the user to select one
# this function will return a string representing either one of the skills selected
# from the presented list, "SKIP" to indicated the user did not select a skill or "-1"
# meaning that the user selected an invalid option
def PresentSkillsAction() -> List[str]:
    skills = SkillsList
    
    selectedSkills = []

    # this variable will identify if the user decided to go back
    terminateSelections = False

    while True:
        print("\nPlease select one of the following skills: ")

        DisplaySkills(skills)

        while True:
            try:
                skillSelect = MenuHelpers.InputOptionNo()
                
                if skillSelect == 1:
                    selectedSkills.append(skills[0])
                    MenuHelpers.PrintUnderConstruction()
                    break
                elif skillSelect == 2:
                    selectedSkills.append(skills[1])
                    MenuHelpers.PrintUnderConstruction()
                    break
                elif skillSelect == 3:
                    selectedSkills.append(skills[2])
                    MenuHelpers.PrintUnderConstruction()
                    break
                elif skillSelect == 4:
                    selectedSkills.append(skills[3])
                    MenuHelpers.PrintUnderConstruction()
                    break
                elif skillSelect == 5:
                    selectedSkills.append(skills[4])
                    MenuHelpers.PrintUnderConstruction()
                    break
                elif skillSelect == -1:
                    selectedSkills.append("SKIP")
                    terminateSelections = True
                    break
                else:
                    selectedSkills.append("-1")
                    print("\nError! Invalid entry! Try again.")
            except:
                selectedSkills.append("-1")
                print("\nError! Invalid Entry! Try again.")
        
        if terminateSelections:
            break

    return selectedSkills
    
