#!/usr/bin/env python3
"""Update a document in pymonogo"""


def update_topics(mongo_collection, name, topics):
    """Updates a school document with a new list of topics

    Args:
        mongo_collection: The pymongo collection object to update in.
        name (str): The name of the school to update.
        topics (list): The new list of topics to set.

    Returns:
        The result of the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
