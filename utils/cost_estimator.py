from .aws_pricing_engine import get_price
from .file_diff_parser import parse_diff

def estimate_cost_change(base_commit, head_commit):
    modified_resources = parse_diff(base_commit, head_commit)
    total_cost = 0
    breakdown = []
    for resource in modified_resources:
        cost = get_price(resource)
        breakdown.append(f"  - {resource['type']} ({resource['config']}): ₹{cost}/mo")
        total_cost += cost

    summary = f"🧮 CloudUPI Cost Estimator Summary:\n\n• Monthly AWS Cost Impact: ₹{total_cost}/mo\n• Breakdown:\n" + "\n".join(breakdown)
    return summary