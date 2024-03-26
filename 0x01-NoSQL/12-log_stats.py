#!/usr/bin/env python3
"""
A script that provides statas about some nginx logs
stored in MongoDB
"""
from pymongo import MongoClient

def log_stats():
    """log stats of nginx"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logsCollection = client.logs.nginx
    total = logsCollection.count_documents({})
    get = logsCollection.count_documents({"method": "GET"})
    post = logsCollection.count_documents({"method": "POST"})
    put = logsCollection.count_documents({"method": "PUT"})
    patch = logsCollection.count_documents({"method": "PATCH"})
    delete = logsCollection.count_documents({"method": "DELETE"})
    path = logsCollection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
