# Problem: We need a program that shows a storage management system.
# The program should allow users to check stored products and their quantities,
# add products and quantities to storage, and remove product quantities from storage.
# It should also handle invalid inputs and wrong passwords
# to stop unauthorized users from entering the storage system, and
# ensure that users cannot remove more quantity than what is currently in storage
# or remove a product that does not exist.

# Instructions:
# First, we need a message that tells the user to enter the password.
# If the password is correct, then we will show the user the options to
# check storage, add a product, and remove a product.
# If the password is wrong, a message should say the password is invalid,
# tell the user to check the password, and try again.

# After entering the program successfully, 3 options will show to choose one of the options like below:
# Enter 1 to check the storage:
# Enter 2 to add a product to storage:
# Enter 3 to remove a product from storage:

# 1 - For checking the storage, the user will enter 1 and a message
# will be displayed showing all products and their current quantities in storage.
# 2 - If the user enters 2, a message will be displayed to enter
# the name of the product and the quantity to add. After entering them,
# if the product already exists, the quantity will be added to its current quantity;
# otherwise, the new product and its quantity will be added to storage.
# A message will be displayed that the product has been added successfully along with its new quantity.
# 3 - If the user enters 3, a message will be displayed to enter
# the name of the product and the quantity to remove.
# If the product exists and the quantity to remove is less than or equal to the available quantity,
# the removed quantity will be subtracted from the product's quantity, and a message will be
# displayed that the quantity has been removed successfully along with the new quantity.

# Algorithm: Storage Management System

# 1 - START

# 2 - Initialize variables:

#     set stored_password = 1234
#     set storage

# 3 - Allow user for entry:

#     display the message: "Please enter your password:"
#     check the user's input as entered_password

# 4 - Verify password:

#     if entered_password == stored_password, proceed to Step 5
#     else, display the message: "The password is invalid. Please check the password and try again."
#     and return to Step 3

# 5 - Display main menu:

#     display the following options to the user:
#     "Enter 1 to check the storage:"
#     "Enter 2 to add a product to storage:"
#     "Enter 3 to remove a product from storage:"
#     check the user's input choice = option

# 6 - Process User Selection:

#     if the choice is 1 (option == 1 — Check Storage):
#     display the message: "Current storage"
#     proceed to Step 7
#     elif the choice is 2 (option == 2 — Add Product):
#     display the message: "Enter the product name:"
#     check the input as product_name
#     display the message: "Enter the quantity to add:"
#     check the input as add_quantity
#     if product_name in storage:
#     add add_quantity to storage
#     display the message: "The product has been added successfully."
#     display the message: "New quantity of product_name"
#     proceed to Step 7
#     if the choice is 3 (option == 3 — Remove Product):
#     display the message: "Enter the product name to remove:"
#     check the input as product_name
#     if product_name in storage:
#     display the message: "Enter the quantity to remove:"
#     check the input as remove_quantity
#     subtract remove_quantity from storage
#     display the message: "The quantity has been removed successfully."
#     display the message: "New quantity of"
#     display the message: "Insufficient quantity in storage."
#     display the message: "Product not found in storage."
#     proceed to Step 7
#     display the message: "Invalid option selected. Please choose 1, 2, or 3."
#     return to Step 5

# 7 - STOP
