"""
Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02/22
Homework Problem # 6
Description of Problem (1-2 sentence summary in your own words):
Create a Sentence class to represent an English sentence. Include various
methods and attributes. Lastly, perform a unit test and print some output.
"""

import random
import string


class Sentence:
    """
    Class to represent an English sentence.
    """

    def __init__(self, sentence=""):
        """
        Constructor to create a new Sentence object.
        :param sentence: English sentence as a string. Default is empty string
        """
        self.__original_sentence = sentence
        # convert sentence to a list attribute using split()
        # first remove all punctuation
        no_punct_sentence = sentence
        if len(sentence) > 0 and not sentence.isspace():
            for char in string.punctuation:
                no_punct_sentence = no_punct_sentence.replace(char, "")
        self.__sentence = no_punct_sentence.split()

    def get_original_sentence(self):
        """
        :return: original sentence as a string
        """
        return self.__original_sentence

    def get_all_words(self):
        """
        Method to retrieve all words in the sentence.
        :return: all words in the sentence as a list
        """
        return self.__sentence

    def get_word(self, index):
        """
        Method to get one desired word from the sentence.
        :param index: integer index location of desired word
        :return: single word or empty string if index is outside the range
        """
        try:
            word = self.__sentence[index]
        except IndexError:
            # assignment instructions state that "it is okay for the program to
            # crash on a non-integer argument." So, only account for IndexError
            print(f"Index {index} is outside of range 0-"
                  f"{len(self.__sentence) - 1} inclusive")
            word = ""
        return word

    def set_word(self, index: int, new_word):
        """
        Changes the word at a given index location in the sentence to a new
        word. The word change will persist within the instance.
        :param index: integer index of the word to change in the list of all
        words
        :param new_word: string word that will replace the word at specified
        index
        """
        try:
            self.__sentence[index] = new_word
        except TypeError:
            print(f"Invalid list index {index!r}. List indices must be "
                  f"integers or slices.")
        except IndexError:
            print(f"Index {index} is outside of range 0-"
                  f"{len(self.__sentence) - 1} inclusive")

    def scramble(self):
        """
        Scramble the list of all words in the sentence. Uses a shallow
        copy and random.shuffle().
        :return: new scrambled list of all words in the sentence
        """
        # strings are immutable in Python, therefore it is ok to use a
        # shallow copy of the sentence list
        scrambled = self.__sentence.copy()
        random.shuffle(scrambled)
        return scrambled

    def __repr__(self):
        """
        :return: sentence list as a single string, with a period at the end
        """
        return f"{' '.join(self.__sentence)}."


if __name__ == "__main__":
    # Unit Test(s)
    s = Sentence("The quick brown fox jumps over the lazy dog.")
    s.set_word(-1, "cat")
    assert "cat" == s.get_word(-1)
    print("Sentence unit test successful")
    print(f"Original sentence as string: {s.get_original_sentence()}")
    print(f"Scrambled sentence as string: {' '.join(s.scramble())}.")
    print(f"Final sentence as string: {s}")
