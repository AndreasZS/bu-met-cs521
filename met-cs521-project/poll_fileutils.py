"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
poll_fileutils.py:
Various functions to help read and write Polls to and from JSON files.
"""

import json

from Poll import Poll
from PollOption import PollOption


def read_polls_from_json(filepath):
    """
    Read one or more Poll objects from a JSON file specified by filepath.
    :param filepath: string JSON filepath
    :return: list of Poll objects
    """
    result = []
    with open(filepath, "r") as file:
        try:
            deserialized = json.load(file)
        except Exception as e:
            print(f"Exception: {e}")
        if isinstance(deserialized, list):
            result = [json_dict_to_poll(obj) for obj in deserialized]
        else:
            result = [json_dict_to_poll(deserialized)]
    result = [x for x in result if x]
    if len(result) == 0:
        print(f"ERROR: {filepath!r} contained no polls")
    return result


def write_polls_to_json(filepath, polls):
    """
    Write Poll objects to an output JSON file.
    :param filepath: string JSON filepath
    :param polls: list of Poll objects
    """
    with open(filepath, "w") as file:
        try:
            json.dump(polls, file, default=lambda x: x.serialize_to_json())
            print(f"SUCCESS! Polls were written to {filepath!r}")
            print("NOTE: Due to Python file buffering, the file may not be "
                  "available until this application terminates.")
        except Exception as e:
            print(f"ERROR: unable to write polls to file.\nException: {e}")


def json_dict_to_poll(json_object):
    """
    Create a Poll object from a JSON dictionary.
    :param json_object: dictionary JSON object
    :return: Poll instance from json_object
    """
    name = json_object.get("name")
    if name is None:
        print("ERROR: one or more polls is missing a name")
        return None
    is_anon = json_object.get("is_anonymous")
    options = json_object.get("options")
    if options is None:
        options = []
    options = [json_to_poll_option(option) for option in options]
    options = [x for x in options if x]
    return Poll(name, options, is_anon)


def json_to_poll_option(json_object):
    """
    Create a PollOption object from a JSON dictionary.
    :param json_object: dictionary JSON object
    :return: PollOption instance from json_object
    """
    name = json_object.get("name")
    if name is None:
        print("ERROR: one or more poll options is missing a name")
        return None
    num_votes = json_object.get("num_votes")
    if num_votes is None:
        num_votes = 0
    voters = json_object.get("voters")
    if voters is None:
        voters = set()
    else:
        voters = set(voters)
    return PollOption(name, num_votes, voters=voters)


if __name__ == "__main__":
    polls = read_polls_from_json("test-files/example-input.json")
    assert 2 == len(polls)
    assert isinstance(polls[0], Poll)
