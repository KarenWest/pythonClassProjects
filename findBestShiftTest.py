from buildCoderTest import *
from applyCoderTest import *
from applyShiftTest import *
from loadWords_isWord import *

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

        
#if __name__ == '__main__':
#    wordList = loadWords()
#    encText = applyShift('Hello, world!', 8)
#    print "text " + "Hello, world!" + " encoded with shift 8 text is " + encText
#    shiftFound = findBestShift(wordList, encText)
#    print "shift found " + str(shiftFound) + " encText before decode " + encText
#    shouldBeOrigText = applyShift(encText, shiftFound)
#    print " did we get original text back? guess at shift gave decryption: " + shouldBeOrigText
