#!/usr/bin/env python3
"""Shebang script"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
