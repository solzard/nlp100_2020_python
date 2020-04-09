"""
01. “schooled”
Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string
“schooled”.
"""


def concatenate_odd_letters(s: str) -> str:
    """
    >>> concatenate_odd_letters("schooled")
    'shoe'
    """
    return "".join(c for i, c in enumerate(s, 1) if i % 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
