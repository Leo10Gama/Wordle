from collections import defaultdict
from importlib.machinery import WindowsRegistryFinder
from typing import Dict, List
import wordle_dictionary as wd


# Values each letter based on its frequency
# Values taken from en.wikipedia.org/wiki/Letter_frequency
ALPHABET_WEIGHTS = {
    "a": 7.8,
    "b": 2.0,
    "c": 4.0,
    "d": 3.8,
    "e": 11.0,
    "f": 1.4,
    "g": 3.0,
    "h": 2.3,
    "i": 8.2,
    "j": 0.21,
    "k": 2.5,
    "l": 5.3,
    "m": 2.7,
    "n": 7.2,
    "o": 6.1,
    "p": 2.8,
    "q": 0.24,
    "r": 7.3,
    "s": 8.7,
    "t": 6.7,
    "u": 3.3,
    "v": 1.0,
    "w": 0.91,
    "x": 0.27,
    "y": 1.6,
    "z": 0.44
}


def weigh_word(word: str) -> float:
    """Assign a given word a numeric value based on its letter frequency.
    
    Pre: `word` is in all lowercase
    """

    total = 0
    seen = defaultdict(int)
    for letter in word:
        seen[letter] += 1
        total += ALPHABET_WEIGHTS[letter] / seen[letter]
    return total


def solve_step(entered_word: str, hints: List[wd.Hint], curr_possible: Dict[str, float]=None) -> str:
    """Given a word and its hints, return the most likely word it is.
    
    Pre: `entered_word` is lowercase; `len(hints) == 5`
    """

    # Make sure there are possible values
    if curr_possible is None:
        curr_possible = {word : weigh_word(word) for word in wd.get_guessables()}
    # Iterate through guess to remove invalid possibilities
    for i, h in enumerate(hints):
        letter = entered_word[i]
        if h == wd.Hint.BLACK:      # Letter not in word; remove all words with that letter
            curr_possible = {word : val for (word, val) in curr_possible.items() if letter not in word}
        elif h == wd.Hint.GREEN:    # Letter in correct position; remove words that dont have that letter in that position
            curr_possible = {word : val for (word, val) in curr_possible.items() if word[i] == letter}
        elif h == wd.Hint.YELLOW:   # Letter in word but not position; remove words with letter in position and words without letter
            curr_possible = {word : val for (word, val) in curr_possible.items() if word[i] != letter and letter in word}
    # Return the next most likely word
    return max(curr_possible, key=curr_possible.get), curr_possible


def solve_puzzle():
    """Driver function to solve Wordles."""

    # Initialize
    best_guess = ""
    hints = []
    possibles = {word : weigh_word(word) for word in wd.get_guessables()}
    for _ in range(6):
        # Provide guess
        best_guess, possibles = solve_step(best_guess, hints, possibles)
        print(f"Best guess: {best_guess} (out of {len(possibles)} results)")
        print(f"(Enter to continue)")
        input()
        # Get results of best guess
        if input(f"Did you win? (y/n) ").lower() == "y":
            break
        hints = input(f"What was the result of that guess?\n(Use b=Black, y=Yellow, g=Green): ").lower()
        hints = [wd.Hint(h) for h in hints]
        print()
    else:
        print("Better luck next time!")
        return
    print(f"Congrats!!")
    return


if __name__ == "__main__":
    solve_puzzle()
