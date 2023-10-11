from pydantic import BaseModel

from src.data_infrastructure.arangodb.connection.utils import get_db


def write_pydantic_to_arangodb(pydantic_obj: BaseModel, conn=None):
    # Get the collection name from the pydantic object's name
    collection_name = f"{pydantic_obj.__class__.__name__}Collection"

    db = get_db(conn)

    # Check if the collection exists, if not, create it
    if not db.hasCollection(collection_name):
        db.createCollection(name=collection_name)

    # Get the collection and save the document
    collection = db[collection_name]
    data = pydantic_obj.model_dump()
    document = collection.createDocument(data)
    document.save()
