def extract_resources_from_tf_file(file_path):
    resources = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                if line.strip().startswith("resource"):
                    parts = line.split()
                    if len(parts) >= 3:
                        resource_type = parts[1].replace('"', '')
                        resources.append(resource_type)
    except FileNotFoundError:
        print(f"⚠️ File not found: {file_path}")
    return resources
