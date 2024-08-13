#!/usr/bin/env python3
""" Provides stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    """
    Counts the number of data in a nginix log
    """
    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
