"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/01/28
Homework Problem # 2_3
Description of Problem (1-2 sentence summary in your own words):
Prompt the user for number input. Cube the number then divide it by itself.
Finally, print the formula and the result, truncating the number to two decimal
places.
"""

# 3a
n = input("Please enter a number: ")
# 3b
float_n = float(n)
n_squared = float_n**3 / float_n
# 3c
print(f"{n}**3/{n} = {n_squared:.2f}")
