from model.Profile import Experience, Profile


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
