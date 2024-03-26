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
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
