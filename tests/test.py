import pygit.pygit as pygit
pygit.set_repo('/home/denhofja/MMVAE/')
print(pygit.get_last_commit_hash())