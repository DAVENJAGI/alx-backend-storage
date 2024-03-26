#!/usr/bin/env python3
"""
Changes all topics of school document
"""


def update_topics(mongo_collection, name, topics):
    '''Updates topics'''
    mongo_collection.update_any({'name': name}, {$set: {'topics': topics}})
