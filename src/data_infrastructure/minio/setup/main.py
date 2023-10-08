from minio import Minio
from minio.error import S3Error

import settings


def setup_minio_buckets(bucket_names, endpoint, access_key, secret_key, secure=False):
    # Create the MinIO client
    client = Minio(
        endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure
    )

    # Iterate over bucket names and attempt to create each
    for bucket in bucket_names:
        try:
            if not client.bucket_exists(bucket):
                client.make_bucket(bucket)
                print(f"Bucket {bucket} created successfully.")
            else:
                print(f"Bucket {bucket} already exists.")
        except S3Error as exc:
            # Check for a specific error code (e.g., "BucketAlreadyOwnedByYou")
            if exc.code == "BucketAlreadyOwnedByYou":
                print(f"Bucket {bucket} already owned by you.")
            else:
                print(f"Failed to create bucket {bucket}. Error: {exc}")


if __name__ == "__main__":
    buckets_to_create = [settings.HAR_BUCKET,
                         settings.SCREENSHOT_BUCKET,
                         settings.HTML_BUCKET]

    setup_minio_buckets(
        buckets_to_create,
        endpoint="localhost:9000",
        access_key="minioaccesskey",
        secret_key="miniosecretkey"
    )
