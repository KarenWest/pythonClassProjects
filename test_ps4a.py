from ps4a import *

#
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

# To run these tests, simply run this file (open up in IDLE, then run the file as normal)

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, ("fork", 4):94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print "FAILURE: test_getWordScore()"
            print "\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n)
            failure=True
    if not failure:
        print "SUCCESS: test_getWordScore()"

# end of test_getWordScore


def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"        
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2

        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"                
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        
        return # exit function

    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        
        return # exit function

    print "SUCCESS: test_updateHand()"

# end of test_updateHand

def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", handOrig

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE: test_isValidWord()"

        if handCopy != handOrig:
            print "\tTesting word", word, "for a second time - be sure you're not modifying hand."
            print "\tAt this point, hand ought to be", handOrig, "but it is", handCopy

        else:
            print "\tTesting word", word, "for a second time - have you modified wordList?"
            wordInWL = word in wordList
            print "The word", word, "should be in wordList - is it?", wordInWL

        print "\tExpected True, but got False for word: '" + word + "' and hand:", handCopy

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '"+ word +"' and hand:", hand

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand
        
        failure = True
        
    # test 6
    word = "even"

    if  isValidWord(word, hand, wordList):
        print "FAILURE: test_isValidWord()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        print "\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)"        
        
        failure = True        

    if not failure:
        print "SUCCESS: test_isValidWord()"


wordList = loadWords()
print "----------------------------------------------------------------------"
print "Testing getWordScore..."
test_getWordScore()
print "----------------------------------------------------------------------"
print "Testing updateHand..."
test_updateHand()
print "----------------------------------------------------------------------"
print "Testing isValidWord..."
test_isValidWord(wordList)
print "----------------------------------------------------------------------"
print "All done!"

'''
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
That is not a valid word. Please choose another word
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e

Scoring

        The score for the hand is the sum of the scores for each word formed.

        The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

        Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

        For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

        As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

Testing: Make sure the test_updateHand() tests pass. You will also want to test your implementation of updateHand with some reasonable inputs.

Test Case 1:
Function Call:

wordList = loadWords()
playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)

Output:

  Current Hand:  a c i h m m z
  Enter word, or a "." to indicate that you are finished: him
  "him" earned 24 points. Total: 24 points
 
  Current Hand:  a c m z
  Enter word, or a "." to indicate that you are finished: cam
  "cam" earned 21 points. Total: 45 points
 
  Current Hand:  z
  Enter word, or a "." to indicate that you are finished: .
  Goodbye! Total score: 45 points.    

Test Case 2:

Function Call:

wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)

Output:

  Current Hand:  a s t t w f o
  Enter word, or a "." to indicate that you are finished: tow
  "tow" earned 18 points. Total: 18 points
 
  Current Hand:  a s t f
  Enter word, or a "." to indicate that you are finished: tasf
  Invalid word, please try again.
 
  Current Hand:  a s t f
  Enter word, or a "." to indicate that you are finished: fast
  "fast" earned 28 points. Total: 46 points. 
 
  Run out of letters. Total score: 46 points.    

Test Case 3:
Function Call:

wordList = loadWords()
playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)

Output:

  Current Hand: a r e t i i n
  Enter word, or a "." to indicate that you are finished: inertia
  "inertia" earned 99 points. Total: 99 points

  Run out of letters. Total score: 99 points.

Additional Testing:
Be sure that, in addition to the listed tests, you test the same basic test conditions with varying values of n. n will never be smaller than the number of letters in the hand. 

Game output should look like:
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e

Hint:
Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in playHand - be sure that your code is modular and uses function calls to the playHand helper function!

You should also make calls to the dealHand helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.

Here is the above output, with the output from playHand obscured:


Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
<call to playHand> 

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e

Hopefully this hint makes the problem seem a bit more approachable.

Mutation:
Please note that our implementation of playHand DOES mutate the hand. Be sure you pass in a copy of the hand to this function when you call it.

If you're not sure what this means, please review the Python docs on dictionaries. Especially of interest is the 'copy' function.

Note on Run Time:
You may notice that things run a bit slowly when the computer plays. This is to be expected - the wordList has 83667 words, after all!

However, don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out.

Test Cases:
Some test cases to look at:

>>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)
appels
>>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
acta
>>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)
imamate
>>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList)
None

Some test cases to look at:
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)

Current Hand: 
a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 1100 points.

compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)

Current Hand: 
a a c b t
"acta" earned 24 points. Total: 24 points
Current Hand: 
b
Total score: 24 points.

compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)

Current Hand: 
a a e e i i m m n n t t
"immanent" earned 96 points. Total: 96 points
Current Hand: 
a e t i
"ait" earned 9 points. Total: 105 points
Current Hand: 
e
Total score: 105 points.

A Note on Run Time:
You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the compChooseWord function.

Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).

IMPORTANT:Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.

'''
