# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

LOWER_CASE_LETTERS = string.ascii_lowercase
UPPER_CASE_LETTERS = string.ascii_uppercase
#" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"" --all but the numerics below
PUNCTUATION_NUMERICS_SPACE = " " + string.punctuation + "0123456789"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dictForCipher = {}

    for letter in LOWER_CASE_LETTERS:
        i = LOWER_CASE_LETTERS.find(letter)
        j = i + shift
        if (j > 25):
            #wrap around
            wrapNum = j - 26
            j = wrapNum
        cipherLetter = LOWER_CASE_LETTERS[j]
        dictForCipher[letter] = dictForCipher.setdefault(letter, cipherLetter)
        #print "letter " + letter + " cipher letter " + cipherLetter + " shift was " + str(shift)

    for letter in UPPER_CASE_LETTERS:
        i = UPPER_CASE_LETTERS.find(letter)
        j = i + shift
        if (j > 25):
            #wrap around
            wrapNum = j - 26
            j = wrapNum
        cipherLetter = UPPER_CASE_LETTERS[j]
        dictForCipher[letter] = dictForCipher.setdefault(letter, cipherLetter)
        #print "letter " + letter + " cipher letter " + cipherLetter + " shift was " + str(shift)

    return(dictForCipher)

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedText = ""
    coderCopy = coder.copy()

    for letter in text:
        if letter not in PUNCTUATION_NUMERICS_SPACE:
            for ltrKey, ltrVal in coderCopy.items():
                if ltrKey == letter:
                    encodedText += ltrVal
        else:
            encodedText += letter
    #print PUNCTUATION_NUMERICS_SPACE
    #print " !@#$%^&*()-_+={}[]|\\:;'<>?,./\""
    return encodedText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
    

#
# Problem 2: Decryption
#
'''
PSEUDOCODE PROVIDED BY PEOPLE WHO DESIGNED COURSE (findBestShift()):

=========================
Problem 2: findBestShifts
=========================

1. Set the maximum number of real words found to 0.
2. Set the best shift to 0.
3. For each possible shift from 0 to 26:
	4. Shift the entire text by this shift.
	5. Split the text up into a list of the individual words.
	6. Count the number of valid words in this list.
	7. If this number of valid words is more than the largest number of
	   real words found, then:
		8. Record the number of valid words.
		9. Set the best shift to the current shift.
	10. Increment the current possible shift by 1. Repeat the loop
	   starting at line 3.
11. Return the best shift.

PSEUDOCODE I WROTE MYSELF:
--ShiftGuess = Make Random Guess beteween 0-26.
--Apply Shift(message, 26 - ShiftGuess)
--Apply isWord() helper function to message to determine if the words
in the message are valid words OR if a word may be misspelled in her email,
count the most number of valid words in a message, and that is likely the
best shift key, if not all words were valid for any shift key in 0-26.
    
You may find the function string.split useful for dividing the text up into words. 
'''
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxNumRealWords = 0
    textCopy = text
    numRealWords = 0
    decodedWordList = []
    decodedText = ""
    decodedText = applyShift(textCopy, 0) #have to do zero case separately or their assertion fails
    decodedWordList = decodedText.split(" ")
    for word in decodedWordList:
        if (isWord(wordList, word) == True):
            numRealWords += 1
    numRealWords = maxNumRealWords
    bestShift = 0

    for shift in range(1,26):
        textCopy = text
        numRealWords = 0
        decodedWordList = []
        decodedText = ""
        decodedText = applyShift(textCopy, 26 - shift)
        decodedWordList = decodedText.split(" ")
        for word in decodedWordList:
            if (isWord(wordList, word) == True):
                numRealWords += 1
        if (numRealWords > maxNumRealWords):
            bestShift = 26 - shift
            maxNumRealWords = numRealWords
    return (bestShift)    
    
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    storyString = getStoryString()
    shiftFound = findBestShift(wordList, storyString)
    print "shift found " + str(shiftFound) + " encText before decode " + storyString
    shouldBeOrigText = applyShift(storyString, shiftFound)
    #print " did we get original text back? guess at shift gave decryption: " + shouldBeOrigText
    return shouldBeOrigText

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()
