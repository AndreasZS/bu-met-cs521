"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
promptutils.py:
Functions to help prompt for user input in a variety of scenarios.
"""

import copy
import os
import random

# String constants used by multi_choice_prompt
CHOICE_OTHER = f"{chr(0x25C8)} Other - please specify"
CHOICE_EXIT = f"{chr(0x25C8)} Exit"


def yes_no_prompt(prompt_msg, expected_responses=("y", "Y", "n", "N"),
                  default="Y"):
    """
    Prompt a user to provide a yes or no response via input(). Yes
    responses are y or Y. No responses are n or N.
    :param prompt_msg: string to prompt the yes or no response
    :param expected_responses: expected responses from the user
    :param default: default response if user does not provide one
    :return: True if user provides yes response, otherwise False
    """
    if default == "Y":
        yes_no = "[Y\\n]"
    else:
        yes_no = "[y\\N]"
    is_yes = False
    while True:
        answer = input(f"{prompt_msg} {yes_no} ")
        is_blank = (answer == "" or answer.isspace())
        if is_blank:
            answer = default
        if answer not in expected_responses:
            print(f"{answer} does not match any expected responses.")
            continue
        is_yes = answer in ("y", "Y")
        break
    return is_yes


def multi_choice_prompt(choices, prompt="Choose one:", shuffle=False,
                        allow_other=False, allow_exit=False):
    """
    Prompt a user to choose from multiple choices by providing the
    corresponding zero-based index of their desired choice.
    :param shuffle: if True, display choices in random order
    :param allow_other: if True, include 'Other' at end of choices
    :param allow_exit: if True, include 'Exit' at end of choices
    :param choices: iterable of choice strings the user can choose from
    :param prompt: optional message to print before listing choices
    :return: object corresponding to the selected choice from choices
    """
    choices = copy.copy(choices)
    if shuffle:
        random.shuffle(choices)
    if allow_other:
        choices.append(CHOICE_OTHER)
    if allow_exit:
        choices.append(CHOICE_EXIT)
    choices_dict = {ind: choice for ind, choice in enumerate(choices)}
    choices_str = choices_dict_to_choices_str(choices)
    choice = ""
    num_choice = None
    prompt = f"{prompt}\n{box_up_text(choices_str)}"
    print(box_up_text(prompt))
    input_prompt = "Please enter the corresponding number for your choice: "
    while not choice or not num_choice:
        num_choice = input(input_prompt)
        try:
            choice = choices_dict[int(num_choice)]
        except (ValueError, KeyError):
            print(f"ERROR: '{num_choice}' is not a valid option. Please "
                  f"enter a value in the range 0-"
                  f"{len(choices) - 1} inclusive.")
    return choice


def choices_dict_to_choices_str(choices):
    """
    Convert an iterable to a formatted string meant to neatly
    represent the elements as choices for a user.
    :param choices: iterable of choices
    :return: formatted string to represent iterable elements as choices
    """
    return "\n".join(f"[{ind}] {choice}" for ind, choice in enumerate(
        choices))


def non_blank_input(prompt=""):
    """
    Repeatedly ask a user for input using the provided prompt until they
    provide a non-empty, non-blank input.
    :param prompt: string message to display when asking for input
    :return: user provided string, will not be blank or empty
    """
    while True:
        input_str = input(prompt)
        if len(input_str) == 0 or input_str.isspace():
            print("Input must be non-blank and non-empty. Please try again.")
            continue
        return input_str


def filepath_prompt(prompt="Please enter a valid filepath: ",
                    ext=".json", predicate=os.path.isfile):
    """
    Repeatedly prompt a user for a filepath until a valid one is provided,
    then return a normalized version of the filepath with any environment
    variables expanded. Validity is determined by the predicate parameter
    which defaults to os.path.isfile, as well as the file extension.
    :param prompt: optional string message to use when asking for input
    :param ext: optional string for expected file extension, case-insensitive
    :param predicate: optional function to determine filepath validity
    :return: valid filepath as expanded and normalized string
    """
    is_valid = False
    filepath = ""
    while True:
        filepath = non_blank_input(prompt)
        filepath = expand_and_normalize_filepath(filepath)
        is_valid_ext = filepath.upper().endswith(ext.upper())
        is_valid = predicate(filepath) and is_valid_ext
        if is_valid:
            break
        else:
            if not is_valid_ext:
                print(f"ERROR: {filepath!r} does not end with {ext.lower()} "
                      f"or {ext.upper()}")
            elif predicate.__name__ == "isfile":
                print(f"ERROR: {filepath!r} does not exist or is not a file")
    return filepath


def expand_and_normalize_filepath(filepath):
    """
    Return the filepath parameter after the following changes: replace all
    backslashes with front slashes, expand any environment variables,
    normalize the filepath.
    :param filepath: string filepath
    :return: string expanded and normalized filepath
    """
    # Replace backslashes with forward slashes.
    # Python on Windows will be able to work with forward slashes.
    filepath = filepath.replace("\\", "/")
    filepath = os.path.expanduser(filepath)
    filepath = os.path.expandvars(filepath)
    filepath = os.path.normpath(filepath)
    return filepath


def box_up_text(text, upper_box_char=chr(0x2550),
                side_box_char=chr(0x2551), lower_box_char=chr(0x2550),
                upper_left_corner=chr(0x2554), upper_right_corner=chr(0x2557),
                lower_left_corner=chr(0x255A), lower_right_corner=chr(0x255D)):
    """
    Create a box around a provided string using unicode characters.
    :param text: string to place in box
    :param upper_box_char: string for upper part of box
    :param side_box_char: string for sides of box
    :param lower_box_char: string for lower part of box
    :param upper_left_corner: string for upper left corner of box
    :param upper_right_corner: string for upper right corner of box
    :param lower_left_corner: string for lower left corner of box
    :param lower_right_corner: string for lower right corner of box
    :return: text string now inside a box
    """
    # expand tabs to avoid misleading results from __len__
    text = text.expandtabs()
    strings = text.split("\n")
    longest_line = len(max(strings, key=lambda x: len(x)))
    # use longest_line + 2 to allow a space on each side
    border_len = longest_line
    upper_border = (f"{upper_left_corner}"
                    f"{upper_box_char * (border_len + 2)}"
                    f"{upper_right_corner}")
    lower_border = (f"{lower_left_corner}"
                    f"{lower_box_char * (border_len + 2)}"
                    f"{lower_right_corner}")
    new_strings = []
    for s in strings:
        surround_text = f"{side_box_char} {s:{border_len}} {side_box_char}"
        new_strings.append(surround_text)
    new_strings = "\n".join(new_strings)
    return f"{upper_border}\n{new_strings}\n{lower_border}"


if __name__ == "__main__":
    # unit tests
    test_filepath = ".\\path\\to\\file"
    assert "path/to/file" == expand_and_normalize_filepath(test_filepath)
