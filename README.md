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
export OPEN_AI_KEY=<insert key>
docker run -e OPEN_AI_KEY --rm iac-gitlab-bot --repo-url <repository-url> --commit-sha1 <commit-sha1> --commit-sha2 <commit-sha2>
```

## Example Usage
```docker run -e OPENAI_API_KEY --rm iac-gitlab-bot --repo-url=https://github.com/charlesastokes/IaC-Gitlab-Bot.git --commit-sha1=8fdd6a9d3c16847b11c33f5459fa80e6511f9dfe --commit-sha2=eabf5dbeae6e4ac7ab9058a164e38283cf71ed66```

Additional Example using IAM policy change:
```
docker run -e OPENAI_API_KEY --rm iac-gitlab-bot --repo-url=https://github.com/charlesastokes/ExampleTerraformChanges.git --commit-sha1=129340e322cb26d3a93072738bbf0df0f68fb47d --commit-sha2=23e1ca1684c03e5813106134f0e0457a2d0df244
```
## Additional Options

To include debugging output, add the option `--bot-debug-info=true`

## Output

The output is in Markdown format, and is intended to be used either as a pipeline step or post-merge request action for a bot to comment on merge requests

## Future Plans

Currently this project is very simple, although there are many ways it can be improved and extended. The code was intentionally designed agnostic of any particular source code management platform such as Gitlab or Github, and instead utilizes native Git functionality. Becuase of this it can be used in various automated scenarios.

This project was written in just a few hours during a busy Hack Day event. Some ideas of where this was intended to go include determining source code graph structure, and using OpenTofu in a container to test which subfolders are valid Terraform/OpenTofu modules even in a mono-repo structure using deterministic, non-AI methods, then feeding that source graph and code into an LLM for analysys. This would solve the problem of models not getting proper context related to IaC codebases which are often mono-repos with repetitive file names which can confuse LLMs or cause context window degredation across many files.
