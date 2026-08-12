from github import Github
import os

class GitHubIntegration:
    """
    Handles autonomous cloning, issue parsing, and PR creation.
    """
    def __init__(self, token: str = None):
        self.token = token or os.getenv("GITHUB_PAT")
        if not self.token:
            print("Warning: GITHUB_PAT not set. Operating in read-only/mock mode.")
        self.client = Github(self.token)

    def fetch_issue(self, repo_name: str, issue_number: int) -> dict:
        try:
            repo = self.client.get_repo(repo_name)
            issue = repo.get_issue(number=issue_number)
            return {
                "title": issue.title,
                "body": issue.body,
                "state": issue.state
            }
        except Exception as e:
            return {"error": str(e)}

    def create_pull_request(self, repo_name: str, branch: str, title: str, body: str):
        print(f"[GitHub] Creating PR for {repo_name} on branch {branch}...")
        if not self.token:
            print("[GitHub] Mock PR created (Authentication required for real PR).")
            return
            
        repo = self.client.get_repo(repo_name)
        try:
            pr = repo.create_pull(title=title, body=body, head=branch, base="main")
            print(f"[GitHub] PR created successfully: {pr.html_url}")
        except Exception as e:
            print(f"[GitHub] Error creating PR: {e}")
