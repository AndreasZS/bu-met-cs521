"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
"""

from PollOption import PollOption
from promptutils import non_blank_input, multi_choice_prompt, CHOICE_OTHER, \
    CHOICE_EXIT


class Poll:
    """
    A poll that users can vote on
    """

    def __init__(self, name, options=None, is_anonymous=True):
        """
        Constructor for Poll objects.
        :param name: string name for this Poll
        :param options: list of PollOption objects
        :param is_anonymous: bool is this Poll anonymous?
        """
        if options is None:
            # IDE warned that the default argument of [] is mutable
            options = []
        self.name = name
        if is_anonymous is None:
            is_anonymous = True
        self.is_anonymous = is_anonymous
        self.__options_dict = {option.get_name(): option for option in
                               options}

    def __eq__(self, other):
        """
        :param other: other Poll instance
        :return: True if self and other have the same name, otherwise False
        """
        return self.get_name() == other.get_name()

    def __repr__(self):
        """
        :return: string to create this Poll instance
        """
        return (f"Poll(name={self.name!r},"
                f" options={list(self.__options_dict.values())},"
                f" is_anonymous={self.is_anonymous})")

    def __str__(self):
        """
        :return: string name of this Poll
        """
        return f"Poll: {self.name}"

    def serialize_to_json(self):
        """
        Convert this Poll instance to a dictionary which can be serialized
        using Python's json module.
        :return: dictionary representation of this Poll
        """
        poll_as_dict = dict()
        poll_as_dict["name"] = self.get_name()
        poll_as_dict["is_anonymous"] = self.is_anonymous
        poll_as_dict["options"] = self.get_options()
        return poll_as_dict

    def add_option(self, new_option):
        """
        Attempt to add a PollOption to this Poll.
        :param new_option: PollOption attempting to be added to this Poll
        instance
        :return: True if new_option was added to self.__options_dict. False
        otherwise
        """
        if new_option.get_name() not in self.__options_dict:
            # verify the PollOption does not already exist for this poll
            self.__options_dict.update({new_option.get_name(): new_option})
            return True
        else:
            print(f"ERROR: {new_option.get_name()} is already an option in "
                  f"this poll")
            return False

    def add_option_via_input(self):
        """
        Use input() to prompt for the name of a PollOption to add to this Poll
        instance. Then, create a new PollOption with the provided name and
        pass it to self.add_option().
        :return: new PollOption that was added, or None if adding was
        unsuccessful
        """
        new_option_name = non_blank_input("What option are you adding?\n")
        new_option = PollOption(new_option_name)
        if self.add_option(new_option):
            return new_option
        else:
            return None

    def vote_via_input(self):
        """
        Vote for a PollOption via input(). User can specify a new PollOption or
         choose not to vote.
        :return: False if no votes were cast, True otherwise
        """
        option_names = [option.get_name() for option in
                        self.get_options()]
        choice = multi_choice_prompt(option_names, prompt="Choose an option "
                                                          "to vote for: ",
                                     shuffle=True, allow_other=True,
                                     allow_exit=True)
        if choice == CHOICE_EXIT:
            return False
        elif choice == CHOICE_OTHER:
            new_option = self.add_option_via_input()
            choice = new_option.get_name()
        self.vote_by_option_name(choice)
        return True

    def vote_by_option_name(self, option_name=""):
        """
        Vote for the PollOption with name equal to option_name if it exists.
        :param option_name: name of the PollOption to vote for
        """
        if option_name not in self.__options_dict:
            print(f"'{option_name}' is not one of the options")
        else:
            self.__options_dict.get(option_name).add_vote(self)

    def vote_by_option(self, option):
        """
        Vote for the PollOption specified by Option.
        :param option: PollOption to vote for
        """
        self.vote_by_option_name(option.get_name())

    def get_results(self):
        """
        Get the results of this Poll as a string. The string is a
        representation of PollOptions and their corresponding number of votes.
        If this Poll is not anonymous, then results will include names of
        voters as comma-separated values.
        :return: string representation of results for this Poll
        """
        title = f"Results of {self.name} Poll\n"
        if self.is_anonymous:
            results_str = self.__get_anonymous_results()
        else:
            results_str = self.__get_nonanon_results()
        return f"{title}{results_str}"

    def get_all_voter_names(self):
        """
        Get the names of everyone who has voted on this Poll.
        :return: set containing string names of everyone who voted on this
        Poll. Empty set if this Poll is anonymous
        """
        all_voters = set()
        if not self.is_anonymous:
            for poll_option in self.get_options():
                all_voters = all_voters.union(poll_option.get_voters())
        return all_voters

    def get_name(self):
        """
        Get the name of this Poll instance.
        :return: name of this Poll
        """
        return self.name

    def set_name(self, new_name):
        """
        Set the name of this Poll instance.
        :param new_name: new name for this Poll
        """
        self.name = new_name

    def get_options(self):
        """
        Get all the PollOptions for this Poll.
        :return: list of PollOptions for this Poll instance
        """
        return list(self.__options_dict.values())

    def set_options(self, new_options):
        """
        Set all PollOptions for this Poll.
        :param new_options: new list of options for this Poll
        """
        self.__options_dict = {option.get_name(): option for option in
                               new_options}

    def get_options_dict(self):
        """
        Get all PollOptions for this Poll as a dictionary. Keys are the
        PollOption names and values are PollOption objects.
        :return: dictionary of PollOptions for this Poll
        """
        return self.__options_dict

    def set_options_dict(self, new_options_dict):
        """
        Set the PollOptions dictionary for this Poll.
        :param new_options_dict: new dictionary of PollOptions for this Poll
        """
        self.__options_dict = new_options_dict

    def remove_option(self, option):
        """
        Remove a PollOption from Poll instance by removing it from
        self.__options_dict.
        :param option: PollOption to remove
        """
        self.__options_dict.pop(option.get_name())

    def set_anonymity(self, is_anon):
        """
        Set whether this Poll is anonymous or not.
        """
        self.is_anonymous = is_anon

    def __get_anonymous_results(self):
        """
        Get a string representing the results. Do not display names of any
        voters.
        :return: string representation of anonymous results
        """
        return "\n".join([f"{option.get_name()}: "
                          f"{option.get_num_votes()} "
                          for option in self.__options_dict.values()])

    def __get_nonanon_results(self):
        """
        Get a string representing the results. Include the names of voters.
        :return: string representation of non-anonymous results
        """
        return "\n".join([f"{option.get_name()}: "
                          f"{option.get_num_votes()}"
                          f"\nvoters: {', '.join(option.get_voters())}"
                          for option in self.__options_dict.values()])


if __name__ == "__main__":
    # Unit Tests
    p = Poll("Test Poll", [PollOption("Option 1"), PollOption("Option 2"),
                           PollOption("Option 3")])
    p2 = Poll("test poll")
    p3 = Poll("Test Poll", [PollOption("Option 1", voters={"John", "Jane"}),
                            PollOption("Option 2", voters={"Tom", "Jerry"})],
              is_anonymous=False)
    assert {"John", "Jane", "Tom", "Jerry"} == p3.get_all_voter_names()
    p4 = Poll("Test Poll", [PollOption("Option 1", voters={"John", "Jane"}),
                            PollOption("Option 2", voters={"Tom", "Jerry"})],
              is_anonymous=True)
    assert set() == p4.get_all_voter_names()
