from time import perf_counter

import wordle_dictionary as wd


def main():
    w = wd.get_word()
    unusable = set()
    for i in range(6):
        guess = input(f"GUESS {i+1}:\nGuess a 5-letter word:\n\n").lower().strip()
        if len(guess) != 5 or not wd.is_guessable(guess):
            print("\nInvalid guess.\n")
            continue
        hints = wd.validate_guess(guess, w)
        for i, hint in enumerate(hints):
            print(hint.value, end="")
            if hint == wd.Hint.BLACK:
                unusable.add(guess[i])
        if i == 0:
            print(f"\n\nNOTE:\n{wd.Hint.BLACK.value} = Not in word\n{wd.Hint.YELLOW.value} = In word, wrong position\n{wd.Hint.GREEN.value} = Correct\n")
        else:
            print("\n")
        print(f"Cannot use: {unusable}\n")
        if guess == w:
            break
    else:
        print(f"Game over! The word was: '{w}'\n")
    again = input(f"Would you like to play again? (y/n): ").lower().strip()
    if again == "y":
        main()


if __name__ == "__main__":
    main()