"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/18
Homework Problem # 5_4
Description of Problem (1-2 sentence summary in your own words):
Prompt for a text file then create a function to return a list of words
that appear exactly twice in the file.
"""

import os
import string


def text_file_to_word_list(valid_filepath):
    """
    Given a valid path to a text file, remove all punctuation and return
     a list of words in the file.
    :param valid_filepath: string representing valid path to a text file
    :return: list of all words in the text file
    """
    word_list = []
    if is_valid_file(valid_filepath):
        # use `with open()` to open the file for reading
        # it will be closed automatically
        with open(valid_filepath, "r") as text_file:
            all_text = text_file.read()
            for char in string.punctuation:
                all_text = all_text.replace(char, "")
            word_list = all_text.split()
    return word_list


def prompt_for_text_file():
    """
    Repeatedly prompt a user until they provide a valid path to a text
    file. Path must end in '.txt' and exist. User and environment
    variables will be expanded and path will be normalized.
    :return: valid path to a .txt file as a string
    """
    filepath = ""
    is_valid = False
    while not is_valid:
        filepath = input("Please provide a path to a text file: ")
        # Python on Windows will be able to work with forward slashes
        # replace backslashes with forward slashes
        filepath = filepath.replace("\\", "/")
        filepath = os.path.expanduser(filepath)
        filepath = os.path.expandvars(filepath)
        filepath = os.path.normpath(filepath)
        is_valid = is_valid_file(filepath)
    return filepath


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


def list_to_twice_words(input_list):
    """
    Take a list of words in a file and return a list of words that appear
    exactly twice.
    :param input_list: list of words from text file
    :return: list of words that appear exactly twice
    """
    # use string.upper() to ignore case
    input_list = [word.upper() for word in input_list]
    twice_word_set = {word for word in input_list
                      if input_list.count(word) == 2}
    return list(twice_word_set)


if __name__ == "__main__":
    valid_filename = prompt_for_text_file()
    words = text_file_to_word_list(valid_filename)
    twice_words = list_to_twice_words(words)
    print(f"Words that appear twice in '{valid_filename}':\n{twice_words}")
