"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/01/28
Homework Problem # 2_2
Description of Problem (1-2 sentence summary in your own words):
Prompt the user for a string or number input. Then print that input as a
string, integer, and float. Explain what data type must be input to not produce
any errors.
"""

# 2a
user_input = input("Please enter a string or a number:\n")
# 2b
print(f"User input from 2a, as a string: {user_input}")
print(f"User input from 2a, as an integer: {int(user_input)}")
print(f"User input from 2a, as a floating-point value: {float(user_input)}")
# 2c
"""
To avoid generating any errors, the user input must be a whole number with no
decimal point. A whole number can be displayed as a string, cast to an integer, 
or cast to a float, without generating any errors. A string containing text will 
generate errors when attempting to cast it to a number. A number with decimal 
point values will generate an error when attempting to cast it to an integer. 
Therefore, to not generate errors, the user must input a whole number.
"""
