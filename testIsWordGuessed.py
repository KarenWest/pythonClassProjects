def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
#NOTE:
#The is keyword is a test for object identity while == is a value comparison.

#If you use "is", the result will be true if and only if the object is the same
#object. However, "==" will be true any time the values of the object are the
#same.

#Test cases submitted against:
#Test 1

#Function call: isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])

#Output:

#    False

#Test 2

#Function call: isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])

#Your output:

#    False

#Correct output:

#    True

#Random Test 1

#Function call: isWordGuessed('grapefruit', ['c', 'w', 'i', 'a', 'b', 'h', 'p', 'n', 'm', 'y'])

#Output:

#    False

#Random Test 2

#Function call: isWordGuessed('banana', ['u', 'l', 'a', 'e', 'o', 'n', 'x', 'k', 's', 't'])

#Output:

#    False

#Random Test 3

#Function call: isWordGuessed('grapefruit', [])

#Output:

#    False

#Random Test 4

#Function call: isWordGuessed('pineapple', ['z', 'x', 'q', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e'])

#Output:

#    True

# Start of my code:
    guessedWordStr = ""
    
    guessedWordStr = ''.join(lettersGuessed) #puts list of chars in str
    wordGuessed = False
    findStr = 0
    findLtr = 0
    #for letter in secretWord:
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
`
#call isWordGuessed to test it here
#secretWord = "karenwest"
#lettersGuessed = ['s','h','a','y','k', 'a', 'r', 'e', 'n', 'w', 'e', 's', 't']
secretWord = "durian"
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
result = isWordGuessed(secretWord, lettersGuessed)
if (result == True):
    print "You guessed the correct word!"
else:
    print "Try again-- you did NOT guess the correct word!"
