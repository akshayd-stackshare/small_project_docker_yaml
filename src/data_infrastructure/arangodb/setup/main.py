from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb

__info__ = """
The main here attempts to write pydantic data models to the DB
if the collection for a data model doesn't exist it creates one
"""

from src.system.models.errors import ScrapeError
from src.system.models.urls import URLMetadata

if __name__ == '__main__':
    from datetime import datetime

    # test with URLMetadtat
    sample_data = URLMetadata(url="http://example.com",
                              screenshot_path="/path/to/screenshot",
                              har_path="/path/to/har",
                              html_path="/path/to/html",
                              utc_time=datetime.utcnow())

    write_pydantic_to_arangodb(sample_data)

    # Test with ScrapeError
    sample_data_scrapeerror = ScrapeError(
        url="http://error.com",
        err_type="404",
        err_msg="Page Not Found",
        utc_time=datetime.utcnow()
    )

    write_pydantic_to_arangodb(sample_data_scrapeerror)

    print("Data written to ArangoDB!")
