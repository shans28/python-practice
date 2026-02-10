from find_recent_error import most_frequent_error

def test_basic():
    logs = [
        "2024 INFO a ok",
        "2024 ERROR a failed",
        "2024 ERROR a failed",
        "2024 ERROR b timeout"
    ]
    assert most_frequent_error(logs) == "a failed"

