from src.data_infrastructure.arangodb.shared.pydantic.write import write_pydantic_to_arangodb
from src.system.models.errors import ScrapeError


def write_error_to_arango(err_data: ScrapeError):
    write_pydantic_to_arangodb(err_data)


if __name__ == '__main__':
    from datetime import datetime

    # Test with ScrapeError
    sample_data_scrapeerror = ScrapeError(
        url="http://error2.com",
        err_type="404",
        err_msg="Page Not Found",
        utc_time=datetime.utcnow()
    )
