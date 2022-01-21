from wordle_dictionary import Hint
import wordle_dictionary as wd
import solver


def main():
    ALL_WORDS = wd.get_presentables()
    cracked_on = [0] * 7
    default_possibles = {word : solver.weigh_word(word) for word in wd.get_guessables()}
    # Test all words
    for windex, w in enumerate(ALL_WORDS):
        print(f"{windex:4}/{len(ALL_WORDS):4}") if windex % 100 == 0 else ...
        # Initialize
        best_guess = ""
        hints = []
        possibles = {k : v for k, v in default_possibles.items()}
        for i in range(6):
            # Provide guess
            best_guess, possibles = solver.solve_step(best_guess, hints, possibles)
            # Get results of best guess
            if best_guess == w:
                cracked_on[i+1] += 1
                break
            hints = wd.validate_guess(best_guess, w)
        else:
            cracked_on[0] += 1
    
    for turn, solutions in enumerate(cracked_on):
        if turn == 0:
            print(f"Unsolved:\t{solutions}")
        else:
            print(f"Turn {turn}:\t\t{solutions}")


if __name__ == "__main__":
    main()