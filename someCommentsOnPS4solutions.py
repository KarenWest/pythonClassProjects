
Problem set 4; some solutions by Mabooka18

I just don't get reddit: don't understand how to use it, don't like it. So here is my code right here in our wiki.

Disclaimer: I learned and used some stuff that was not yet taught here, namely list comprehension and some functional stuff.

1) One thing that bothered me was, in playHand(hand, wordList, n) I had to output :

    Current Hand: p z u t t t o

obviously using the already provided displayHand(), like this:

print "Current Hand: ",
displayHand(hand)

Which seemed just plain ugly: TWO lines of CODE for ONE line of output?!?

So I changed it to:

print "Current Hand:  %s" % repr_hand(hand)

Of course that required a new function repr_hand ("aka represent hand") : it returned exactly what the MIT's displayHand would print, but with no printing, just as a string. That allowed me also to change the implementation of displayHand to just one line. Here we go:

def repr_hand(hand):
    return "".join([("%s " % (k)) * v for k, v in hand.items()] )

def displayHand(hand):
    print repr_hand(hand)

2) Feeling good about one-liners, I wrote these:

def loadWords():
    return set([ln.strip().lower() for ln in open(WORDLIST_FILENAME)])

from collections import Counter
def getFrequencyDict(sequence):
    return Counter(sequence)

def getWordScore(word, n):
    return sum([SCRABBLE_LETTER_VALUES[ch] for ch in word])*len(word) + (len(word) == n and 50 or 0)

3) in isValidWord, there are two tests: whether the word is in wordList and whether the word can be 'constructed' from the hand. So naturally it gave:

def isValidWord(word, hand, wordList):
    return word in wordList and can_construct(word, hand)

Here, can_construct() is a function that figures out whether the word can be constructed from letters in the hand:

def can_construct(word, hand):
    # Can the word be constructed from letters in the hand?
    # This simulates building the word from the hand:
    nh = hand.copy()
    for ch in word:
        if not ch in nh:
            return False # some letter cannot be found: cannot construct
        nh[ch] -= 1
        if nh[ch] < 0:
            return False

    return True

4) the hand's length:

def calculateHandlen(hand):
    return sum(hand.values())

5) But what really manifests the incredible beauty of Python is this:

def compChooseWord(hand, wordList):
    good_words = [w for w in wordList if can_construct(w, hand)]
    if not good_words: 
        return None # special case
    return max(good_words, key = lambda w: getWordScore(w, HAND_SIZE))

Notice that this function searches for a word in good_words, but... there is no loop :-). Python rocks!

Thanks for reading and of course feel free to add your questions or comments here.
