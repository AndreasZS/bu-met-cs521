"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/01/26
Homework Problem # 2_1
Description of Problem (1-2 sentence summary in your own words):
Prompt a user for a whole number input, then perform different operations on it.
"""

# 1a
user_provided_string = input("Please enter a whole number from 1 to 7:\n")
# 1b
user_provided_int = int(user_provided_string)
b = (user_provided_int * 2 + 10) / 2 - user_provided_int
# 1c
print("Result of computations from 2.1b, as an integer:", int(b))
# 1d
hundreds_digit = user_provided_string
tens_digit = str(user_provided_int + 1)
ones_digit = str(user_provided_int + 2)
three_digit_int = int(hundreds_digit + tens_digit + ones_digit)
# 1e
three_digit_sum = int(hundreds_digit) + int(tens_digit) + int(ones_digit)
print("Sum of the three digits from 1d:", three_digit_sum)
# 1f
three_digit_division = three_digit_int / three_digit_sum
print(
    "Result of dividing the three-digit number from 1d by the sum from 1e,"
    " as a float:",
    three_digit_division)
# 1g
print(f"Output from 1f, as a truncated integer: {three_digit_division:.0d}")

