def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer’s word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    availableLtrsStr = ""
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    availLtrsStr = ""
    wordGuessed = False
    alreadyGuessed = False
    correctLtrsGuessedStr = ""
    mistakesMade = 0

    print "Welcome to the game, Hangman!"
    #print "for debug - secret word is: " + secretWord
    numLet = len(secretWord)
    print "I am thinking of a word that is " + str(numLet) + " letters long."

    maxGuesses = 8
    print "You have " + str(maxGuesses - 1) + " guesses left."
    print "Available letters: " + available_letters
    
    while (maxGuesses > 0) and (wordGuessed == False):
        guessChar = raw_input('Please guess a letter. ')
        guessLowCaseCh = guessChar.lower()
        alreadyGuessed = False
        correctLetter = False
        for letter in lettersGuessed:
            if (letter == guessChar):
               print "Oops! That letter is not in my word. "
               print "You have " + str(maxGuesses - 1) + " guesses left."
               alreadyGuessed = True
               mistakesMade += 1
               break
       if (alreadyGuessed == False):
            lettersGuessed.append(guessLowCaseCh)
            availableStr = getAvailableLetters(lettersGuessed)
            correctLettersGuessedStr = getGuessedWord(secretWord, lettersGuessed)
            if guessLowCaseCh in correctLettersGuessedStr
                print "Good Guess! " + correctLettersGuessedStr
                wordGuessed = isWordGuessed(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word. "
                print "You have " + str(maxGuesses - 1) + " guesses left."
                alreadyGuessed = True
                mistakesMade += 1
 
        print "-------------------------------------------------"
        maxGuesses -= 1

    if (wordGuessed == False):
        print "Sorry, you ran out of guesses. The correct word was " + secretWorddd
        print "Mistake guesses = " str(mistakesMade) + "Correct Guesses = " + str(8 - mistakesMade)
    else:
        print "Congratulations, you won! " #+ secretWord
        print "Mistake guesses = " str(mistakesMade) + "Correct Guesses = " + str(8 - mistakesMade)
