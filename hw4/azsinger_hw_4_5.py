"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/11
Homework Problem # 4_5
Description of Problem (1-2 sentence summary in your own words):
Create a constant dictionary of number-related characters. Receive a number from
 input. Validate the input and reprompt if there is an issue. Print out a text
 representation of the number, using the constant dictionary.
 NOTE: this problem does not account for complex numbers
"""

# 4.5a
CHAR_DICT = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
             "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero",
             "-": "negative", ".": "point"}
# 4.5b
num = ""
while True:
    num = input("Enter a number: ")
    if num.find(",") != -1:
        # are any commas present
        error_msg = "Please try again without entering commas."
    elif num.find("+") != -1:
        # plus sign is present
        error_msg = "Please try again without entering plus signs."
    else:
        try:
            num_as_float = float(num)
            # if casting to float did not error, then the input is a number
            break
        except ValueError as e:
            error_msg = f'"{num}" is not a valid number. Please try again'
    print(error_msg)

# translate number string to textual representation using dictionary
as_text = [CHAR_DICT.get(char).title() for char in num]
print(f"As Text: {' '.join(as_text)}")
