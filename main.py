import os
import boto3
import random
import base64
from botocore.config import Config
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    print(event)
    if event["requestContext"]["http"]["method"] == "GET":
        try:
            return get_random_photo_html()
        except Exception as e:
            return {"statusCode": 500, "body": f"Error: {str(e)}"}
    elif event["requestContext"]["http"]["method"] == "POST":
        try:
            if event.get("isBase64Encoded", False):
                image_data = base64.b64decode(event["body"])
            else:
                image_data = event["body"].encode("utf-8")
            return upload_photo(image_data)
        except Exception as e:
            return {"statusCode": 500, "body": f"Error: {str(e)}"}


def get_random_photo_html():
    try:
        image_url = get_random_image_s3()
    except Exception as e:
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

    # read the html template from index.html
    with open("index.html", "r") as file:
        html_template = file.read()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_template.replace("{image_url}", image_url),
    }


def upload_photo(photo_file):
    bucket = os.environ["IMAGES_BUCKET"]
    config = Config(signature_version="s3v4")
    s3 = boto3.client("s3", config=config)

    # Check if the file is an image
    # if not photo_file.startswith(b"\xff\xd8") and not photo_file.startswith(b"\x89PNG"):
    # return {"statusCode": 400, "body": "Error: Uploaded file is not a valid image"}

    try:
        # Generate a unique filename
        filename = f"{random.randint(1000000, 9999999)}.jpg"
        s3.put_object(Bucket=bucket, Key=filename, Body=photo_file)
        return {"statusCode": 200, "body": "OK"}
    except Exception as e:
        return {"statusCode": 500, "body": f"Error uploading photo: {str(e)}"}


def get_random_image_s3():
    bucket = os.environ["IMAGES_BUCKET"]
    config = Config(signature_version="s3v4")
    s3 = boto3.client("s3", config=config)

    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket)

        # Filter for image files
        image_keys = [
            obj["Key"]
            for obj in response.get("Contents", [])
            if obj["Key"].lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        if not image_keys:
            image_url = "https://images.unsplash.com/photo-1605054576990-8d1d1e623fad?q=80&w=2340&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        else:
            random_image_key = random.choice(image_keys)

            image_url = s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": bucket, "Key": random_image_key},
                ExpiresIn=300,
            )

        return image_url
    except Exception as e:
        raise Exception(f"Error retrieving random image: {str(e)}")
