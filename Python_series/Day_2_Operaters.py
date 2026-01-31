# What is Operaters in Python?
# Operators in Python are special symbols or keywords that perform operations on one or more operands (values or variables) to produce a result. 
# Python supports various types of operators, including:

# 1. Arithmetic Operators:
# These operators perform basic mathematical operations.
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division
# % : Modulus (remainder)
# ** : Exponentiation (power)
# // : Floor Division (quotient without the decimal part)

# num1 = 10
# num2 = 3        
# print("Addition:", num1 + num2)       
# print("Subtraction:", num1 - num2)    
# print("Multiplication:", num1 * num2)  
# print("Division:", num1 / num2)        
# print("Modulus:", num1 % num2)         
# print("Exponentiation:", num1 ** num2) 
# print("Floor Division:", num1 // num2) 

# 2. Assignment Operators:
# These operators are used to assign values to variables.
# = : Assignment
# += : Add and Assign
# -= : Subtract and Assign
# *= : Multiply and Assign
# /= : Divide and Assign
# %= : Modulus and Assign      

# num1 = 10
# num2 = 5
# num1 += num2  
# print("After += Assignment:", num1)
# num1 -= num2  
# print("After -= Assignment:", num1)
# num1 *= num2  
# print("After *= Assignment:", num1)
# num1 /= num2            
# print("After /= Assignment:", num1)
# num1 %= num2
# print("After %= Assignment:", num1)



# 3. Comparison Operators:
# These operators compare two values and return a Boolean result (True or False).
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to    


# a = 15 
# b = 20
# print("Is a equal to b?", a == b)
# print("Is a not equal to b?", a != b)
# print("Is a greater than b?", a > b)
# print("Is a less than b?", a < b)
# print("Is a greater than or equal to b?", a >= b)
# print("Is a less than or equal to b?", a <= b)

# 4. Logical Operators:
# These operators are used to combine conditional statements.
# and : Logical AND
# or : Logical OR
# not : Logical NOT


# a = True    
# b = False
# print("a and b:", a and b)
# print("a or b:", a or b)
# print("not a:", not a)
# print("not b:", not b)

# 5.identity operators:
# These operators compare the memory locations of two objects.
# is : Returns True if both variables point to the same object
# is not : Returns True if both variables point to different objects

# fruits  = ["apple", "banana", "cherry"]
# m = fruits
# o = ["apple", "banana", "Pineapple"]

# print("m is fruits:", m is fruits)
# print("o is fruits:", o is fruits)
# print("m is not fruits:", m is not fruits)
# print("o is not fruits:", o is not fruits) 
# 
# 
# 6. membership operators:
# These operators test for membership in a sequence (like strings, lists, or tuples).
# in : Returns True if a value is found in the sequence
# not in : Returns True if a value is not found in the sequence

# fruits = ["apple", "banana", "cherry"]
# print("banana" not in fruits)

# a = "Mukul"
# print("k" in a)
# print("z" in a)