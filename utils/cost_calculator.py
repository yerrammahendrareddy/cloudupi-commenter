def estimate_cost(resources):
    total_cost = 0
    summary_lines = []

    for res in resources:
        cost = 0
        if res["service"] == "ec2":
            instance = res["instance_type"]
            region = res["region"]
            if instance == "t3.medium" and region == "ap-south-1":
                cost = 3800
            summary_lines.append(f"• EC2 ({instance}, {region}): ₹{cost}/mo")

        elif res["service"] == "s3":
            storage_gb = res["storage_gb"]
            cost = storage_gb * 8  # ₹8 per GB
            summary_lines.append(f"• S3 ({storage_gb} GB, Standard): ₹{cost}/mo")

        total_cost += cost

    return "\n".join(summary_lines), total_cost