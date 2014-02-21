# 6.00 Problem Set 3 - Karen West - Oct. 22nd, 2012
# 
# Hangman game
#
#Sample Output from a winning game for this hang man game:
#	Loading word list from file...
#	55900 words loaded.
#	Welcome to the game, Hangman!
#	I am thinking of a word that is 4 letters long.
#	-------------
#	You have 8 guesses left.
#	Available letters: abcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Good guess: _ a_ _
#	------------
#	You have 8 guesses left.
#	Available letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Oops! You've already guessed that letter: _ a_ _
#	------------
#	You have 8 guesses left.
#	Available letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: s
#	Oops! That letter is not in my word: _ a_ _
#	------------
#	You have 7 guesses left.
#	Available letters: bcdefghijklmnopqrtuvwxyz
#	Please guess a letter: t
#	Good guess: ta_ t
#	------------
#	You have 7 guesses left.
#	Available letters: bcdefghijklmnopqruvwxyz
#	Please guess a letter: r
#	Oops! That letter is not in my word: ta_ t
#	------------
#	You have 6 guesses left.
#	Available letters: bcdefghijklmnopquvwxyz
#	Please guess a letter: m
#	Oops! That letter is not in my word: ta_ t
#	------------
#	You have 5 guesses left.
#	Available letters: bdefghijklmnopquvwxyz
#	Please guess a letter: c
#	Good guess: tact
#	------------
#	Congratulations, you won!

#Sample output of a losing game for this hang man game:
#	Loading word list from file...
#	55900 words loaded.
#	Welcome to the game Hangman!
#	I am thinking of a word that is 4 letters long
#	-----------
#	You have 8 guesses left
#	Available Letters: abcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Oops! That letter is not in my word _ _ _ _
#	-----------
#	You have 7 guesses left
#	Available Letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: b
#	Oops! That letter is not in my word _ _ _ _
#	-----------
#	You have 6 guesses left
#	Available Letters: cdefghijklmnopqrstuvwxyz
#	Please guess a letter: c
#	Oops! That letter is not in my word _ _ _ _
#	-----------
#	You have 5 guesses left
#	Available Letters: defghijklmnopqrstuvwxyz
#	Please guess a letter: d
#	Oops! That letter is not in my word _ _ _ _
#	-----------
#	You have 4 guesses left
#	Available Letters: efghijklmnopqrstuvwxyz
#	Please guess a letter: e
#	Good guess: e_ _ e
#	-----------
#	You have 4 guesses left
#	Available Letters: fghijklmnopqrstuvwxyz
#	Please guess a letter: f
#	Oops! That letter is not in my word e_ _ e
#	-----------
#	You have 3 guesses left
#	Available Letters: ghijklmnopqrstuvwxyz
#	Please guess a letter: g
#	Oops! That letter is not in my word e_ _ e
#	-----------
#	You have 2 guesses left
#	Available Letters: hijklmnopqrstuvwxyz
#	Please guess a letter: h
#	Oops! That letter is not in my word e_ _ e
#	-----------
#	You have 1 guesses left
#	Available Letters: ijklmnopqrstuvwxyz
#	Please guess a letter: i
#	Oops! That letter is not in my word e_ _ e
#	-----------
#	Sorry, you ran out of guesses. The word was else. 
	
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
#from __future__ import unicode_literals

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, correctLettersInWord):
    guessedWordStr = ""
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    wordGuessed = False
    #print "debugging: secretWord is: " + secretWord
    lenList = len(correctLettersInWord)
    #print "length of list of correct letters = " + str(lenList)
    guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
    #print "check: does guessed word = secretWord? secretWord = " + secretWord
    #print "guessed Word = " + guessedWordStr
    if (secretWord == guessedWordStr):
        #print "You guessed the correct word!"
        wordGuessed = True
    #else:
        #print "You did NOT guess the correct word!"
    return wordGuessed

def isLetterGuessed(secretWord, guessChar):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    validChar = True
    if guessChar not in secretWord:
        validChar = False
    return validChar

def getGuessedWord(secretWord, lettersGuessed, wordGuessed, correctLettersInWord, guessChar, numLet):
    findCh = 0
    guessedWordStr = ""
    modGuessedWordStr = ""
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    findCh = secretWord.find(guessChar)
    if (findCh != -1):
        #print "letter found in secret word at index " + str(findCh)

        #must use list for correctLettersInWord since strings are immutable in Python
        #so here, cannot use replace as you do for strings, but must insert char into list,
        #and then remove the blank underscore character that follows this char you inserted
        correctLettersInWord.insert(findCh,guessChar)
        guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
        #stringGuess[: (findCh + 1)] -- take start of string to (findCh)
        #stringGuess[(findCh + 2) :] -- take char folllowing insert, skipping char after it (blank underscore), to end
        modGuessedWordStr = guessedWordStr[: (findCh + 1)] + guessedWordStr[(findCh + 2) :]
        #print "modified string guess " + modGuessedWordStr
        correctLettersInWord = []
        i = 0
        while (i < numLet):
            correctLettersInWord.append(modGuessedWordStr[i])
            #print correctLettersInWord[i]
            i += 1
        
        while (findCh != -1):
            findCh = secretWord.find(guessChar, findCh + 1)
            if (findCh != -1):
                #print "letter found in secret word at index " + str(findCh)
                correctLettersInWord.insert(findCh,guessChar)
                guessedWordStr = ""
                modGuessedWordStr = ""
                guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
                #stringGuess[: (findCh + 1)] -- take start of string to (findCh)
                #stringGuess[(findCh + 2) :] -- take char folllowing insert, skipping char after it (blank underscore), to end
                modGuessedWordStr = guessedWordStr[: (findCh + 1)] + guessedWordStr[(findCh + 2) :]
                #print "modified string guess " + modGuessedWordStr
                correctLettersInWord = []
                i = 0
                while (i < numLet):
                    correctLettersInWord.append(modGuessedWordStr[i])
                    i += 1
            #else:
                #print "no more of this guess letter in future location in string - letter was: " + guessChar
        wordGuessed = isWordGuessed(secretWord, correctLettersInWord)
    #else:
        #print "letter NOT found at this point in string - letter was: " + guessChar

    return wordGuessed, correctLettersInWord
                   
def getAvailableLetters(lettersGuessed, available_letters, guessChar):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alreadyGuessed = False
    for letter in lettersGuessed:
        if (letter == guessChar):
            print "Oops! You already guessed that character."
            alreadyGuessed = True
    if (alreadyGuessed == False):
        lettersGuessed.append(guessChar)
        available_letters = available_letters.replace(guessChar, '_')
    return lettersGuessed, available_letters, alreadyGuessed

def hangman(secretWord):
    lettersGuessed = []
    guessedWordStr = ""
    wordGuessed = False
    correctLetter = False
    #available_letters = '[a-z]'
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    correctLettersInWord = []
    print "Welcome to the game, Hangman!"
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
    # FILL IN YOUR CODE HERE...
    #print "for debug - secret word is: " + secretWord
    numLet = len(secretWord)
    print "I am thinking of a word that is " + str(numLet) + " letters long."
    i = 0
    while (i < numLet):
        correctLettersInWord.append('_')
        i += 1
    maxGuesses = 8
    guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
    print guessedWordStr
    print "You have " + str(maxGuesses - 1) + " guesses left."
    print "Available letters: " + available_letters
    
    while (maxGuesses > 0) and (wordGuessed == False):
        #decode(sys.stdin.encoding) OR decode('utf-8')
        #print "available letters to choose from are : " + available_letters
        guessChar = raw_input('Please guess a letter. ').decode('utf-8')
        alreadyGuessed = False
        correctLetter = False
        (lettersGuessed, available_letters, alreadyGuessed) = getAvailableLetters(lettersGuessed, available_letters, guessChar)
        if (alreadyGuessed == False):
            #print "calling isLetterGuessed"
            correctLetter = isLetterGuessed(secretWord, guessChar)
        #print "alreadyGuessed = " + str(alreadyGuessed)
        #print "correctLetter = " + str(correctLetter)
        if (correctLetter == True) and (alreadyGuessed == False):
            #print "correct letter guess: " + guessChar
            #now see if entire secret word has been guessed
            (wordGuessed, correctLettersInWord) = getGuessedWord(secretWord, lettersGuessed, wordGuessed, correctLettersInWord, guessChar, numLet)
            if (wordGuessed == True):
                guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
                print "Good Guess! " + guessedWordStr
            else:
                guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
                print "Good Guess! " + guessedWordStr
                print "You have " + str(maxGuesses - 1) + " guesses left."
        elif (alreadyGuessed == False):
            guessedWordStr = ''.join(correctLettersInWord) #puts list of chars in str
            print "Oops! That letter is not in my word. " + guessedWordStr
            print "You have " + str(maxGuesses - 1) + " guesses left."
 
        print "-------------------------------------------------"
        maxGuesses -= 1

    if (wordGuessed == False):
        print "Sorry, you ran out of guesses.  The correct word was " + secretWord
    else:
        print "Congratulations, you won! " #+ secretWord



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
