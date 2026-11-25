# Create a program that prints a multiplication table from 1 to 5.

# Use an outer loop for numbers 1 to 5.
# Use an inner loop for multipliers 1 to 10.
# Calculate the multiplication result.
# Print each multiplication expression.
# Separate each number's table with a blank line.

for number in range(1, 11):

    for multi in range(1, 11):
        result = number * multi
        print(number, "x", multi, "=", result)

    print("===============")
