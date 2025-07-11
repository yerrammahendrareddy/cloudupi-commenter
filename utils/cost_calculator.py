import json

def calculate_cost(file_path):
    with open(file_path) as f:
        resources = json.load(f)

    total_cost = 0
    breakdown = []

    for resource in resources.get("Resources", []):
        service = resource["Service"]
        config = resource["Config"]

        if service == "EC2":
            cost = 3800  # Example fixed price for t3.medium ap-south-1
        elif service == "S3":
            gb = config.get("StorageGB", 0)
            cost = gb * 8  # ₹8/GB
        else:
            cost = 0

        total_cost += cost
        breakdown.append(f"{service} ({config.get('Type', '')}): ₹{cost}/mo")

    return {
        "total": total_cost,
        "breakdown": breakdown
    }
