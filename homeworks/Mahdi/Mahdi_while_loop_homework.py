# Create a program that asks the user to enter a number until they enter zero.

# Start with a variable that allows the loop to run.
# Use while to check whether the number is not zero.
# Ask the user for another number inside the loop.
# When the user enters zero, stop the loop.
# Print a goodbye message after the loop.


number = 1

while number != 0:
    number = int(input("enter a number and enter 0 to stop: "))

print("goodbye")
