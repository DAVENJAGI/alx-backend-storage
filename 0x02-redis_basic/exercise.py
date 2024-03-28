#!/usr/bin/env python3
"""
Create cache class. In the __init__ method, stores an instance
"""
from redis import Redis
import uuid
from typing import Union


class Cache:
    '''class cache'''
    def __init__(self):
        '''initialize method'''
        self.__redis = Redis()
        self.__redis.flushdb()

    def store(self, data: [str, bytes, int, float]) -> str:
        '''generates a random key, stores the data in redis
        using random key and returns the key'''

        key = str(uuid.uuid4())
        self.__redis.mset({key: data})
        return key
