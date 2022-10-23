from model.Profile import Experience, Profile
from model.User import User


class ProfileHelpers:
    _experiencesLimit: int = 3

    # Checks if the maximum number of experiences have been entered for a user profile.
    def IsProfileExpLimitMet(user: User) -> bool:
        if user.Profile == None or user.Profile == Profile():
            return False

        experiences: list[Experience] = user.Profile.ExperienceList

        if  experiences == ([] or None):
            return False
        
        return True if len(experiences) > ProfileHelpers._experiencesLimit else False