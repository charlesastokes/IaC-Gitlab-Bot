import argparse
from git import Repo

def main():
    parser = argparse.ArgumentParser(description="IaC-Gitlab-Bot")
    parser.add_argument('--repo-url', type=str, help='URL of the Git repository to clone')
    parser.add_argument('--commit-sha1', type=str, help='First commit SHA for diff without proposed changes')
    parser.add_argument('--commit-sha2', type=str, help='Second commit SHA for diff with proposed changes')
    args = parser.parse_args()

    print(f"Cloning repository: {args.repo_url}")
    # Clone the repository using GitPython
    clone_dir = "./repo_clone"
    Repo.clone_from(args.repo_url, clone_dir)
    print(f"Repository cloned to {clone_dir}")
    print(f"Creating diff between {args.commit_sha1} and {args.commit_sha2}")

if __name__ == "__main__":
    main()
