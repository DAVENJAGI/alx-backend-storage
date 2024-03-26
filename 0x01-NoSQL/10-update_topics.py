#!/usr/bin/env python3
"""
Changes school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Updates topics based on school name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
