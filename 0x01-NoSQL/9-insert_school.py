#!/usr/bin/env python3
"""
Insert a new document
"""

def insert_school(mongo_collection, **kwargs):
    '''inserts new document in a collection'''
    newDocu = mongo_collection(insertOne(kwargs))
    return newDocu.insertedId
