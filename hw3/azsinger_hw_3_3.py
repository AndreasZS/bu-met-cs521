"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/04
Homework Problem # 3_3
Description of Problem (1-2 sentence summary in your own words):
Prompt users for a 3-digit integer that meets certain requirements. Until the
input meets the requirements, print an appropriate error message and reprompt.
"""

DUPLICATION_ERROR_MSG = "Your number contains duplication."
LEN_ERROR_MSG = "You did not enter a 3-digit number."
NON_INT_ERROR_MSG = "This is not an integer. Please re-enter."
NOT_ASC_ERROR_MSG = "The digits are not in ascending order."

is_input_valid = False

while not is_input_valid:
    output_msg = "Number Accepted!"
    user_input = input("Please enter a 3-digit integer: ")
    # input must be a three-digit whole number and digits must be in ascending
    # order without duplicates
    if not user_input.isdigit():
        # is the input an integer
        output_msg = NON_INT_ERROR_MSG
    elif not len(user_input) == 3:
        # is the input 3 characters
        output_msg = LEN_ERROR_MSG
    elif len(set(user_input)) < 3:
        # does the input contain duplicates
        output_msg = DUPLICATION_ERROR_MSG
    elif not (user_input[0] < user_input[1] < user_input[2]):
        # are the digits in ascending order
        output_msg = NOT_ASC_ERROR_MSG
    else:
        # correct input
        is_input_valid = True
        print(output_msg)
        break
    print(f"--> Error: {output_msg}")
