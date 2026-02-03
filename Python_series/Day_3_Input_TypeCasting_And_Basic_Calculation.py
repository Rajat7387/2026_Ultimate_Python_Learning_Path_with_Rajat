# what us input() function in python?
# The input() function in Python is used to take input from the user. When this function is called,
# the program waits for the user to type something and press the Enter key. The input provided  
# 
#Tecnically, the input() function reads a line from input, converts it into a string (stripping any 
# trailing newline), and returns that.  
# 
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello,", name, "you are", age, "years old")  

# in input function is always treated as a string.


# Typecasting in python:
# Typecasting is the process of converting a variable from one data type to another.
# In Python, you can use built-in functions to perform typecasting. Some common typecasting functions include:
# int(): Converts a value to an integer.
# float(): Converts a value to a floating-point number.
# str(): Converts a value to a string.
# bool(): Converts a value to a Boolean (True or False). 

# Example of typecasting:
# converting string to integer:

# age = input("Enter your age: ")  # input() returns a string
# age = int(age)  # typecasting string to integer
# print("Your age is:", age)
# print("Type of age before typecasting:", type(age))

# temperature = input("Enter the temperature in Celsius: ")
# temperature = float(temperature)  # typecasting string to float
# print(type(temperature))


# Convert number to string:
# sales = 10000
# total_sales = "The total sales is " + str(sales)
# print(total_sales)
# print(type(total_sales))

# exampele 1:
# product = input("Enter the product name: ")
# quantity = input("Enter the quantity: ")
# price_per_item = input("Enter the price per item: ")

# total_sales = int(quantity) * float(price_per_item)

# print ("Product:", product)
# print("Total sales amount is:", total_sales)    


# example 2:

# num1 = 20 
# num2 = 30
# sum = num1 + num2
# print(sum)


# Assignment 1:
# make a Salary slip Calculation :

# employee_name = input("Enter the employee name: ")
# basic_salary = float(input("Enter the basic salary: "))
# bonus_amount = float(input("Enter the bonus amount: "))
# tax_percentage = float(input("Enter the tax percentage: "))

# # Ccalculate 
# gross_salary = basic_salary + bonus_amount
# tax_amount = (tax_percentage / 100) * gross_salary
# net_salary = gross_salary - tax_amount
# print("Employee Name:", employee_name)
# print("Gross Salary:", gross_salary)
# print("Tax Amount:", tax_amount)
# print("Net Salary:", net_salary)


# Assignment 2:
# item = input("Enter the item name: ")
# price = float(input("Enter the price of the item: "))
# discount_percentage = float(input("Enter the discount percentage: "))

# # Calculate
# discount_amount = (discount_percentage / 100) * price
# final_price = price - discount_amount

# print("Item Name:", item)
# print("Original Price:", price)
# print("Discount Amount:", discount_amount)
# print("Final Price:", final_price)

# print("Final Price of", item, "after", discount_percentage, "% discount is:", final_price)





