from model.User import User
from helpers.UserNotificationHelpers import UserNotificationHelpers
from helpers.JobNotificationHelpers import JobNotificationHelpers

class NotificationHelpers:

    # Display notifications presented in the login menu.
    def DisplayLoginNotifications(loggedUser: User):
        
        print(f"\n================= Notifications =================\n")

        # Notify the user about the new users who joined the platform
        UserNotificationHelpers.NotifyAboutNewUsers(loggedUser)
        
        # Notify if user has not created a profile
        UserNotificationHelpers.NotifyIfProfileNotCreated(loggedUser)

        # Notify if the user as unread messages.
        UserNotificationHelpers.NotifyIfUnreadMessages(loggedUser)

        # Notify if the user has not applied for a job in a while.
        JobNotificationHelpers.NotifyIfNotAppliedJob(loggedUser)

        # Notify if new jobs have been posted since the user last logged in.
        JobNotificationHelpers.NotifyIfNewJobsPosted(loggedUser)

        print("\n=================================================\n")
    

    # Display notifications presented in the job/internship menu.
    def DisplayJobInternshipNotifications(loggedUser: User):

        print(f"\n================= Notifications =================\n")

        # tell the user how many jobs they have applied to
        JobNotificationHelpers.NotifyAppliedJobsCount(loggedUser)

        # first we notify the user if a job or jobs they applied for has 
        # or have been deleted from the DB
        JobNotificationHelpers.NotifyIfAppliedJobsDeleted(loggedUser)

        print("\n=================================================\n")
