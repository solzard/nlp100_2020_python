"""
04. Atomic symbols
Split the sentence "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations
Might Also Sign Peace Security Clause. Arthur King Can." into words, and extract
the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and
the first two letters from the other words.
Create an associative array (dictionary object or mapping object) that maps from
the extracted string to the position (offset in the sentence) of the corresponding word.
"""
import re
from typing import Dict


def extract_atomic_symbols(sentence: str) -> Dict[str, int]:
    """
    >>> extract_atomic_symbols('''Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.''')
    {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
    """
    first_letter_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    return {
        (word[0] if i in first_letter_positions else word[:2]): i
        for i, word in enumerate(re.findall(r"[a-zA-Z]+", sentence), 1)
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
