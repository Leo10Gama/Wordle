from enum import Enum
from random import choice
from typing import List


FILE_GUESSABLE = "words/5guessable.txt"
FILE_PRESENTABLE = "words/5presentable.txt"
WORD_FILES = [FILE_PRESENTABLE, FILE_GUESSABLE]


class Hint(Enum):
    """An enum to represent hint colours.
    
    Like in the original Wordle, each colour says something about a given 
    letter's position in the word:
    `BLACK` means the letter is nowhere in the word.
    `YELLOW` means the letter is in the word, but in the incorrect position.
    `GREEN` means the letter is in the correct position in the word.
    """
    BLACK = "b"
    YELLOW = "y"
    GREEN = "g"


def get_presentables() -> List[str]:
    """Return the list of all words that can be presented."""

    words = []
    with open(FILE_PRESENTABLE, "r") as f:
        for line in f.readlines():
            words.append(line.strip())
    return words


def get_guessables() -> List[str]:
    """Return the list of all guessable words."""

    words = get_presentables()  # Presentable words can also be guessed
    with open(FILE_GUESSABLE, "r") as f:
        for line in f.readlines():
            words.append(line.strip())
    return words


def is_guessable(word: str) -> bool:
    """Check whether a word can be guessed."""
    
    return word in get_guessables()


def get_word() -> str:
    """Get a 5 letter word for the game."""

    return choice(get_presentables())


def validate_guess(guess: str, word: str) -> List[Hint]:
    """Return the guess information.
    
    The List returned will be of size 5 exactly, where each index `i` 
    corresponds to the status of the `i`th character in the guess.
    """
    hints = []
    for i, c in enumerate(guess):
        if c not in word:   # Letter not in word
            hints.append(Hint.BLACK)
        elif word[i] == c:  # Letter in correct position
            hints.append(Hint.GREEN)
        else:               # Letter in word, but wrong position
            hints.append(Hint.YELLOW)
    return hints
