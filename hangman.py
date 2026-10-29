MAX_LIVES = 6

def display_word(secret, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in secret)

def display_lives_left(lives):
    return ("❤️ " * lives + "🖤" * (MAX_LIVES - lives))

def main():
    secret_word = "python"
    guessed_letters = set()
    lives = MAX_LIVES

    while (lives > 0):
        print(display_word(secret_word, guessed_letters) + "\t" + display_lives_left(lives))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("Letter already guessed. Try again.")
        elif guess not in secret_word:
            lives -= 1

        guessed_letters.add(guess)

        if all(letter in guessed_letters for letter in secret_word):
            print(display_word(secret_word, guessed_letters) + "\t" + display_lives_left(lives))
            print("Congrats, you win!")
            break
    else:
        print(f"You lost. The secret word was {secret_word}.")

if __name__ == "__main__":
    main()