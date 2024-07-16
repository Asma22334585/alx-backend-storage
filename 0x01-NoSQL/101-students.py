#!/usr/bin/env python3
"""Top students """


def top_students(mongo_collection):
    """ all students sorted by average score """
    students_sorted = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return students_sorted
