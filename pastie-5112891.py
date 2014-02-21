def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %i letters long' % len(secretWord))
    used = ''
    guess = 8
    while guess and not isWordGuessed(secretWord, used):
        print('-' * 11)
        print('You have %i guesses left' % guess)
        available = getAvailableLetters(used)
        print('Available Letters: %s' % available)
        c = raw_input('Please guess a letter: ').lower()
        if len(c) == 1:
            if not c.isalpha():
                print('That is not letter!')  
            else:
                if c in available:
                    used += c
                    if c in secretWord:
                        print 'Good guess:',
                    else:
                        print 'Oops! That letter is not in my word:',
                        guess -= 1
                else:
                    print "Oops! You've already guessed that letter:",
        else:
            print("Input exactly one letter!")
        print(getGuessedWord(secretWord, used))

    print('-' * 11)  
    if isWordGuessed(secretWord, used):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was %s.' % secretWord)
