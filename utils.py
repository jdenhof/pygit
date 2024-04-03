import os
import subprocess

__global_repo = None

def get_repo():
    return __global_repo

def set_repo(__repo: str):
    global __global_repo
    __global_repo = __repo

def execute_in_repo(__repo, func, *args):
    
    if __repo == None and __global_repo == None:
        raise ValueError(f"No supplied or global_directory to execute function {func.__name__}\nSupply a directory or use GitUtils.set_global_directory(dir: str)")
    elif __repo == None:
        __repo = __global_repo
    
    if not os.path.exists(__repo):
        raise RuntimeError(f"Repo {__repo} does not exists!")
    
    curdir = os.curdir
    os.chdir(__repo)
    result = func(*args)
    os.chdir(curdir)
    return result

def __git_get_last_commit_hash():
    return subprocess.run(['git', 'rev-parse', 'HEAD'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip()

def __git_get_num_commits():
    return int(subprocess.run(["git", "rev-list", "--all", "--count"], capture_output=True, text=True).stdout.strip())

def __git_is_clean_working_tree():
    return bool("nothing to commit, working tree clean" in subprocess.run(["git", "status"], capture_output=True, text=True).stdout.strip())