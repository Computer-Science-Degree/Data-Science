def calculate_average(values):
    if not values:
        raise ValueError("No Values to analyze")
    return sum(values) / len(values)