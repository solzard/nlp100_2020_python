"""
09. Typoglycemia
Write a program with the specification:
    * Receive a word sequence separated by space
    * For each word in the sequence:
        * If the word is no longer than four letters, keep the word unchanged
        * Otherwise,
            * Keep the first and last letters unchanged
            * Shuffle other letters in other positions (in the middle of the word)
Observe the result by giving a sentence.
e.g., "I couldn't believe that I could actually understand what I was reading :
the phenomenal power of the human mind ."
"""
import random


def generate_typoglycemia(sentence: str) -> str:
    words = sentence.split()
    result = [words[0]]
    shuffle_word = lambda s: "".join(random.sample(s, len(s)))
    for word in words[1:-1]:
        if len(word) <= 4:
            result.append(word)
        else:
            result.append(shuffle_word(word))
    result.append(words[-1])
    return " ".join(result)


def main():
    example = """I couldn't believe that I could actually understand what I was reading\
     : the phenomenal power of the human mind."""
    print(generate_typoglycemia(example))


if __name__ == "__main__":
    main()
