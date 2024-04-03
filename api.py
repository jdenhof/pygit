import utils

def get_num_commits(directory: str = None): 
    return utils.execute_in_directory(directory, utils.__get_num_commits)

def is_clean_working_tree(directory: str = None):
    return utils.execute_in_directory(directory, utils.__is_clean_working_tree)