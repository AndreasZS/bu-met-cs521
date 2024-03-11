"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
"""

from promptutils import non_blank_input


class PollOption:
    """
    Voting option for a Poll instance
    """

    def __init__(self, name, num_votes=0, voters=None):
        """
        Constructor for PollOption.
        :param name: string name of this PollOption
        :param num_votes: optional integer number of votes
        :param voters: optional set of voter name strings
        """
        self.name = name
        self.__num_votes = num_votes
        if voters is None:
            # IDE warned that the default argument of set() is mutable
            voters = set()
        self.__voters = voters

    def __lt__(self, other):
        """
        :param other: PollOption
        :return: True if self has fewer votes than other, otherwise False
        """
        return self.get_num_votes() < other.get_num_votes()

    def __le__(self, other):
        """
        :param other: PollOption
        :return: True if self has fewer or the same votes as other,
        otherwise False
        """
        return self.get_num_votes() <= other.get_num_votes()

    def __gt__(self, other):
        """
        :param other: PollOption
        :return: True if self has more votes than other, otherwise False
        """
        return self.get_num_votes() > other.get_num_votes()

    def __ge__(self, other):
        """
        :param other: PollOption :return: True if self has more or the same
        votes as other, otherwise False
        """
        return self.get_num_votes() >= other.get_num_votes()

    def __ne__(self, other):
        """
        :param other: PollOption
        :return: True if self has a different name than other, otherwise False
        """
        return not self == other

    def __eq__(self, other):
        """
        :param other: PollOption
        :return: True if self and other have the same name, otherwise False
        """
        return self.get_name() == other.get_name()

    def __repr__(self):
        """
        :return: string to create this PollOption instance
        """
        return f"PollOption({self.name!r}, {self.__num_votes})"

    def __str__(self):
        """
        :return: string name of this PollOption
        """
        return f"{self.name}"

    def get_name(self):
        """
        Get name of this PollOption
        :return: string name of this PollOption
        """
        return self.name

    def set_name(self, new_name):
        """
        Set name of this PollOption.
        :param new_name: string new_name for this PollOption
        """
        self.name = new_name

    def add_vote(self, poll):
        """
        Add a vote to this PollOption. If is_anon is False, then prompt the
        user for their name. If someone with that name has already voted,
        then prompt again. Increments num_votes.
        :param poll:
        """
        if poll and not poll.is_anonymous:
            all_voter_names = poll.get_all_voter_names()
            while True:
                voter_name = non_blank_input("Name: ")
                if voter_name in all_voter_names:
                    print(f"Someone with the name {voter_name!r} has already "
                          f"voted on {poll!s}.")
                    print("Try adding the initial of your last and/or middle "
                          "name.")
                else:
                    break
            self.__voters.add(voter_name)
        self.__num_votes += 1

    def get_num_votes(self):
        """
        :return: the number of votes this PollOption has received
        """
        return self.__num_votes

    def get_voters(self):
        """
        :return: set containing names of voters if the Poll is not
        anonymous, otherwise an empty set
        """
        return self.__voters

    def serialize_to_json(self):
        """
        Convert this PollOption instance to a dictionary which can be
        serialized using Python's json module.
        :return: dictionary representation of this PollOption
        """
        poll_option_as_dict = dict()
        poll_option_as_dict["name"] = self.name
        poll_option_as_dict["num_votes"] = self.get_num_votes()
        poll_option_as_dict["voters"] = list(self.__voters)
        return poll_option_as_dict


if __name__ == "__main__":
    # unit tests
    test_poll_option = PollOption("")
    assert isinstance(test_poll_option.get_voters(), set)
    test_poll_option.add_vote(None)
    assert 0 == len(test_poll_option.get_voters())
    assert 1 == test_poll_option.get_num_votes()
