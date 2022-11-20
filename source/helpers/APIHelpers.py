import os
from helpers.JobHelpers import JobHelpers
from helpers.UserHelpers import UserHelpers
from model.Job import Job

# returns current path of where this function is called from
# ideally would be called from a directory in level with main.py for any user
def getCurrentPath() -> str:
    try:
        return os.getcwd()
    except Exception as e:
        print(f"Couldn't get current path {e}\n")


def createOutputDirectory():
    output_path = getCurrentPath() + '\output'
    try:
        if not os.path.exists(output_path):
            os.mkdir(getCurrentPath() + '\output')
    except Exception as e:
        print(f"Couldn't make output directory {e}\n")


def checkInputFileExists(fileName: str) -> str:
    input_path = getCurrentPath()
    try:
        path = input_path + "\\" + fileName
        if os.path.exists(path):
            return path
        else:
            try:
                path = input_path + "\input\\" + fileName
                if os.path.exists(path):
                    return path
                else:
                    return None
            except Exception as e:
                print(f"Error checking input directory {e}")

    except Exception as e:
        print(f"Error checking if input file exists {e}")


def GetInputJob(title, desc, posterName, employer, loc, salary, userCollection) -> Job:
    posterId = UserHelpers.GetUserIdByName(posterName, userCollection)
    if not posterId:
        raise Exception(f"Couldn't find user with poster name {posterName}\n")

    id: str = JobHelpers.CreateJobId(
        title,
        employer,
        desc,
        loc,
        salary
    )

    return Job(id, title, employer, desc, loc, salary, posterId)
