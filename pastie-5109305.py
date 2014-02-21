    guesses = 0
    mistakesMade = 0
    count = str(len(secretWord))
    lettersGuessed = []
    availableLetters = string.ascii_lowercase
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ count + ' letters long.'

    while mistakesMade < 8:
        guesses = str(8-mistakesMade)
        print "-------------"
        print "You have " + guesses + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if not guess in availableLetters:
            print "Oops! You've Already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed):
                print "------------"
                print "Congratulations, you won!"
                return None
        else:
            lettersGuessed.append(guess)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            mistakesMade += 1
            availableLetters = getAvailableLetters(lettersGuessed)
    print("------------")
    print("Sorry you ran out of guesses. The word was " + secretWord + ".")
    return None
