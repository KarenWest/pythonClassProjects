#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    total = 0
    for h in hand:
        total += hand[h]
    return total



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # As long as there are still letters left in the hand:
    letters_left = calculateHandlen(hand)
    total_score = 0
    while letters_left > 0:
    
        # Display the hand
        print('Current Hand: '),
        displayHand(hand)
        
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate ' + 
                         'that you are finished: ')
        # If the input is a single period:
        if word == '.':
            
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total_score += getWordScore(word, n)
                print(word + ' earned ' + str(getWordScore(word, n)) + 
                      ' points. Total: ' + str(total_score) + ' points') 
                
                # Update the hand
                hand = updateHand(hand, word)
                letters_left = calculateHandlen(hand)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if letters_left == 0:
        print('Run out of letters.'),
    else:
        print('Goodbye!'),
    print('Total score: ' + str(total_score) + ' points.')