import boto3

import settings


def get_connection():
    # Create a session
    session = boto3.session.Session()
    # Create an S3 client
    s3_client = session.client(
        's3',
        region_name='us-east-1',
        endpoint_url=f'http://{settings.MINIO_HOST}:9000',  # replace with your MinIO endpoint
        aws_access_key_id=settings.MINIO_ACCESS_KEY,  # replace with your MinIO access key
        aws_secret_access_key=settings.MINIO_SECRET_KEY,  # replace with your MinIO secret key
        config=boto3.session.Config(signature_version='s3v4')
    )
    return s3_client
