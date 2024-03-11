"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/15
Homework Problem # 5_2
Description of Problem (1-2 sentence summary in your own words):
Use three functions to generate a letter count dictionary, a list of
most common letters, and a histogram based on the dictionary. Print
formatted output.
"""

import os
import string


def letter_counts(input_str):
    """
    Return a dictionary using characters from the input string as keys
    and the number of times that letter appears as values. This ignores
    case.
    :param input_str: string to analyze for letter counts
    :return: dictionary of letter counts
    """
    input_str_upper = input_str.upper()
    return {letter: input_str_upper.count(letter) for letter
            in string.ascii_uppercase
            if input_str_upper.count(letter) > 0}


def most_common_letter(input_str):
    """
    Create a letter count dictionary for the provided string then
    create a list of the most frequent letters.
    :param input_str: string to analyze for most frequent letter(s)
    :return: list of letters that appear most frequently in input_str
    """
    letter_counts_dict = letter_counts(input_str)
    most_common_letters = []
    if len(letter_counts_dict) > 0:
        highest_count = max(letter_counts_dict.values())
        most_common_letters = [letter for letter in letter_counts_dict.keys()
                               if
                               letter_counts_dict.get(letter) == highest_count]
    return most_common_letters


def string_count_histogram(input_str):
    """
    Create a list representing letter counts of input_str as a histogram.
    :param input_str: string from which to generate letter count
    histogram
    :return: list of strings representing a letter count histogram
    """
    return [letter * count for letter, count
            in letter_counts(input_str).items()]


if __name__ == "__main__":
    # Analyze string constant and provide output
    # CONSTANT_STR ="WAS IT A RAT I SAW"
    CONSTANT_STR = "WWWAS IT A RAT I SAW"
    print(f'The string being analyzed is: "{CONSTANT_STR}"')
    letter_count_dict = letter_counts(CONSTANT_STR)
    if not letter_count_dict:
        # handle bad input
        print("ERROR: Constant string does not contain any letters")
    else:
        # print letter_count_dict as comma separated data
        letter_counts_list = [f"{repr(key)}: {value}" for key, value
                              in list(letter_counts(CONSTANT_STR).items())]
        print(f"1. Letter counts: {', '.join(letter_counts_list)}")

        # generate and print most common letter(s)
        most_freq_letters = most_common_letter(CONSTANT_STR)
        # adjust words to make the print statements grammatically correct
        letter_appear_time = ["letter", "appears", "times"]
        if len(most_freq_letters) > 1:
            letter_appear_time[0] = "letters:"
            letter_appear_time[1] = "each appear"
        if most_freq_letters and letter_count_dict[most_freq_letters[0]] == 1:
            letter_appear_time[2] = "time"
        most_freq_str = ', '.join(repr(letter) for letter in most_freq_letters)
        most_freq_msg = "{} {} {} {} {}.".format(letter_appear_time[0],
                                                 most_freq_str,
                                                 letter_appear_time[1],
                                                 letter_count_dict[
                                                     most_freq_letters[0]],
                                                 letter_appear_time[2])
        print(f"2. Most frequent {most_freq_msg}")

        # generate and print histogram
        histogram = string_count_histogram(CONSTANT_STR)
        # os.linesep should not be used if writing text to files
        # but since this is just a print statement, it should be fine
        print(f"Histogram:\n{os.linesep.join(histogram)}")
        # the following only works for Python version >= 3.12
        # print(
        # f"Histogram:\n{'\n'.join(histogram)}"
        # )
