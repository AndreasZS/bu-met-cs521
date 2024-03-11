"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/01/28
Homework Problem # 2_4
Description of Problem (1-2 sentence summary in your own words):
Prompt the user for number input. Cast the number to an integer, then print out
a 0 if the number is even or a 1 if the number is odd.
"""

# 4a
user_input = input("Please enter a number:\n")
# 4b
user_integer = int(user_input)
# 4c
print(user_integer % 2)
