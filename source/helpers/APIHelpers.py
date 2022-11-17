import os

# returns current path of where this function is called from
# ideally would be called from a directory in level with main.py for any user
def getCurrentPath():
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
