# Create a program that searches for a specific number in a list and stops when the number is found.

# Create a list of numbers.
# Choose a number to search for.
# Use a for loop to check each number.
# Print a message when the number is found.
# Use break to stop searching.

numbers = [1, 2, 3, 4, 5]

search = 8

for number in numbers:
    if number == search:
        print("number is found", search)
        break

else:
    print("number is not found", search)
