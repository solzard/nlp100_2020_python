"""
02. “shoe” + “cold” = “schooled”
Obtain the string “schooled” by concatenating the letters in “shoe” and “cold”
one after the other from head to tail.
"""
from itertools import zip_longest


def concatenate_two_strings_alternately(s1: str, s2: str) -> str:
    """
    >>> concatenate_two_strings_alternately("shoe", "cold")
    'schooled'
    """
    return "".join("".join([c1, c2]) for c1, c2 in zip_longest(s1, s2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
