#!/usr/bin/env python3
"""Provides stats about Nginix logs stored in a mongodb"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.logs
    nginx_collection = db.nginx
    total = nginx_collection.count_documents({})
    get = nginx_collection.count_documents({"method": {"$eq": "GET"}})
    post = nginx_collection.count_documents({"method": {"$eq": "POST"}})
    put = nginx_collection.count_documents({"method": {"$eq": "PUT"}})
    patch = nginx_collection.count_documents({"method": {"$eq": "PATCH"}})
    delete = nginx_collection.count_documents({"method": {"$eq": "DELETE"}})
    status = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print(
        f"methods:\n\tmethod GET: {get}\n\tmethod POST: {post}\n\tmethod PUT: {put}\n\tmethod PATCH: {patch}\n\tmethod DELETE: {delete}\n{status} status check"
    )
