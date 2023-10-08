import io
import os

import settings
from src.data_infrastructure.minio.shared.upload import upload_file_like_to_minio


def har_upload_to_minio(file_path, bucket_name=settings.HAR_BUCKET, object_name=None, delete=True):
    with open(file_path, 'rb') as file:
        data = io.BytesIO(file.read())
        har_object_path = upload_file_like_to_minio(data=data, bucket_name=bucket_name, object_name=object_name)

    # cleanup
    if delete:
        os.remove(file_path)

    return har_object_path


if __name__ == '__main__':
    OBJECT_NAME = 'testing.har'
    FILE_PATH = str(settings.HAR_DIR / '.har')
    har_upload_to_minio(file_path=FILE_PATH, object_name=OBJECT_NAME, delete=False)
