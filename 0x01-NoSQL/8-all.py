#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object to query.

    Returns:
        A list of all documents in the collection. Returns an empty list if the collection is empty.
    """
    documents = mongo_collection.find()

    return list(documents)
