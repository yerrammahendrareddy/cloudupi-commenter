
import os
import requests

REPO = os.getenv("GITHUB_REPOSITORY")
REF = os.getenv("GITHUB_REF", "")
TOKEN = os.getenv("GITHUB_TOKEN")
PR_NUMBER = REF.split("/")[-2] if "refs/pull/" in REF else None

def post_comment(pr_number, comment):
    url = f"https://api.github.com/repos/{REPO}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.post(url, headers=headers, json={"body": comment})
    if response.status_code == 201:
        print("✅ Comment posted successfully!")
    else:
        print(f"Failed to post comment: {response.status_code}, {response.text}")

if __name__ == "__main__":
    if not PR_NUMBER:
        print("PR number not found.")
    else:
        post_comment(PR_NUMBER, "🧮 CloudUPI Cost Estimate: ₹12,000/mo (estimated)")
