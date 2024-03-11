"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
"""

import sys

from Poll import Poll
from PollOption import PollOption
from poll_fileutils import read_polls_from_json
from poll_fileutils import write_polls_to_json
from promptutils import yes_no_prompt, multi_choice_prompt, box_up_text, \
    CHOICE_OTHER, CHOICE_EXIT, filepath_prompt, non_blank_input

CREATE_NEW_POLL = "Create a New Poll"
READ_FROM_FILE = "Read from file"
WRITE_TO_FILE = "Write to file"
VOTE_ON_POLL = "Vote on a Poll"
VIEW_RESULTS = "View Results of a Poll"
EXIT = "Exit"


class PollManager:
    """
    Manager for Poll instances. Allow users to create and interact with Polls
    """

    def __init__(self):
        """
        Constructor for PollManager.
        """
        self.__id = id(self)
        self.__polls = dict()

    def get_polls(self):
        """
        :return: dictionary of Poll names and Poll instances known to this
        manager
        """
        return self.__polls

    def set_polls(self, polls):
        """
        Set self.__polls
        :param polls: list of Poll objects
        """
        self.__polls = {poll.get_name(): poll for poll in polls}

    def clear_polls(self):
        """
        Remove all Poll instances from self.__polls
        """
        if yes_no_prompt("Are you sure you want to remove all polls from "
                         "this PollManager?"):
            self.__polls.clear()

    def initial_menu(self):
        """
        The initial menu visible to users. Users can navigate to different
        menus by providing the corresponding input.
        """
        prompts = [CREATE_NEW_POLL, READ_FROM_FILE, EXIT]
        while True:
            if len(self.__polls) > 0 and len(prompts) < 4:
                prompts.insert(1, VOTE_ON_POLL)
                prompts.insert(2, VIEW_RESULTS)
                prompts.insert(4, WRITE_TO_FILE)
            choice = (
                multi_choice_prompt(prompts,
                                    prompt="What would you like to do?"))

            if choice == CREATE_NEW_POLL:
                self.add_poll_via_prompt()
            elif choice == VOTE_ON_POLL:
                self.voting_menu()
            elif choice == VIEW_RESULTS:
                self.view_results_menu()
            elif choice == READ_FROM_FILE:
                self.read_from_file_prompt()
            elif choice == WRITE_TO_FILE:
                self.write_to_file_prompt()
            elif choice == EXIT:
                save_polls = (
                    yes_no_prompt(
                        "Would you like to save your polls to a file?"))
                if save_polls:
                    self.write_to_file_prompt()
                print(box_up_text("Thank you, goodbye!"))
                sys.exit()

    def read_from_file_prompt(self):
        """
        Read a JSON file from user input. If the file contains a Poll or
        Polls, then they can be added to this PollManager.
        :return: True if reading polls from file was successful, otherwise
        False
        """
        filepath = filepath_prompt()
        try:
            polls_from_file = read_polls_from_json(filepath)
        except Exception as e:
            print(f"ERROR: unable to read polls from {filepath!r}.")
            print("Is the file formatted correctly?")
            print(f"Exception: {e}")
            return False
        overwrite = True
        if len(self.__polls) > 0:
            overwrite = yes_no_prompt("Overwrite all existing polls?")
        if overwrite:
            self.__polls = {poll.get_name(): poll for poll in polls_from_file}
        else:
            polls_dict = {poll.get_name(): poll for poll in polls_from_file
                          if poll.get_name() not in self.__polls}
            self.__polls.update(polls_dict)
        return True

    def write_to_file_prompt(self):
        """
        Write this PollManager's polls as JSON to the output file specified by
        user input.
        :return: True if writing polls to file was successful, otherwise False
        """
        filepath = filepath_prompt(predicate=lambda x: True)
        try:
            write_polls_to_json(filepath, list(self.__polls.values()))
            return True
        except Exception as e:
            print(f"ERROR: unable to write polls to file.")
            print(f"Exception: {e}")
            return False

    def poll_exists(self, poll):
        """
        :param poll: Poll instance
        :return: True if a Poll with this name is already known to this
        PollManager, otherwise False
        """
        return poll.get_name() in self.__polls

    def add_poll(self, new_poll):
        """
        Add a new Poll to this PollManager.
        :param new_poll: Poll instance to be added
        :return: True if new_poll was added, otherwise False
        """
        existing_poll = self.__polls.get(new_poll.get_name())
        yes_overwrite = False
        was_poll_added = False
        if existing_poll:
            print(f"Poll with name '{existing_poll.get_name()}' already "
                  f"exists.")
            yes_overwrite = yes_no_prompt("Would you like to overwrite it?")
        if not existing_poll or yes_overwrite:
            self.__polls[new_poll.get_name()] = new_poll
            was_poll_added = True
        return was_poll_added

    def add_poll_via_prompt(self):
        """
        Add a new Poll to this PollManager. The Poll will be created based
        on user input.
        :return: the new Poll that was added
        """
        poll_name = non_blank_input("What is the name of the new poll?\n")
        new_poll = Poll(poll_name)
        if self.add_poll(new_poll):
            is_anon = yes_no_prompt("Is this poll anonymous?", default="Y")
            choices = ["Add an option"]
            choice = multi_choice_prompt(choices, allow_exit=True)
            poll_options = []
            if choice == choices[0]:
                poll_options = create_options()
            new_poll.set_options(poll_options)
            new_poll.set_anonymity(is_anon)
            return new_poll

    def voting_menu(self):
        """
        The voting menu visible to users if they chose to vote on a poll. Will
        continue displaying until user indicates they are done voting.
        """
        target_poll = self.__select_poll_via_input(
            "What poll would you like to vote on?")
        if target_poll:
            while True:
                keep_voting = target_poll.vote_via_input()
                if not keep_voting and yes_no_prompt("Are you sure?"):
                    break

    def view_results_menu(self):
        """
        The view results menu visible to users if they chose to view results
        of a poll. Will continue displaying until user chooses to exit.
        """
        target_poll = self.__select_poll_via_input(
            "What poll would you like to view the results of?")
        if target_poll:
            print(box_up_text(target_poll.get_results()))
            done_viewing = False
            while not done_viewing:
                done_viewing = yes_no_prompt(
                    "Are you done viewing these results?")
            # stay on View Results menu until user chooses to Exit
            self.view_results_menu()

    def __select_poll_via_input(self, prompt="Select poll:"):
        """
        Private method to select a Poll instance using user input.
        :param prompt: optional string to display before listing polls
        :return: Poll instance selected by user
        """
        target_poll_name = multi_choice_prompt(list(self.__polls.keys()),
                                               prompt=prompt,
                                               allow_other=True,
                                               allow_exit=True)
        if target_poll_name == CHOICE_OTHER:
            target_poll = self.add_poll_via_prompt()
        elif target_poll_name == CHOICE_EXIT:
            target_poll = None
        else:
            target_poll = self.__polls.get(target_poll_name)
        return target_poll


def create_options():
    """
    :return: list of PollOption instances created using user input
    """
    print("Enter name(s) for poll option(s). Enter a blank if you are "
          "finished: ")
    poll_options = []
    option_name = input()
    while option_name and not option_name.isspace():
        poll_options.append(PollOption(option_name))
        option_name = input()
    return poll_options


if __name__ == "__main__":
    # unit tests
    test_manager = PollManager()
    test_option = PollOption("Test Option 1")
    test_poll = Poll("Test Poll", [test_option])
    test_manager.add_poll(test_poll)
    assert test_manager.poll_exists(test_poll)
    assert "Test Poll" == list(test_manager.get_polls())[0]
