from utils import get_repo, set_repo

def get_num_commits(directory: str = None) -> int:
    """Return the number of commits in repo history"""

def is_clean_working_tree(directory: str = None) -> bool:
    """Return boolean indicating repo working tree is clean and upto date"""

def get_last_commit_hash(directory: str = None) -> str:
    """Gets repo's last commit hash string"""
    
def expose_utils_functions():
    import utils
    # Get all functions from utils module
    utils_functions = [func for func in dir(utils) if callable(getattr(utils, func)) and func.startswith("__git")]

    # Dynamically create functions in your module
    for func_name in utils_functions:
        exposed_func_name = func_name.lstrip('__git_')  # Remove leading underscores
        exposed_func = lambda directory=None, func=getattr(utils, func_name): utils.execute_in_repo(directory, func)
        globals()[exposed_func_name] = exposed_func

# Call the function to expose utils functions
expose_utils_functions()