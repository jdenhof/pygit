from .registry import register_command
import subprocess

@register_command
def get_last_commit_hash(repository: str = None):
    return subprocess.run(
        ['git', 'rev-parse', 'HEAD'], 
        check=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    ).stdout.strip()

@register_command
def get_num_commits(repository: str = None):
    return int(subprocess.run(
        ["git", "rev-list", "--all", "--count"], 
        capture_output=True, 
        text=True
    ).stdout.strip())

@register_command
def is_clean_working_tree(repository: str = None):
    return bool("nothing to commit, working tree clean" in subprocess.run(
        ["git", "status"], 
        capture_output=True, 
        text=True
    ).stdout.strip())
    

    
    