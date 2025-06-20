import argparse
from git import Repo
from pydantic_ai_agent import summarize_iac_changes

def main():
    parser = argparse.ArgumentParser(description="IaC-Gitlab-Bot")
    parser.add_argument('--repo-url', type=str, help='URL of the Git repository to clone')
    parser.add_argument('--commit-sha1', type=str, help='First commit SHA for diff without proposed changes')
    parser.add_argument('--commit-sha2', type=str, help='Second commit SHA for diff with proposed changes')
    parser.add_argument('--bot-debug-info', type=bool, help='Second commit SHA for diff with proposed changes')
    args = parser.parse_args()
    if args.bot_debug_info:
        print(f"Cloning repository: {args.repo_url}")
    # Clone the repository using GitPython
    clone_dir = "./repo_clone"
    cloned_repo = Repo.clone_from(args.repo_url, clone_dir)
    if args.bot_debug_info:
        print(f"Repository cloned to {clone_dir}")
    # Make sure both commit shas exist in the cloned repository
    if not cloned_repo.commit(args.commit_sha1):
        raise ValueError(f"Commit SHA1 {args.commit_sha1} does not exist in the repository.")
    if not cloned_repo.commit(args.commit_sha2):
        raise ValueError(f"Commit SHA2 {args.commit_sha2} does not exist in the repository.")
    if args.bot_debug_info:
        print("Commit Shas exist in the repository.\n\n")

    #Determine Diff
    if args.bot_debug_info:
        print(f"Creating diff between {args.commit_sha1} and {args.commit_sha2}")
    diff = cloned_repo.git.diff(args.commit_sha1, args.commit_sha2)

    summarize_iac_changes(diff)

if __name__ == "__main__":
    main()
