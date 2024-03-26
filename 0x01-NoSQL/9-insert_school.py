#!/usr/bin/env python3
"""
Insert a new document
"""


def insert_school(mongo_collection, **kwargs):
    '''inserts new document in a collection'''
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
