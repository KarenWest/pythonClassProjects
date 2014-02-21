#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    return dict((key, hand[key] - word.count(key)) for key in hand)


def possible(word, hand):
    """
    Returns True if word which is assumed to to be correct is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    """
    return all(hand.setdefault(c, 0) >= word.count(c) for c in set(word))

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    return word in wordList and possible(word, hand)


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand[key] for key in hand)



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
    total_score = 0   
    while True:
        print 'Current Hand:',
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == '.':
            print "Goodbye!",
            break
        else:
            if not isValidWord(word, hand, wordList):
                print "That is not a valid word. Please choose another word"
            else:
                score = getWordScore(word, n)
                hand = updateHand(hand, word)
                total_score += score
                print '"%s" earned %i points. Total: %i points' % (word, score, total_score)
                if calculateHandlen(hand) == 0:
                    print "\nRun out of letters.",
                    break
                print
                
    # Game is over (ran out of letters or no more valid words), so tell user the total score and return it
    print "Total score: %i points." % total_score
    return total_score