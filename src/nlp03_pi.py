"""
03. Pi
Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures
involving quantum mechanics.” into words, and create a list whose element presents
the number of alphabetical letters in the corresponding word.
"""
import re
from typing import List


def count_length_of_each_word(sentence: str) -> List[int]:
    """
    >>> count_length_of_each_word('''Now I need a drink, alcoholic of course, after the\
     heavy lectures involving quantum mechanics.''')
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    """
    return [len(word) for word in re.findall(r"[a-zA-Z]+", sentence)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
