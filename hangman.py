

def display_word(secret, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in secret)

def main():
    secret_word = "python"
    guessed_letters = set()
    lives = 6

    while (lives > 0):
        print(display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            lives -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print(display_word(secret_word, guessed_letters))
            print("Congrats, you win!")
            break
    else:
        print(f"You lost. The secret word was {secret_word}.")

if __name__ == "__main__":
    main()