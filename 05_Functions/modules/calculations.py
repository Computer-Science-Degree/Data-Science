def calculate_average(numbers):
    if not numbers:
        raise ValueError("Give at least one number.")
    return sum(numbers) / len(numbers)

def calculate_total(numbers):
    return sum(numbers)

def find_highest(numbers):
    if not numbers:
        raise ValueError("Give at least one number.")
    return max(numbers)

if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    
    total = calculate_total(sample_numbers)
    average = calculate_average(sample_numbers)
    highest = find_highest(sample_numbers)
    
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest: {highest}")