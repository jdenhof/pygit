import os
import subprocess

global_directory = None

def execute_in_directory(directory, func, *args):
    if directory == None and global_directory == None:
        raise ValueError(f"No supplied or global_directory to execute function {func.__name__}\nSupply a directory or use GitUtils.set_global_directory(dir: str)")
    elif directory == None:
        directory = global_directory
    
    if not os.path.exists(directory):
        raise RuntimeError(f"Directory {directory} does not exists!")
    
    curdir = os.curdir
    os.chdir(directory)
    result = func(*args)
    os.chdir(curdir)
    return result

def __set_global_directory(directory: str):
    global global_directory
    global_directory = directory

def __get_num_commits():
    return int(subprocess.run(["git", "rev-list", "--all", "--count"], capture_output=True, text=True).stdout)

def __is_clean_working_tree():
    return bool("nothing to commit, working tree clean" in subprocess.run(["git", "status"], capture_output=True, text=True).stdout)
