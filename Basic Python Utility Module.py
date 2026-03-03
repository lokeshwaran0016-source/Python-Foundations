
# BASIC ARITHMETIC OPERATIONS


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b



# TEMPERATURE CONVERSION


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273



# AREA CALCULATIONS


def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height



# BASIC BANKING OPERATIONS


def create_account(name, balance):
    account = {"name": name, "balance": balance}
    return account

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient balance"
    return balance - amount



# STUDENT ACADEMIC RESULTS


def calculate_total(marks_list):
    return sum(marks_list)

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


# TESTING THE FUNCTIONS


print("Addition:", add(10, 5))
print("Celsius to Fahrenheit:", celsius_to_fahrenheit(30))
print("Circle Area:", circle_area(5))

account = create_account("Lokesh", 1000)
print("Account Created:", account)

new_balance = deposit(account["balance"], 500)
print("Balance after Deposit:", new_balance)

marks = [80, 70, 90]
total = calculate_total(marks)
average = calculate_average(marks)

print("Total Marks:", total)
print("Average:", average)
print("Grade:", assign_grade(average))
