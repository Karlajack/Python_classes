import random
# hangman words
hangman = ["berries", "water", "rosemary", "glucose", "orange", "white"]
max_wrong = len(hangman) - 1
# pick a word
word = random.choice(hangman)
print(word)
# Dashes for each letter in a word
current_guess = "-" * len(word)
print(word)
print(current_guess)
# wrong guess counter
wrong_guesses = 0
# used letters tracker
used_letters = []
#main loop
print("try to guess the word")
while wrong_guesses < max_wrong and current_guess != word:
    print(hangman[wrong_guesses])
    print("you have used the following letters:", used_letters)
    print("so far the word is:", current_guess)
    guess = input("enter your letter guess: ")
    guess = guess.upper()
# To check if letter was already used
    while guess in used_letters:
        print("you have already guessed that letter", guess)
        guess = input("enter your letter guess:")
        guess = guess.upper()
    # adding new guessed letters to list of letters
    used_letters.append(guess)
    # to check guess
    if guess in word:
        print("you have guessed correctly!")