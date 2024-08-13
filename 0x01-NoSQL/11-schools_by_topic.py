#!/usr/bin/env python3
"""Using find in pymongo"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of all school having a specific topic"""
    result = mongo_collection.find({"topics": {"$eq": topic}})
    return list(result)
