def parse_diff(diff_data):
    resources = []
    for change in diff_data.get("changes", []):
        if change["type"] == "resource" and change["action"] in ["add", "modify"]:
            res = change["data"]
            resources.append(res)
    return resources