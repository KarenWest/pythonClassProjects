## ps3_newton.py [python]
# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    count = 0
    result = 0.0
    for a in poly:
        result += a if count == 0 else a*x**count
        count += 1
    return result


# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    b = 0.0
    result = []
    for a in poly[1:]:
        b+=1.0
        result.append(a*b)
    if b == 0.0:
        result = [0.0]
    return result


# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    count = 0
    x = x_0
    while abs(evaluatePoly(poly, x)) >= epsilon:
        x = x - (evaluatePoly(poly, x) / evaluatePoly(computeDeriv(poly), x))
        count += 1

    return [x, count]


## ps3_hangman.py [python]
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if result != '':
            result += ' '
        result += letter if letter in lettersGuessed else '_'

    return result


import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    for letter in lettersGuessed:
        available = available.replace(letter,'') # replacing with a space would look better
    return available


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
    allowedMistakes = 8
    lettersGuessed = []
    guessWord = getGuessedWord(secretWord, lettersGuessed)

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."

    while allowedMistakes > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print "-------------"
        print "You have "+str(allowedMistakes)+" guesses left."
        print "Available letters: "+getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ").lower()
        if len(guess) != 1:  # not required
            print "Oops! You have to enter a single character, try again!"
        elif guess in lettersGuessed:
            print "Oops! You've already guessed that letter: "+guessWord
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                guessWord = getGuessedWord(secretWord, lettersGuessed)
                print "Good guess: "+guessWord
            else:
                allowedMistakes -= 1
                print "Oops! That letter is not in my word: "+guessWord

    print "-------------"
    if allowedMistakes > 0:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was "+secretWord+"." 



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

