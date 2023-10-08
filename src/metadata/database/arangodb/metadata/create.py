from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb
from src.system.models.urls import URLMetadata


def write_url_metadata_to_arango(url_metadata: URLMetadata):
    write_pydantic_to_arangodb(url_metadata)


if __name__ == '__main__':
    from datetime import datetime

    # test with URLMetadtat
    sample_data_url = URLMetadata(url="http://example.com",
                              screenshot_path="/path/to/screenshot",
                              har_path="/path/to/har",
                              html_path="/path/to/html",
                              utc_time=datetime.utcnow())

    write_url_metadata_to_arango(sample_data_url)