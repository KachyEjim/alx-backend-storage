#!/usr/bin/env python3
"""Inserts into a document"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection with attributes given as keyword arguments.

    Args:
        mongo_collection: The pymongo collection object to insert the document into.
        **kwargs: Key-value pairs representing the attributes of the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    args = mongo_collection.insert_one(kwargs)
    return args.inserted_id
