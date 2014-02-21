# -*- coding: utf-8 -*-
# 6.00 Problem Set 3 - Karen West - Oct. 23rd, 2012
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessedWordStr = ""
    
    guessedWordStr = ''.join(lettersGuessed) #puts list of chars in str
    wordGuessed = False
    findStr = 0
    findLtr = 0
    #print "guessedWordStr " + guessedWordStr
    #print "secretWord " + secretWord
    findStr = guessedWordStr.find(secretWord)
    if (findStr != -1):
        wordGuessed = True
    else: # try finding secretWord not in order in lettersGuessed
        lenWord = len(secretWord)
        index = 0
        for letter in secretWord:
            findLtr = guessedWordStr.find(letter)
            if (findLtr == -1):
                break
            else:
                index += 1
        if (index == lenWord):
            #print "index = " + str(index) + " lenWord = " + str(lenWord)
            wordGuessed = True
    return wordGuessed

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWordStr = ""
    guessedCorrectLtrs = [] #use list since string is not mutable (in Python)
    guessedCorrectStr = ""
    
    guessedWordStr = ''.join(lettersGuessed) #puts list of chars in str
    findLtr = 0
    print "guessedWordStr " + guessedWordStr
    print "secretWord " + secretWord
    index = 0
    for letter in secretWord:
        findLtr = guessedWordStr.find(letter)
        if (findLtr == -1):
            guessedCorrectLtrs.append(' _ ')
            index += 1
        else:
            guessedCorrectLtrs.append(letter)
            index += 1
    guessedCorrectStr = ''.join(guessedCorrectLtrs) #puts list of chars in str
    print "guessed Correct string : " + guessedCorrectStr
    
    return guessedCorrectStr

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
# FILL IN YOUR CODE HERE...

    guessedWordStr = ""
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    availableLtrs = [] #use list since string is not mutable (in Python)
    availableStr = ""
    
    guessedWordStr = ''.join(lettersGuessed) #puts list of chars in str
    print "guessedWordStr " + guessedWordStr
    index = 0
    for letter in available_letters:
        findLtr = guessedWordStr.find(letter)
        if (findLtr == -1):
            availableLtrs.append(letter)
            index += 1
        else:
            index += 1
    availableStr = ''.join(availableLtrs) #puts list of chars in str
    print "letters not yet guessed - string : " + availableStr
    
    return availableStr

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
    print "-----------"    
    maxGuesses = 8
    print "You have " + str(maxGuesses) + " guesses left."
    print "Available letters: " + available_letters

    while (maxGuesses > 0) and (wordGuessed == False):
        guessChar = raw_input('Please guess a letter. ').decode('utf-8')
        guessLowCaseCh = guessChar.lower()
        alreadyGuessed = False
        correctLetter = False
        for letter in lettersGuessed:
            if (letter == guessChar) and (alreadyGuessed == False):
               print "Oops! You've already guessed that letter: " + correctLettersGuessedStr
               print "You have " + str(maxGuesses - 1) + " guesses left."
               alreadyGuessed = True
               mistakesMade += 1
               break
        if (alreadyGuessed == False):
            lettersGuessed.append(guessLowCaseCh)
            availableStr = getAvailableLetters(lettersGuessed)
            correctLettersGuessedStr = getGuessedWord(secretWord, lettersGuessed)
            if guessLowCaseCh in correctLettersGuessedStr:
                print "Good Guess! " + correctLettersGuessedStr
                wordGuessed = isWordGuessed(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word. " + correctLettersGuessedStr
                print "You have " + str(maxGuesses - 1) + " guesses left."
                alreadyGuessed = True
                mistakesMade += 1
 

        print "-----------"
        maxGuesses -= 1

    if (wordGuessed == False):
        print "Sorry, you ran out of guesses. The correct word was " + secretWord
        print "Mistake guesses = " + str(mistakesMade) + " Correct Guesses = " + str(8 - mistakesMade)
    else:
        print "Congratulations, you won! " #+ secretWord
        print "Mistake guesses = " + str(mistakesMade) + " Correct Guesses = " + str(8 - mistakesMade)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

#NOTE - They said it failed--ridiculous--slight text difference--passes all tests!
'''
Function call: hangman(c)

Testing if we can correctly guess a short word...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. c
    Good Guess! c
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: c
    Good guess: c
    -----------
    Congratulations, you won!
    None

Function call: hangman(zzz)

Testing if we can correctly fill in repeat letters ...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. z
    Good Guess! zzz
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: z
    Good guess: zzz
    -----------
    Congratulations, you won!
    None

Function call: hangman(c)

Testing if we can incorrectly guess a short word...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. a
    Oops! That letter is not in my word. _ 
    You have 7 guesses left.
    -----------
    Please guess a letter. b
    Oops! That letter is not in my word. _ 
    You have 6 guesses left.
    -----------
    Please guess a letter. d
    Oops! That letter is not in my word. _ 
    You have 5 guesses left.
    -----------
    Please guess a letter. e
    Oops! That letter is not in my word. _ 
    You have 4 guesses left.
    -----------
    Please guess a letter. f
    Oops! That letter is not in my word. _ 
    You have 3 guesses left.
    -----------
    Please guess a letter. g
    Oops! That letter is not in my word. _ 
    You have 2 guesses left.
    -----------
    Please guess a letter. h
    Oops! That letter is not in my word. _ 
    You have 1 guesses left.
    -----------
    Please guess a letter. i
    Oops! That letter is not in my word. _ 
    You have 0 guesses left.
    -----------
    Sorry, you ran out of guesses. The correct word was c
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: a
    Oops! That letter is not in my word: _ 
    -----------
    You have 7 guesses left
    Available Letters: bcdefghijklmnopqrstuvwxyz
    Please guess a letter: b
    Oops! That letter is not in my word: _ 
    -----------
    You have 6 guesses left
    Available Letters: cdefghijklmnopqrstuvwxyz
    Please guess a letter: d
    Oops! That letter is not in my word: _ 
    -----------
    You have 5 guesses left
    Available Letters: cefghijklmnopqrstuvwxyz
    Please guess a letter: e
    Oops! That letter is not in my word: _ 
    -----------
    You have 4 guesses left
    Available Letters: cfghijklmnopqrstuvwxyz
    Please guess a letter: f
    Oops! That letter is not in my word: _ 
    -----------
    You have 3 guesses left
    Available Letters: cghijklmnopqrstuvwxyz
    Please guess a letter: g
    Oops! That letter is not in my word: _ 
    -----------
    You have 2 guesses left
    Available Letters: chijklmnopqrstuvwxyz
    Please guess a letter: h
    Oops! That letter is not in my word: _ 
    -----------
    You have 1 guesses left
    Available Letters: cijklmnopqrstuvwxyz
    Please guess a letter: i
    Oops! That letter is not in my word: _ 
    -----------
    Sorry, you ran out of guesses. The word was c.
    None

Function call: hangman(sea)

Testing if we handle repeat correct guesses...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. a
    Good Guess! _ _ a
    -----------
    Please guess a letter. e
    Good Guess! _ ea
    -----------
    Please guess a letter. a
    Oops! You've already guessed that letter: _ ea
    You have 5 guesses left.
    -----------
    Please guess a letter. e
    Oops! You've already guessed that letter: _ ea
    You have 4 guesses left.
    -----------
    Please guess a letter. s
    Good Guess! sea
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: a
    Good guess: _ _ a
    -----------
    You have 8 guesses left
    Available Letters: bcdefghijklmnopqrstuvwxyz
    Please guess a letter: e
    Good guess: _ ea
    -----------
    You have 8 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: a
    Oops! You've already guessed that letter: _ ea
    -----------
    You have 8 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: e
    Oops! You've already guessed that letter: _ ea
    -----------
    You have 8 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: s
    Good guess: sea
    -----------
    Congratulations, you won!
    None

Function call: hangman(y)

Testing if we handle repeat incorrect guesses...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. x
    Oops! That letter is not in my word. _ 
    You have 7 guesses left.
    -----------
    Please guess a letter. z
    Oops! That letter is not in my word. _ 
    You have 6 guesses left.
    -----------
    Please guess a letter. x
    Oops! You've already guessed that letter: _ 
    You have 5 guesses left.
    -----------
    Please guess a letter. z
    Oops! You've already guessed that letter: _ 
    You have 4 guesses left.
    -----------
    Please guess a letter. y
    Good Guess! y
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 1 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: x
    Oops! That letter is not in my word: _ 
    -----------
    You have 7 guesses left
    Available Letters: abcdefghijklmnopqrstuvwyz
    Please guess a letter: z
    Oops! That letter is not in my word: _ 
    -----------
    You have 6 guesses left
    Available Letters: abcdefghijklmnopqrstuvwy
    Please guess a letter: x
    Oops! You've already guessed that letter: _ 
    -----------
    You have 6 guesses left
    Available Letters: abcdefghijklmnopqrstuvwy
    Please guess a letter: z
    Oops! You've already guessed that letter: _ 
    -----------
    You have 6 guesses left
    Available Letters: abcdefghijklmnopqrstuvwy
    Please guess a letter: y
    Good guess: y
    -----------
    Congratulations, you won!
    None
'''

#And their more complex test cases got the following output (more points lost!)
'''
Function call: hangman(zzz)

Testing if we can correctly fill in repeat letters and handle capitalized input ...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. Z
    Good Guess! zzz
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 3 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: Z
    Good guess: zzz
    -----------
    Congratulations, you won!
    None

Function call: hangman(camel)

Testing if we can correctly guess a word...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 5 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. a
    Good Guess! _ a_ _ _ 
    -----------
    Please guess a letter. e
    Good Guess! _ a_ e_ 
    -----------
    Please guess a letter. i
    Oops! That letter is not in my word. _ a_ e_ 
    You have 5 guesses left.
    -----------
    Please guess a letter. m
    Good Guess! _ ame_ 
    -----------
    Please guess a letter. n
    Oops! That letter is not in my word. _ ame_ 
    You have 3 guesses left.
    -----------
    Please guess a letter. l
    Good Guess! _ amel
    -----------
    Please guess a letter. k
    Oops! That letter is not in my word. _ amel
    You have 1 guesses left.
    -----------
    Please guess a letter. c
    Good Guess! camel
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 5 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: a
    Good guess: _ a_ _ _ 
    -----------
    You have 8 guesses left
    Available Letters: bcdefghijklmnopqrstuvwxyz
    Please guess a letter: e
    Good guess: _ a_ e_ 
    -----------
    You have 8 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: i
    Oops! That letter is not in my word: _ a_ e_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghjklmnopqrstuvwxyz
    Please guess a letter: m
    Good guess: _ ame_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghjklnopqrstuvwxyz
    Please guess a letter: n
    Oops! That letter is not in my word: _ ame_ 
    -----------
    You have 6 guesses left
    Available Letters: bcdfghjklopqrstuvwxyz
    Please guess a letter: l
    Good guess: _ amel
    -----------
    You have 6 guesses left
    Available Letters: bcdfghjkopqrstuvwxyz
    Please guess a letter: k
    Oops! That letter is not in my word: _ amel
    -----------
    You have 5 guesses left
    Available Letters: bcdfghjopqrstuvwxyz
    Please guess a letter: c
    Good guess: camel
    -----------
    Congratulations, you won!
    None

Function call: hangman(guanabana)

Testing if we run out of guesses...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 9 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. E
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 7 guesses left.
    -----------
    Please guess a letter. O
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 6 guesses left.
    -----------
    Please guess a letter. M
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 5 guesses left.
    -----------
    Please guess a letter. L
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 4 guesses left.
    -----------
    Please guess a letter. R
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 3 guesses left.
    -----------
    Please guess a letter. S
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 2 guesses left.
    -----------
    Please guess a letter. T
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 1 guesses left.
    -----------
    Please guess a letter. Z
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ 
    You have 0 guesses left.
    -----------
    Sorry, you ran out of guesses. The correct word was guanabana
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 9 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: E
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 7 guesses left
    Available Letters: abcdfghijklmnopqrstuvwxyz
    Please guess a letter: O
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 6 guesses left
    Available Letters: abcdfghijklmnpqrstuvwxyz
    Please guess a letter: M
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 5 guesses left
    Available Letters: abcdfghijklnpqrstuvwxyz
    Please guess a letter: L
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 4 guesses left
    Available Letters: abcdfghijknpqrstuvwxyz
    Please guess a letter: R
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 3 guesses left
    Available Letters: abcdfghijknpqstuvwxyz
    Please guess a letter: S
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 2 guesses left
    Available Letters: abcdfghijknpqtuvwxyz
    Please guess a letter: T
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    You have 1 guesses left
    Available Letters: abcdfghijknpquvwxyz
    Please guess a letter: Z
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ 
    -----------
    Sorry, you ran out of guesses. The word was guanabana.
    None

Function call: hangman(senselessness)

Testing if we can correctly fill in multiple letters...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 13 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. a
    Oops! That letter is not in my word. _ _ _ _ _ _ _ _ _ _ _ _ _ 
    You have 7 guesses left.
    -----------
    Please guess a letter. e
    Good Guess! _ e_ _ e_ e_ _ _ e_ _ 
    -----------
    Please guess a letter. s
    Good Guess! se_ se_ ess_ ess
    -----------
    Please guess a letter. n
    Good Guess! sense_ essness
    -----------
    Please guess a letter. l
    Good Guess! senselessness
    -----------
    Congratulations, you won! 
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 13 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: a
    Oops! That letter is not in my word: _ _ _ _ _ _ _ _ _ _ _ _ _ 
    -----------
    You have 7 guesses left
    Available Letters: bcdefghijklmnopqrstuvwxyz
    Please guess a letter: e
    Good guess: _ e_ _ e_ e_ _ _ e_ _ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: s
    Good guess: se_ se_ ess_ ess
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrtuvwxyz
    Please guess a letter: n
    Good guess: sense_ essness
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmopqrtuvwxyz
    Please guess a letter: l
    Good guess: senselessness
    -----------
    Congratulations, you won!
    None

Function call: hangman(cheetah)

Testing if we correctly handle repeat guesses...

Your output:

    Welcome to the game Hangman!
    I am thinking of a word that is 7 letters long.
    -----------
    You have 8 guesses left.
    Available letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter. A
    Good Guess! _ _ _ _ _ a_ 
    -----------
    Please guess a letter. e
    Good Guess! _ _ ee_ a_ 
    -----------
    Please guess a letter. z
    Oops! That letter is not in my word. _ _ ee_ a_ 
    You have 5 guesses left.
    -----------
    Please guess a letter. t
    Good Guess! _ _ eeta_ 
    -----------
    Please guess a letter. a
    Oops! You've already guessed that letter: _ _ eeta_ 
    You have 3 guesses left.
    -----------
    Please guess a letter. z
    Oops! You've already guessed that letter: _ _ eeta_ 
    You have 2 guesses left.
    -----------
    Please guess a letter. E
    Good Guess! _ _ eeta_ 
    -----------
    Please guess a letter. r
    Oops! That letter is not in my word. _ _ eeta_ 
    You have 0 guesses left.
    -----------
    Sorry, you ran out of guesses. The correct word was cheetah
    None

Correct output:

    Welcome to the game Hangman!
    I am thinking of a word that is 7 letters long
    -----------
    You have 8 guesses left
    Available Letters: abcdefghijklmnopqrstuvwxyz
    Please guess a letter: A
    Good guess: _ _ _ _ _ a_ 
    -----------
    You have 8 guesses left
    Available Letters: bcdefghijklmnopqrstuvwxyz
    Please guess a letter: e
    Good guess: _ _ ee_ a_ 
    -----------
    You have 8 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxyz
    Please guess a letter: z
    Oops! That letter is not in my word: _ _ ee_ a_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrstuvwxy
    Please guess a letter: t
    Good guess: _ _ eeta_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrsuvwxy
    Please guess a letter: a
    Oops! You've already guessed that letter: _ _ eeta_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrsuvwxy
    Please guess a letter: z
    Oops! You've already guessed that letter: _ _ eeta_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrsuvwxy
    Please guess a letter: E
    Oops! You've already guessed that letter: _ _ eeta_ 
    -----------
    You have 7 guesses left
    Available Letters: bcdfghijklmnopqrsuvwxy
    Please guess a letter: r
    Oops! That letter is not in my word: _ _ eeta_ 
    -----------
    You have 6 guesses left
    Available Letters: bcdfghijklmnopqsuvwxy
    Please guess a letter: t
    Oops! You've already guessed that letter: _ _ eeta_ 
    -----------
    You have 6 guesses left
    Available Letters: bcdfghijklmnopqsuvwxy
    Please guess a letter: h
    Good guess: _ heetah
    -----------
    You have 6 guesses left
    Available Letters: bcdfgijklmnopqsuvwxy
    Please guess a letter: c
    Good guess: cheetah
    -----------
    Congratulations, you won!
    None
'''
