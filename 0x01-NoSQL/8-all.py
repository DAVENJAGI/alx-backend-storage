#!/usr/bin/env python3
"""
A python script that lists all documents
"""


def list_all(mongo_collection):
    '''returns an empty list if no document in collection'''
    return mongo_collection.find()
