"""
06. Set
Let the sets of letter bi-grams from the words "paraparaparadise" and "paragraph",
$X$ and $Y$, respectively.
Obtain the union, intersection, difference of the two sets.
In addition, check whether the bi-gram "se" is included in the sets $X$ and $Y$.
"""
from src.nlp05_n_gram import create_n_gram


def main():
    X, Y = set(create_n_gram("paraparaparadise", 2)), set(create_n_gram("paragraph", 2))
    se = ("s", "e")
    print(f"Union: {X | Y}")
    print(f"Intersection: {X & Y}")
    print(f"Difference: {X - Y}")
    print(f'"se" in X: {se in X} / in Y: {se in Y}')


if __name__ == "__main__":
    main()
