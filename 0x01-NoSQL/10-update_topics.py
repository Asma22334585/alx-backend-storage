#!/usr/bin/env python3
"""changes all topics """


def update_topics(mongo_collection, name, topics):
    """update name and topic"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
