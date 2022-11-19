from helpers.APIHelpers import checkInputFileExists, GetInputJob
from helpers.JobHelpers import JobHelpers

def RunInputAPIS(jobCollection:str = "Jobs", userCollection:str = "Users") -> bool:

    try:
        if not jobsInputAPI(jobCollection, userCollection):
            raise Exception("Error running jobs input API\n")

        return True

    except Exception as e:
        print(e)
        return False

def jobsInputAPI(jobCollection:str = "Jobs", userCollection:str = "Users") -> bool:
    input_path = checkInputFileExists("newJobs.txt")
    if input_path == None:
        raise Exception("Input path does not exist!\n")

    try:
        with open(input_path, "r") as inputFile:
            count = 0
            description = posterName = salary = employer = location = ""

            isDescription = False
            skip = False
            try:
                for line in inputFile:
                    # if end of description
                    if line.strip() == "&&&":
                        isDescription = False
                        count += 1
                        continue
                    # end of job details, make job if limit not met
                    elif line.strip() == "=====":
                        if not skip:
                            job = GetInputJob(jobTitle, description, posterName, employer, location, salary, userCollection)
                            if not job: raise Exception ("could not format input job\n")

                            if not JobHelpers.IsJobLimitMet(jobCollection):
                                if not JobHelpers.CreateJob(job, jobCollection):
                                    raise Exception(f"Error Adding Job to DB!\n")

                        # reset values
                        description = posterName = salary = employer = location = ""
                        continue

                    # take, store and manage input from input file
                    if count % 6 == 0: # Title
                        jobTitle = line.strip()
                        # check title against data in DB
                        try:
                            if JobHelpers.CheckTitleInFB(jobTitle, jobsCollection=jobCollection):
                                skip = True
                            else:
                                skip = False
                        except Exception as e:
                            print(f"Error checking if title exists in DB {e}\n")
                            return False

                    elif count % 6 == 1: # Description
                        isDescription = True
                        description += " " + line.strip()

                    elif count % 6 == 2 and not skip: # Poster Name
                        posterName = line.strip()

                    elif count % 6 == 3 and not skip: # Employer Name
                        employer = line.strip()

                    elif count % 6 == 4 and not skip: # Location
                        location = line.strip()

                    elif count % 6 == 5 and not skip: # Salary
                        salary = line.strip()

                    if not isDescription:
                        count += 1

            except Exception as e:
                print(f"Error reading job input file lines {e}\n")
                return False

        return True

    except Exception as e:
        print(f"Error reading job input file {e}\n")
        return False
