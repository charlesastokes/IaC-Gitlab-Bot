def print_diff(repo, commit_sha1, commit_sha2):
    print(f"Creating diff between {commit_sha1} and {commit_sha2}")
    diff = repo.git.diff(commit_sha1, commit_sha2)
    print("Diff between commits:")
    print(diff)
