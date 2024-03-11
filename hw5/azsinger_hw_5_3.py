"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/16
Homework Problem # 5_3
Description of Problem (1-2 sentence summary in your own words):
Receive four numbers from user input then perform a specific calculation using
 the provided numbers. Handle errors/exceptions and reprompt for correct input.
"""

import sys

calc_result = None # calculated result using the four provided numbers
while not calc_result:
    user_input = input(
        "Please enter four numbers using a single comma ',' as a delimiter "
        "(e.g. 1,2,3,4): "
    )
    four_numbers = user_input.split(',')
    try:
        # ValueError, IndexError, and ZeroDivisionError will be detected here.
        # It was stated in the facilitator session on 2024/02/17 that use of a
        # try-except for this is allowed
        if len(four_numbers) != 4:
            raise IndexError
        calc_result = (float(four_numbers[0]) * float(four_numbers[1]) + float(
            four_numbers[2]) / float(four_numbers[3]))

    except ValueError:
        print("ValueError: please make sure all values are numerical.")
        continue
    except IndexError:
        print(f"IndexError: please make sure to provide exactly four numbers.")
        continue
    except ZeroDivisionError:
        print("ZeroDivisionError: the last number must not be 0.")
        continue
    # if no errors by now, then input was valid
    # print the formula and result
    print(
        f"({four_numbers[0]} * {four_numbers[1]} + {four_numbers[2]}) /",
        f"{four_numbers[3]} = {calc_result}")
    break
# exit the program
sys.exit()
