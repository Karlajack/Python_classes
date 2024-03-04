from random import choice
#selecting the hangman words
hangman=["JOVIAL","SMART","JUICY","HANDSOME","BRIGHT"]

# selecting the word randomly

word=choice(hangman).lower()

# printing character of randomly selected word as dashes
print(word)
guessed_word=("_"*len(word))


# counting the no of correct guesses
no_correct_guesses=0

# counting the no of incorrect guesses
no_incorrect_guesses=0

letters_guessed=[]
# creating a loop equivalent to length of the word and maximum incorrect guess allowed
while no_correct_guesses<len(word) and no_incorrect_guesses<6:   
    guess=input("Guess the Character of the word: ").lower()
    # checking if  guess is a single character
    if len(guess) !=1:      
        print("please enter a single letter,")
    # checking if guess is letter
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a LETTER.")
    # checking if guess in already in letter guessed
    elif  guess  in letters_guessed:
        print ("Letter already guessed the letter,guess another letter")   
       
    elif guess in word :
        #print (guess,end=" ")
        letters_guessed.append(guess) # Creating a list of characters chosen
        for i in range(len(word)):
            if word[i] in letters_guessed:
                guessed_word=guessed_word[:i] + word[i] + guessed_word[i+1:]
        for letter in guessed_word: 
            print(letter,end=' ')
        print()
             
        no_correct_guesses+=1          # tracking the correct guesses  
    else:
        guess not in word
        print("Letter not in word,guess another lettter")
        letters_guessed.append(guess)
        for letter in guessed_word: 
            print(letter,end=' ')
        print()

        no_incorrect_guesses+=1   # tracking incorrect guess 
           
if no_correct_guesses==len(word):
       print(f"SecretWord is {word},YOU WON")
else:    
    print(f"corretly guessed letters are: {guessed_word}")
    print(f"SecretWord is {word},YOU LOSE,good effort")

        
         
           


