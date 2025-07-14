import boto3
import os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client("s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_fileobj_to_s3(file_obj, s3_key):
    s3.upload_fileobj(file_obj, S3_BUCKET, s3_key)
    return generate_presigned_url(s3_key)

def list_photographer_images(prefix="photographer-uploads/"):
    objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
    keys = []
    for obj in objects.get("Contents", []):
        if obj["Key"].lower().endswith((".jpg", ".jpeg", ".png")):
            keys.append(obj["Key"])
    return keys

def download_image_from_s3(key):
    try:
        file_stream = BytesIO()
        s3.download_fileobj(Bucket=S3_BUCKET, Key=key, Fileobj=file_stream)
        file_stream.seek(0)
        return file_stream
    except Exception as e:
        print(f"Download error: {e}")
        return None

def generate_presigned_url(key, expiration=3600):
    return s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': S3_BUCKET, 'Key': key},
        ExpiresIn=expiration
    )
