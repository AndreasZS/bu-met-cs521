"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/04
Homework Problem # 3_1
Description of Problem (1-2 sentence summary in your own words):
Loop through integers 2 to 130 (inclusive) and print out information on the
characteristics of integers in that range.
"""

LOOP_START = 2
LOOP_END = 131  # use 131 so that we include 130

odd_numbers = []
even_numbers = []
squares_of_ints = []
cubes_of_ints = []

# 3.1a
for num in range(LOOP_START, LOOP_END):
    # 3.1b
    if num % 2 == 1:
        # odd number
        odd_numbers.append(num)
    else:
        # even number
        even_numbers.append(num)
    if num**2 < LOOP_END:
        # square of an integer
        squares_of_ints.append(num**2)
    if num**3 < LOOP_END:
        # cube of an integer
        cubes_of_ints.append(num**3)

# 3.1c
print("Checking numbers from 2 to 130")
print(f"Odd ({len(odd_numbers)}): {odd_numbers[0]}...{odd_numbers[-1]}")
print(f"Even ({len(even_numbers)}): {even_numbers[0]}...{even_numbers[-1]}")
print(f"Square ({len(squares_of_ints)}): {squares_of_ints}")
print(f"Cube ({len(cubes_of_ints)}): {cubes_of_ints}")
