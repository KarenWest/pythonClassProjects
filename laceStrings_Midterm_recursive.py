'''
Problem 5 - Midterm - due 11/4/12

Suppose you are given 2 strings, s1 and s2.  You would like to "lace" these
strings together, by successively alternating elements of each string
(starting with the first character of s1).  If one string is longer than the
other, then the remaining elements of the longer string should simply be
added at the end of the new string.  For example, if we lace 'abcd' and 'efgi',
we would get the new string: 'aebfcgdhi'.

Write a recursive procedue, called laceStringsRecur(s1, s2) that does this.
Your procedure should not use any explicit loop mechanism, such as a "for" or
"while" loop.  Insert code in template given.  Insert a single line of code
in each indicated place.  Otherwise if you write more than 1 line of code,
it will not be correct.

Note: Thoroughly test your code!

'''

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1.  If strings are not of same length, then the
    extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            print "s1 was shorter than or equal to s2 " + out + s2
            return (out + s2)
        if s2 == '':
            print "s2 was shorter than s1 " + out + s1
            return (out + s1)
        else:
            #recurse with modified args??-- s1[taking off first char],
            #s2[taking off first char] and out[adding first char from s1 & s2]
            #print "recursing"
            helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2 [0])
    #note - this next line goes with laceStringsRecur(), not helpLaceStrings()
    print "starting the recursion - s1 = " + s1 + " s2 = " + s2 
    return helpLaceStrings(s1, s2, '')
'''
Test cases output--correct solution in another file:
 INCORRECT Hide output
laceStringsRecur('aaaaaa', 'zzzzzz')

Your output:

    None

Correct output:

    'azazazazazaz'

laceStringsRecur('', '')

Output:

    ''

laceStringsRecur('edr', 'rkqwtpjoic')

Your output:

    None

Correct output:

    'erdkrqwtpjoic'

laceStringsRecur('yluaerbndcv', 'ajlc')

Your output:

    None

Correct output:

    'yaljulacerbndcv'

laceStringsRecur('avsrqxt', 'kthnazdu')

Your output:

    None

Correct output:

    'akvtshrnqaxztdu'

laceStringsRecur('hkzgqcr', 'ughixske')

Your output:

    None

Correct output:

    'hukgzhgiqxcsrke'
'''

'''
iterative version:
    addToEndStr = ""
    diff = 0
    lenS1 = len(s1)
    lenS2 = len(s2)
    #laceList = [] #easier to put in mutable structure then put back in str
    if (lenS1 < lenS2):
        upperIndex = lenS1
        diff = lenS2 - lenS1
        addToEndStr = s2[(lenS2 - diff) :]
    elif (lenS2 < lenS1):
        upperIndex = lenS2
        diff = lenS1 - lenS2
        addToEndStr = s1[(lenS1 - diff) :]
    else:
        upperIndex = lenS1
    if (diff > 0):
        print "diff between s1 and s2 lenths = " + str(diff) + " add to end str = " + addToEndStr
    i = 0
    lacedStr = ""
    oddCnt = 0
    evenCnt = 0
    #guessedWordStr = ''.join(lettersGuessed) #puts list of chars in str
    while (i < (upperIndex * 2)):
        if (i%2 == 0): #i = 0, 2, 4, 6....upperIndex-1 (if even)
            lacedStr += s1[oddCnt]
            print "even i = " + str(i) + " lacedStr = " + lacedStr
            oddCnt += 1
        else: # i = 1, 3, 5, 7...upperIndex-1 (if odd)
            lacedStr += s2[evenCnt]
            print "odd i = " + str(i) + " lacedStr = " + lacedStr
            evenCnt += 1
        i += 1
    if (lenS1 != lenS2):
        lacedStr += addToEndStr
    print "s1 = " + s1 + " s2 = " + s2 + " interlaced str = " + lacedStr
    return lacedStr
'''
#test code
laceStringsRecur("Sophie", "West")
laceStringsRecur("Peter", "West")
laceStringsRecur("Richard", "West")
laceStringsRecur("Rich", "West")
laceStringsRecur("Karen", "West")
laceStringsRecur("Mom", "West")
laceStringsRecur("Dad", "West")
