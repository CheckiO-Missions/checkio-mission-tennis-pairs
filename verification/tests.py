"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3, 4]],
            "answer": 0,
        },
        {
            "input": [[5, 5, 5, 5]],
            "answer": 0,
        },
        {
            "input": [[1, 9, 3, 2]],
            "answer": 5,
        }
    ],
    "Extra": [
        {
            "input": [[15, 10, 35, 25]],
            "answer": 5,
        },
        {
            "input": [[12, 10, 1, 13]],
            "answer": 8,
        },
        {
            "input": [[11, 12, 10, 11]],
            "answer": 0,
        },
    ]
}
