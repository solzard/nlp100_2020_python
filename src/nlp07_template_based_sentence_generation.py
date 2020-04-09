"""
07. Template-based sentence generation
Implement a function that receives arguments, x, y, and z and returns a string
"{y} is {z} at {x}", where "{x}", "{y}", and "{z}" denote the values of x, y, and z,
respectively.
In addition, confirm the return string by giving the arguments x=12, y="temperature",
and z=22.4.
"""


def generate_template_based_sentence(
    x: int = 12, y: str = "temperature", z: int = 22.4
) -> str:
    """
    >>> generate_template_based_sentence()
    'temperature is 22.4 at 12'
    """
    return f"{y} is {z} at {x}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
