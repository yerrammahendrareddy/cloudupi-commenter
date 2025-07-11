COST_MAP = {
    "aws_instance": 25.0,
    "aws_lambda_function": 2.0,
    "aws_s3_bucket": 5.0,
    "aws_dynamodb_table": 15.0,
}

def estimate_cost_from_resources(resources):
    total = 0
    for res in resources:
        total += COST_MAP.get(res, 1.0)
    return total
