import pygit

assert pygit.get_repo() == None
assert pygit.set_repo('/home/denhofja/MMVAE/') == None
assert pygit.get_repo() == '/home/denhofja/MMVAE/'
assert isinstance(pygit.get_last_commit_hash(), str)
assert isinstance(pygit.get_num_commits(), int)
assert isinstance(pygit.is_clean_working_tree(), bool)
print("All tests passed")