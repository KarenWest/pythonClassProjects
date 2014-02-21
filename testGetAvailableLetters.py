def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
#Test 1

#Function call: getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])

#Output:

#    'abcdfghjlmnoqtuvwxyz'

#Test 2

#Function call: getAvailableLetters([])

#Output:

#    'abcdefghijklmnopqrstuvwxyz'

#Random Test 1

#Function call: getAvailableLetters(['q', 'e', 'f', 's', 'd', 'r', 'l', 'u', 't'])

#Output:

#    'abcghijkmnopvwxyz'

#Random Test 2

#Function call: getAvailableLetters(['u', 'c', 'z', 'a', 'd', 't', 'x'])

#Output:

#    'befghijklmnopqrsvwy'

#Random Test 3

#Function call: getAvailableLetters(['l', 'q', 'a', 't', 'i', 's', 'y'])

#Output:

#    'bcdefghjkmnopruvwxz'

#Random Test 4

#Function call: getAvailableLetters(['t', 'x', 'o', 'b', 's', 'k', 'a', 'h', 'q', 'z', 'y'])

#Output:

#    'cdefgijlmnpruvw'
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
