"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/14
Homework Problem # 5_1
Description of Problem (1-2 sentence summary in your own words):
Receive a valid text file from user input. Then, analyze the file and
print out the total number of vowels and total number of consonants.
"""

import os
import string


# using this vowel set rather than str.upper() on the entire textfile
VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
# use string.ascii_letters - vowels as the consonant set
CONSONANTS = set(string.ascii_letters).difference(VOWELS)


def prompt_for_text_file():
    """
    Repeatedly prompt a user until they provide a valid path to a text
    file. Path must end in '.txt' and exist. User and environment
    variables will be expanded and path will be normalized.
    :return: valid path to a .txt file as a string
    """
    is_valid = False
    while not is_valid:
        filepath = input("Enter a path to a text file: ")
        # Python on Windows will be able to work with forward slashes
        # replace backslashes with forward slashes
        filepath = filepath.replace("\\", "/")
        path = os.path.expanduser(filepath)
        path = os.path.expandvars(path)
        normalized_filepath = os.path.normpath(path)
        is_valid = is_valid_file(normalized_filepath)
    return normalized_filepath


def is_valid_file(filepath):
    """
    Determine if provided string is a valid path to a text file.
    :param filepath: string filename or path to a file
    :return: True if the file is a valid text file. False otherwise
    """
    is_valid = False
    if not os.path.isfile(filepath):
        print(f"ERROR: '{filepath}' does not exist or is not a file.")
    elif not filepath.endswith(".txt"):
        print(f"ERROR: '{filepath}' is not a text file.",
              "(does not end with '.txt')")
    else:
        is_valid = True
    return is_valid


def vc_counter(valid_filename):
    """
    Return a dictionary of vowel and consonant counts for a given text
    file.
    :param valid_filename: path to a valid text file
    :return: dictionary containing vowel and consonant counts
    """
    vowel_count = 0
    consonant_count = 0
    # use `with open()` to open the file for reading
    # it will be closed automatically
    with open(valid_filename, "r") as text_file:
        file_str = text_file.read()
        for vowel in VOWELS:
            vowel_count += file_str.count(vowel)
        for consonant in CONSONANTS:
            consonant_count += file_str.count(consonant)
    return {"vowels": vowel_count, "consonants": consonant_count}


def is_vowel(char):
    """
    :param char: string representing a single character
    :return: True if char is in VOWELS set. False otherwise
    """
    return char in VOWELS


def is_consonant(char):
    """
    :param char: string representing a single character
    :return: True if char is in CONSONANTS set. False otherwise
    """
    return char in CONSONANTS


def print_stats(vc_count_dict):
    """
    Print formatted counts of vowels and consonants from the provided
    dictionary.
    :param vc_count_dict: dictionary of vowel and consonant counts
    """
    vowel_count = vc_count_dict.get('vowels')
    consonant_count = vc_count_dict.get('consonants')
    print(f"Total # of vowels in text file: {vowel_count:,}")
    print(f"Total # of consonants in text file: {consonant_count:,}")


if __name__ == "__main__":
    # execute following when this file is run
    filename = prompt_for_text_file()
    print_stats(vc_counter(filename))
