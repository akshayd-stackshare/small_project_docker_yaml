import io

import settings
from src.data_infrastructure.minio.shared.upload import upload_file_like_to_minio


def html_upload_to_minio(data, bucket_name=settings.HTML_BUCKET, object_name=None):
    return upload_file_like_to_minio(data=data, bucket_name=bucket_name, object_name=object_name)


if __name__ == '__main__':
    OBJECT_NAME = 'testing.html'
    DATA = io.StringIO("Hello from StringIO!")
    html_upload_to_minio(data=DATA, object_name=OBJECT_NAME)