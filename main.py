import json
import os
from utils.diff_parser import parse_diff
from utils.cost_calculator import estimate_cost
from utils.commenter import post_comment

REPO = os.getenv("GITHUB_REPOSITORY")
REF = os.getenv("GITHUB_REF", "")
TOKEN = os.getenv("GITHUB_TOKEN")
PR_NUMBER = REF.split("/")[-2] if "refs/pull/" in REF else None

if not PR_NUMBER:
    print("PR number not found.")
    exit(1)

infra_path = ".cloudupi/infra_diff.json"
if not os.path.exists(infra_path):
    print("Infra diff file not found.")
    exit(1)

with open(infra_path, "r") as f:
    diff_data = json.load(f)

resources = parse_diff(diff_data)
summary, cost = estimate_cost(resources)

comment = f"🧮 **CloudUPI Cost Estimator Summary:**\n\n{summary}\n\n**Total Estimated Cost:** ₹{cost}/mo"
post_comment(REPO, PR_NUMBER, comment, TOKEN)