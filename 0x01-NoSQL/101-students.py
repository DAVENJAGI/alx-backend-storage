#!/usr/bin/env python3
"""
A function that returns all students sorted by avg score
"""


def top_students(mongo_collection):
    '''
    The top must be sorted
    '''
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "average_score": {"$avg": "$topics.score"}
        }}
        {"$sort": {"average_score": -1}}
    ])
