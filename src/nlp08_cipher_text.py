"""
08. cipher text
Implement a function cipher that converts a given string with the specification:
    * Every lowercase letter c is converted to a letter whose ASCII code is
    (219 - [the ASCII code of c])
    * Keep other letters unchanged
Use this function to cipher and decipher an English message.
"""


def cipher(s: str) -> str:
    """
    >>> cipher("abc!def.")
    'zyx!wvu.'
    """
    convert = lambda c: chr(219 - ord(c)) if "a" <= c <= "z" else c
    return "".join(map(convert, s))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
