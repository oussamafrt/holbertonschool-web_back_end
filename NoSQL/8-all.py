#!/usr/bin/env python3
"""Shebang script"""

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school

def list_all(mongo_collection):
    """ lists all documents in a collection """
    return [doc for doc in mongo_collection.find()]
