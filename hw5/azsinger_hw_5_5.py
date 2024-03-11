"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/18
Homework Problem # 5_5
Description of Problem (1-2 sentence summary in your own words):
Create two factorial functions, one that uses recursion and one that does not.
"""


def factorial(n):
    """
    Given a positive integer n, calculate the factorial of n using
    recursion.
    :param n: positive integer
    :return: factorial of n as an integer
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    """
    Given a positive integer n, calculate the factorial of n without
    using recursion.
    :param n: positive integer
    :return: factorial of n as an integer
    """
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def prompt_for_valid_input():
    """
    Prompt user for a positive integer. The prompt will repeat until
     a positive integer is provided.
    :return: the positive integer provided via input()
    """
    while True:
        user_input = input("Please enter a positive integer: ")
        try:
            user_int = int(user_input)
        except ValueError:
            print(f"ERROR: '{user_input}' is not an integer.")
            continue
        if user_int < 0:
            print(f"ERROR: '{user_input}' is not a positive integer.")
            continue

        return int(user_input)


if __name__ == "__main__":
    num = prompt_for_valid_input()
    print(f"factorial({num}): {factorial(num):,}")
    print(f"factorial2({num}): {factorial2(num):,}")
