#!/usr/bin/env python3
"""
Changes all topics of school document
"""


def update_topics(mongo_collection, name, topics):
    """Updates topics based on school name"""
    mongo_collection.updateMany({'name': name}, {$set: {'topics': topics}})
