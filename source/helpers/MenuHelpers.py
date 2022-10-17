class MenuHelpers:

    # Displays a prompt to the user to take an integer input from them.
    # Used for selecting a menu option or to exit current menu.
    def InputOptionNo() -> int:
        return int(input("\nEnter (-1 to exit current menu): "))

    # Displays an "under construction" message.
    # Used for an unfinished menu option.
    def PrintUnderConstruction():
        print ("under construction")
    
    # Displays a list of the specified options.
    def DisplayOptions(options: list[str]):
        i: int = 1
        for option in options:
            print(f"{i} - {option}")
            i += 1