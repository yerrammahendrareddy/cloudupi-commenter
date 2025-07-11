# Placeholder for real pricing logic
def get_price(resource):
    if resource["type"] == "EC2":
        return 3800
    elif resource["type"] == "S3":
        return 400
    else:
        return 100