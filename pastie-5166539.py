# Hangman game

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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    count = 0
    assert isinstance(lettersGuessed, list)
    for ltr in lettersGuessed:
        for x in range(len(secretWord)):
            if ltr == secretWord[x]:
                count +=1
    if count >= len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    returnString = ""
    for x in secretWord:
        returnString += "_ "
    if isWordGuessed(secretWord,lettersGuessed):
        return secretWord
    else:
        assert isinstance(lettersGuessed, list)
        for ltr in lettersGuessed:
            y = 0
            for x in range(len(secretWord)):
                if ltr == secretWord[x]:
                    returnString = returnString[:y] +secretWord[x] +returnString[y+1:]
                y += 2
    return returnString

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    allAvailableLetters = string.ascii_lowercase
    for ltr in allAvailableLetters:
        assert isinstance(lettersGuessed, list)
        if lettersGuessed.__contains__(ltr):
            allAvailableLetters = allAvailableLetters[0:allAvailableLetters.index(ltr)] +\
                                  allAvailableLetters[ allAvailableLetters.index(ltr) +1 : ]
    return allAvailableLetters

def hangman(secretWord):
    """
    :type secretWord:
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
    """
    secretWord.lower()
    lettersGuessed = []
    chancesAvailable = 8
    index = 0
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " +str(len(secretWord)) +" letters long")
    print("-----------")
    while chancesAvailable:
        print("You have " +str(chancesAvailable) +" guesses left")
        print("Available Letters: " +getAvailableLetters(lettersGuessed))
        lettersGuessed.extend(raw_input("Please guess a letter: ").lower())
        if secretWord.find(lettersGuessed[index]) >= 0:
            print("Good guess: " +getGuessedWord(secretWord,lettersGuessed))
        else:
            print("Oops! You've already guessed that letter: " +getGuessedWord(secretWord,lettersGuessed))
            if getAvailableLetters(lettersGuessed) != getAvailableLetters(lettersGuessed[0:-1]):
                chancesAvailable -= 1
        index += 1
        print("-----------")
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print("Congratulations, you won!")
            break
    if isWordGuessed(secretWord,lettersGuessed) == False:
        print("Sorry, you ran out of guesses. The word was " +secretWord +".")
