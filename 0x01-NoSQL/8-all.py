#!/usr/bin/env python3
"""lists all documents"""


def list_all(mongo_collection):
    """
    empty list if no document in the collection
    """
    return list(mongo_collection.find())
