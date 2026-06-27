import boto3
import json

s3 = boto3.client("s3")

BUCKET_NAME = "image-output-bucket-yash"   # Replace with your output bucket name

def lambda_handler(event, context):

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "No images found"})
        }

    latest = response["Contents"][-1]["Key"]

    url = f"https://{BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{latest}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "image": latest,
            "url": url
        })
    }