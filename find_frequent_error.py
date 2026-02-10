logs = [
    "2024-01-01 INFO auth User logged in",
    "2024-01-01 ERROR payment Payment failed",
    "2024-01-01 ERROR payment Payment failed",
    "2024-01-01 ERROR auth Invalid token",
    "2024-01-01 INFO payment Payment started"
]

def most_frequent_error(logs):
    error_counts = {}
    
    for log in logs:
        if "ERROR" in log:
            error_message = log.split("ERROR")[1].strip()
            if error_message in error_counts:
                error_counts[error_message] += 1
            else:
                error_counts[error_message] = 1
    print(error_counts)
    most_frequent = max(error_counts, key=error_counts.get)
    return most_frequent
    
most_frequent_error(logs)