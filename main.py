from utils.cost_estimator import estimate_cost_change
from utils.commenter import post_comment
import os

if __name__ == "__main__":
    pr_number = os.getenv("PR_NUMBER", "1")
    base_commit = os.getenv("BASE_COMMIT", "")
    head_commit = os.getenv("HEAD_COMMIT", "")

    cost_summary = estimate_cost_change(base_commit, head_commit)
    post_comment(pr_number, cost_summary)