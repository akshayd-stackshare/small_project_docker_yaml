from pyArango.connection import Connection

import settings


def get_db(conn=None):
    if not conn:
        # Connect to ArangoDB server if no connection is provided
        conn = Connection(username="root", password="rootpassword", arangoURL=settings.ARANGO_HOST)  # replace with your credentials

    # Create a new database if it doesn't exist
    if not conn.hasDatabase("url_fetcher_service"):
        conn.createDatabase(name="url_fetcher_service")

    # Switch to the new database
    db = conn["url_fetcher_service"]

    # Create a new collection if it doesn't exist
    # todo: a list of collections to create
    if not db.hasCollection("MetadataCollection"):
        db.createCollection(name="MetadataCollection")

    return db