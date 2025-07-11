import os
from utils.git_diff_utils import get_changed_tf_files
from parser.terraform_parser import extract_resources_from_tf_file
from pricing_utils import estimate_cost_from_resources
from comment_utils import post_comment

REPO = os.getenv("GITHUB_REPOSITORY")
REF = os.getenv("GITHUB_REF", "")
TOKEN = os.getenv("GITHUB_TOKEN")
PR_NUMBER = REF.split("/")[-2] if "refs/pull/" in REF else None

if not PR_NUMBER:
    print("❌ PR number not found.")
    exit(1)

base_ref = os.getenv("GITHUB_BASE_REF")
head_ref = os.getenv("GITHUB_HEAD_REF")
if not base_ref or not head_ref:
    print("❌ Base or head ref not found.")
    exit(1)

print(f"🔍 Comparing changes from {base_ref} to {head_ref}...")

changed_files = get_changed_tf_files(base_ref, head_ref)
all_resources = []

for tf_file in changed_files:
    resources = extract_resources_from_tf_file(tf_file)
    all_resources.extend(resources)

estimated_cost = estimate_cost_from_resources(all_resources)
comment = f"🧮 CloudUPI Cost Estimate: **${estimated_cost:.2f}/mo** (based on modified infra)"
post_comment(PR_NUMBER, comment, REPO, TOKEN)
