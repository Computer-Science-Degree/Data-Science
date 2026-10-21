from student_utils.analysis import calculate_average
from student_utils.cleaning import remove_missing_values

data = [10, 20, None, 40, 50]
cleaned_data = remove_missing_values(data)
average = calculate_average(cleaned_data)

print(f"original:: {data}")
print(f"Average: {average}")
print(f"Cleaned Data: {cleaned_data}")