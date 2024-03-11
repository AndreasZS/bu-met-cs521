"""
Name: Andreas Z. Singer
Class: CS 521 - Spring 1
Date (YYYY/MM/DD): 2024/02
Term Project
main.py:
This project is meant to be run from here. If running from a terminal that
has Python installed, you can call `python main.py` from the project
directory.
"""

from PollManager import PollManager

if __name__ == "__main__":
    manager = PollManager()
    manager.initial_menu()
