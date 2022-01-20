import wordle

def main():
    option = input("Would you like to play Wordle? (y/n): ").lower().strip()
    if option == "y":
        wordle.start_game()
    else:
        print("oh ok bye")


if __name__ == "__main__":
    main()