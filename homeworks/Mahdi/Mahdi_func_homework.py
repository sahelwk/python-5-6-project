def welcome_message():
    print("Welcome to Python!")
    print("We are happy to have you here.")


welcome_message()

welcome_message()
welcome_message()
welcome_message()


# Parameters and Arguments
def show_student(name, age, city):
    print("----------------")
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("----------------")


show_student("Ahmad", 20, "Kabul")

show_student("Ali", 22, "Herat")


# Return Value
def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    return total_salary


salary = calculate_salary(5000, 1000)

print("Total Salary:", salary)

annual_salary = salary * 12

print("Annual Salary:", annual_salary)


# Keyword Arguments


def calculate_salary(basic_salary, bonus=0):
    total_salary = basic_salary + bonus
    return total_salary


salary1 = calculate_salary(5000, 1000)

salary2 = calculate_salary(5000)

print("Salary with bonus:", salary1)
print("Salary without bonus:", salary2)

# Scope

shop_name = "Sahel Store"


def show_product():

    product = "Laptop"
    print("Shop Name:", shop_name)
    print("Product:", product)

show_product()
print("Shop Name:", shop_name)
