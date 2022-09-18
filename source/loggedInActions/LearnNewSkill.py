from typing import List

# this global variable will store the list of "made-up" skills
SkillsList = ['communcation', 'marketing', 'python programming', 'web development', 'public speaking']


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

        index = 1
        for i in range(len(skills)):
            print(f'{str(index)}. {skills[i].title()}')
            index += 1

        while True:
            try:
                skillSelect = int(input("\nEnter (-1 to go back): "))
                if skillSelect == 1:
                    selectedSkills.append(skills[0])
                    print("\nunder construction")
                    break
                elif skillSelect == 2:
                    selectedSkills.append(skills[1])
                    print("\nunder construction")
                    break
                elif skillSelect == 3:
                    selectedSkills.append(skills[2])
                    print("\nunder construction")
                    break
                elif skillSelect == 4:
                    selectedSkills.append(skills[3])
                    print("\nunder construction")
                    break
                elif skillSelect == 5:
                    selectedSkills.append(skills[4])
                    print("\nunder construction")
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
    
