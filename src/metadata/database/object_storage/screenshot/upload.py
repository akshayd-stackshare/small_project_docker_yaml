from io import BytesIO

import settings
from src.data_infrastructure.minio.shared.upload import upload_file_like_to_minio


def screenshot_upload_to_minio(data, bucket_name=settings.SCREENSHOT_BUCKET, object_name=None):
    return upload_file_like_to_minio(data=data, bucket_name=bucket_name, object_name=object_name)


if __name__ == '__main__':
    FILE_NAME = str(settings.SCREENSHOT_DIR / '.png')
    BUCKET_NAME = settings.SCREENSHOT_BUCKET
    OBJECT_NAME = "testing.png"
    with open(FILE_NAME, 'rb') as file:
        DATA = BytesIO(file.read())
        upload_file_like_to_minio(data=DATA, bucket_name=BUCKET_NAME, object_name=OBJECT_NAME)
