import wordle
import solver

def main():
    option = input("What would you like to do?\n(w) Play Wordle\n(s) Solve Wordle\n").lower().strip()
    if option == "w":
        wordle.start_game()
    elif option == "s":
        solver.solve_puzzle()
    else:
        print("oh ok bye")


if __name__ == "__main__":
    main()