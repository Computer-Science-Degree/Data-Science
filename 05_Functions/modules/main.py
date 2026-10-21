from calculations import(
    calculate_average,
    calculate_total,
    find_highest
)

sales = [150, 200, 250, 300, 350]

# Total
total_sales = calculate_total(sales)
print(f"Total Sales: {total_sales}")

# Average
average_sales = calculate_average(sales)
print(f"Average Sales: {average_sales}")

# Highest
highest_sales = find_highest(sales)
print(f"Highest Sales: {highest_sales}")