def build_comment(cost_data):
    comment = "🧮 CloudUPI Cost Estimator Summary:\n\n"
    for line in cost_data["breakdown"]:
        comment += f"• {line}\n"
    comment += f"\nTotal Estimated Cost: ₹{cost_data['total']}/mo"
    return comment
