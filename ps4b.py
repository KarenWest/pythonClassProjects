from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    validWord = False
    numChHand = 0
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList -
        # you can make a similar function that omits that test)
        validWord = isValidWord(word, hand, wordList)
        if (validWord == True):
            # Find out how much making that word is worth
            numChHand = len(hand)
            wordScore = getWordScore(word, numChHand)
            # If the score for that word is higher than your best score
            if (wordScore > maxScore):
                # Update your best score, and best word accordingly
                maxScore = wordScore
                bestWord = word

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    guessWord = ""
    validWord = False
    wordScore = 0
    handUpdate = {}
    handUpdate = hand.copy()
    # Keep track of two numbers: the number of letters left in your hand and the total score
    handLen = calculateHandlen(handUpdate)
    totalScore = 0
    n = len(handUpdate)
    
    # As long as there are still letters left in the hand:
    while (handLen > 0):
        # Display the hand
        displayHand(handUpdate)
        # Ask user for input
        guessWord = compChooseWord(handUpdate, wordList)
        # If computer has exhausted all of its choices - compChooseWord returns None:
        if (guessWord == None):
            print "computer has exhausted all of its choices - game ends"
            handLen = 0
            break
            # End the game (break out of the loop)
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            validWord = isValidWord(guessWord, handUpdate, wordList)
            if (validWord == False):
                # Reject invalid word (print a message followed by a blank line)
                guessWord + " is INVALID"
                print "Invalid word, please try again"
                print
            # Otherwise (the word is valid):
            else:
                # Tell the computer player how many points the word earned, and the updated total score,
                # in one line followed by a blank line
                wordScore = getWordScore(guessWord, n)
                totalScore += wordScore
                print '"' + guessWord + '"' + ' earned ' + str(wordScore) + ' points.  Total: ' + str(totalScore)
                print
                # Update the hand 
                handUpdate = updateHand(handUpdate, guessWord)
                handLen = calculateHandlen(handUpdate)
    # Game is over (computer exhausted all choices), so tell computer the total score
    print "Goodbye! Total score: " + str(totalScore)

    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    whatToDo = ""
    whatToDoLowCase = ""
    compOrPerson = ""
    compOrPersonLowCase = ""
    gameOn = True
    person = True
    validCommand = True
    hand = {}
    numCh = 0
    validPlayer = False
    # Ask user for input
    while (gameOn == True):
        whatToDo = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').decode('utf-8')
        whatToDoLowCase = whatToDo.lower()
        # If the input is an "e" end game:
        if (whatToDoLowCase == "e"):
            gameOn = False
            break
            # End the game (break out of the loop)
        elif (whatToDoLowCase == "n"): #deal new hand of letters to play scrabble game
            numCh = random.randrange(7,20)
            hand = dealHand(numCh)
            validCommand = True
        elif (whatToDoLowCase == "r"): #replay last hand
            if (len(hand) == 0):
                print "You have not played a hand yet.  Please play a new hand first!"
                validCommand = False
        else:
            print "Invalid command."
            validCommand = False

        if (gameOn == True) and (validCommand == True):
            validPlayer = False
            while (validPlayer == False):
                compOrPerson = raw_input('Enter u for user(real person plays) or c for computer to play instead ').decode('utf-8')
                compOrPersonLowCase = compOrPerson.lower()
                if (compOrPersonLowCase == "c"):
                    person = False
                    validPlayer = True
                elif (compOrPersonLowCase == "u"):
                    person = True
                    validPlayer = True
                else:
                    print "Invalid command - try again."
            if (person == True):
                playHand(hand, wordList, numCh)
            else: # person = False = computer
                compPlayHand(hand, wordList)


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)
    #compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
    playGame(wordList)


