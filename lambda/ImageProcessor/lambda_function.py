import boto3
from PIL import Image

s3 = boto3.client('s3')

OUTPUT_BUCKET = "image-output-bucket-yash"

def lambda_handler(event, context):

    for record in event['Records']:

        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        download_path = "/tmp/input.jpg"
        upload_path = "/tmp/output.jpg"

        s3.download_file(bucket, key, download_path)

        img = Image.open(download_path)

        print("Original Size:", img.size)

        img = img.resize((300, 300))

        print("Resized Size:", img.size)

        img.save(upload_path)

        s3.upload_file(upload_path, OUTPUT_BUCKET, key)

    return {
        "statusCode": 200,
        "body": "Image Processed"
    }
