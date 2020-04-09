"""
00. Reversed string
Obtain the string that arranges letters of the string “stressed” in reverse order
(tail to head).
"""


def reverse_string(s: str) -> str:
    """
    >>> reverse_string("stressed")
    'desserts'
    """
    return s[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
