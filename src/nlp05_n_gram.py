"""
05. n-gram
Implement a function that obtains n-grams from a given sequence object
(e.g., string and list).
Use this function to obtain word bi-grams and letter bi-grams from the sentence
"I am an NLPer".
"""
from typing import List, Sequence, Tuple


def create_n_gram(seq: Sequence[str], n: int) -> List[Tuple[str]]:
    """
    >>> create_n_gram("I am an NLPer".split(), 2)
    [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]

    >>> create_n_gram("I am an NLPer", 2)
    [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'), ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
    """
    return [tuple(seq[i : i + n]) for i in range(len(seq) - n + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
