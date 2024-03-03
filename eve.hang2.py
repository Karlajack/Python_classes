import random
# hangman words
hangman = ["bread", "water", "bosemary", "glucose", "orange", "white"]

# pick a word
word = random.choice(hangman)
print(word)
max_wrong = len(word)
# Dashes for each letter in a word
current_guess = "-" * len(word)
print(current_guess)
# wrong guess counter
wrong_guesses = 0
correct_guess=0
# used letters tracker
used_letters = []
#main loop
print("try to guess the word")
while wrong_guesses < max_wrong and correct_guess<len(word):
    guess = input("enter your letter guess: ")
    guess = guess.lower()
    # To check if letter was already used
    if guess in used_letters:
        print("you have used the following letters:", used_letters)
        # to check guess 
    elif guess not in used_letters and guess in word:
        print("you have guessed correctly!,")
    # adding new guessed letters to list of letters
        used_letters.append(guess)
        correct_guess+=1
         #word with mixed letters and dashes
        print(guess)
    else:
        print("sorry incorrect")
        print("_")
        # increase the number of incorrect by 1
        wrong_guesses +=1
           

           # new_current_guess = ""
            #for letter in range(len(word)): 
               # new_current_guess += current_guess[letter]
               # current_guess = new_current_guess

        
#To end the game.
if correct_guess==len(word):   
    print("The correct word is", word)
    print("You have Won!")
else:
    print("The correct word is", word)   
    print("You have lost!")