def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
#Test 1

#Function call: getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])

#Your output:

#    guessedWordStr eikprs
#    secretWord apple
#    guessed Correct string :  _ pp _ e
#    ' _ pp _ e'

#Correct output:

#    '_ pp_ e'

#Test 2

#Function call: getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])

#Your output:

#    guessedWordStr acdhimnrtu
#    secretWord durian
#    guessed Correct string : durian
#    'durian'

#Correct output:

#    'durian'

#Random Test 1

#Function call: getGuessedWord('pineapple', ['h', 'j', 'v', 't', 'k', 'z', 'e', 'i', 'c', 'y'])

#Your output:

#    guessedWordStr hjvtkzeicy
#    secretWord pineapple
#    guessed Correct string :  _ i _ e _  _  _  _ e
#    ' _ i _ e _  _  _  _ e'

#Correct output:

#    '_ i_ e_ _ _ _ e'

#Random Test 2

#Function call: getGuessedWord('banana', ['z', 'e', 'i', 'k', 'q', 'x', 'w', 'v', 'l', 'r'])

#Your output:

#    guessedWordStr zeikqxwvlr
#    secretWord banana
#    guessed Correct string :  _  _  _  _  _  _ 
#    ' _  _  _  _  _  _ '

#Correct output:

#    '_ _ _ _ _ _ '

#Random Test 3

#Function call: getGuessedWord('pineapple', [])

#Your output:

#    guessedWordStr 
#    secretWord pineapple
#    guessed Correct string :  _  _  _  _  _  _  _  _  _ 
#    ' _  _  _  _  _  _  _  _  _ '

#Correct output:

#    '_ _ _ _ _ _ _ _ _ '

#Random Test 4

#Function call: getGuessedWord('lettuce', ['z', 'x', 'w', 'g', 't', 'b', 'u', 'd', 'p', 'y'])

#Your output:

#    guessedWordStr zxwgtbudpy
#    secretWord lettuce
#    guessed Correct string :  _  _ ttu _  _ 
#    ' _  _ ttu _  _ '

#Correct output:

#    '_ _ ttu_ _ '
#Test 1

#Function call: getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])

#Output:

#    ' _ pp _ e'

#Test 2

#Function call: getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])

#Output:

#    'durian'

#Random Test 1

#Function call: getGuessedWord('lettuce', ['q', 'm', 'u', 'y', 'e', 'i', 'r', 'p', 'l', 'x'])

#Output:

#    'le _  _ u _ e'

#Random Test 2

#Function call: getGuessedWord('coconut', ['s', 'o', 'i', 'f', 'j', 'w', 'r', 'd', 'c', 'l'])

#Output:

#    'coco _  _  _ '

#Random Test 3

#Function call: getGuessedWord('banana', [])

#Output:

#    ' _  _  _  _  _  _ '

#Random Test 4

#Function call: getGuessedWord('banana', ['d', 'u', 'l', 'v', 'r', 'j', 't', 'f', 'z', 'n'])

#Output:

#    ' _  _ n _ n _ '

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
