#!/usr/bin/env python3
"""
A function that returns a list of school having group
"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of school"""
    return mongo_collection.find{"topics": topic}
