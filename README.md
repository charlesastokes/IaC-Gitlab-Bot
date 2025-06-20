# IaC-Gitlab-Bot

This project is designed to run as a standalone containerized application.
It leverages Python for executing key logic and Git for version control operations.
Key operations include:
  - Cloning a Git repository based on a provided URL.
  - Creating a diff between two commit SHAs.
  - Executing IaC operations using OpenTofu (a Terraform-compatible tool).

The Docker container encapsulates the required environment, ensuring reproducible builds with both Python and Git installed.
All Python logic is located in the `python/` folder.

## Usage

To build and run the container, execute:

```bash
docker build -t iac-gitlab-bot .
docker run --rm iac-gitlab-bot
```

Feel free to extend and modify the project as needed.
