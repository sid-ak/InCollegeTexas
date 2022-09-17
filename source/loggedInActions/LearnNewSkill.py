# this global variable will store the list of "made-up" skills
SkillsList = ['communcation', 'marketing', 'python programming', 'web development', 'public speaking']


# this function will present a list of 5 skills and ask the user to select one
# this function will return a string representing either one of the skills selected
# from the presented list, "SKIP" to indicated the user did not select a skill or "-1"
# meaning that the user selected an invalid option
def PresentSkillsAction() -> str:
    skills = SkillsList
    
    print("\nPlease select one of the following skills: ")

    index = 1
    for i in range(len(skills)):
        print(f'{str(index)}. {skills[i].title()}')
        index += 1
    
    selectedSkill = ""

    while True:
        try:
            skillSelect = int(input("\nEnter (-1 to go back): "))
            if skillSelect == 1:
                selectedSkill = skills[0]
                print("\nunder construction")
                break
            elif skillSelect == 2:
                selectedSkill = skills[1]
                print("\nunder construction")
                break
            elif skillSelect == 3:
                selectedSkill = skills[2]
                print("\nunder construction")
                break
            elif skillSelect == 4:
                selectedSkill = skills[3]
                print("\nunder construction")
                break
            elif skillSelect == 5:
                selectedSkill = skills[4]
                print("\nunder construction")
                break
            elif skillSelect == -1:
                selectedSkill = "SKIP"
                break
            else:
                selectedSkill = "-1"
                print("\nError! Invalid entry!")
        except:
            selectedSkill = "-1"
            print("\nError! Invalid Entry! Try again.")

    return selectedSkill
    
