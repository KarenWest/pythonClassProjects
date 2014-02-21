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
    # As long as there are still letters left in the hand:
    letters_left = len(hand)
    total_score = 0
    while letters_left > 0:
        # Display the hand
        print('Current Hand: '),
        displayHand(hand)
        # Ask user for input
        word = compChooseWord(hand, wordList)
        # If the input is a single period:
        if not word:
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            total_score += getWordScore(word, HAND_SIZE)
            print(word + ' earned ' + str(getWordScore(word, HAND_SIZE)) + 
                  ' points. Total: ' + str(total_score) + ' points') 
            # Update the hand
            hand = updateHand(hand, word)
            letters_left = calculateHandlen(hand)
    print('Total score: ' + str(total_score) + ' points.')