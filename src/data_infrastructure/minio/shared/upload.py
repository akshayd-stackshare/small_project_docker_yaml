import io
from botocore.exceptions import NoCredentialsError, BotoCoreError, ClientError
from src.data_infrastructure.minio.connection.utils import get_connection


def upload_file_like_to_minio(data, object_name, bucket_name):
    """
    Uploads data (either StringIO or BytesIO) to a specified MinIO bucket.

    Args:
    - data (io.StringIO or io.BytesIO): The data to be uploaded.
    - object_name (str): The name of the object in the MinIO bucket.
    - bucket_name (str): The name of the MinIO bucket.
    """

    s3_client = get_connection()

    # Check if data is of type StringIO, if so convert to BytesIO
    if isinstance(data, io.StringIO):
        data = io.BytesIO(data.getvalue().encode())

    try:
        # Upload the data to MinIO using s3_client
        s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=data)
        print(f"Data uploaded successfully to {object_name} in {bucket_name}")
        return f"{bucket_name}/{object_name}"

    except (BotoCoreError, ClientError) as error:
        print(f"An error occurred while uploading: {error}")


def upload_file_to_minio(file_name, bucket_name, object_name=None):
    # If object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    s3_client = get_connection()

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"Uploaded {file_name} as {object_name} in {bucket_name}")
    except FileNotFoundError:
        print(f"{file_name} not found")
    except NoCredentialsError:
        print("Credentials not available")


if __name__ == "__main__":
    # upload_file_to_minio("path/to/your/local/file.txt", "your-bucket-name")
    data_str = io.StringIO("Hello from StringIO!")
    upload_file_like_to_minio(data_str, "string_io_object.txt", "html")

    data_bytes = io.BytesIO(b"Hello from BytesIO!")
    upload_file_like_to_minio(data_bytes, "bytes_io_object.txt", "html")
