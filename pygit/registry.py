import os

__global_repo_dir = None

def validate_repo(repository: str, silent: bool = False):
    if os.path.exists(repository):
        return True

    if not silent:
        raise RuntimeError(f"Repo {repository} does not exists!")
    else:
        return False
        
def get_repo():
    return __global_repo_dir

def set_repo(repo_dir: str):
    validate_repo(repo_dir)
    global __global_repo_dir
    __global_repo_dir = repo_dir

def register_command(func):
    def wrapper(*args, **kwargs):
        repo_supplied = 'repository' in kwargs
        if not repo_supplied and get_repo() == None:
            raise RuntimeError("No repository supplied to execute command")
        if repo_supplied:
            validate_repo(kwargs['repository'])
        else: 
            kwargs['repository'] = get_repo()
            
        _prev_dir = os.curdir
        result = None
        try:
            os.chdir(kwargs['repository'])
            result = func(*args, **kwargs)
        except Exception as e:
            raise e # Forward function exceptions on 
        finally:
            os.chdir(_prev_dir)
        return result
    return wrapper