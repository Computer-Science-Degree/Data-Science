def remove_missing_values(values):
    return [
        value 
        for value in values
        if value is not None
    ]