
import string

LOWER_CASE_LETTERS = string.ascii_lowercase
UPPER_CASE_LETTERS = string.ascii_uppercase

#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dictForCipher = {}

    for letter in LOWER_CASE_LETTERS:
        i = LOWER_CASE_LETTERS.find(letter)
        j = i + shift
        if (j > 25):
            #wrap around
            wrapNum = j - 26
            j = wrapNum
        cipherLetter = LOWER_CASE_LETTERS[j]
        dictForCipher[letter] = dictForCipher.setdefault(letter, cipherLetter)
        #print "letter " + letter + " cipher letter " + cipherLetter + " shift was " + str(shift)

    for letter in UPPER_CASE_LETTERS:
        i = UPPER_CASE_LETTERS.find(letter)
        j = i + shift
        if (j > 25):
            #wrap around
            wrapNum = j - 26
            j = wrapNum
        cipherLetter = UPPER_CASE_LETTERS[j]
        dictForCipher[letter] = dictForCipher.setdefault(letter, cipherLetter)
        #print "letter " + letter + " cipher letter " + cipherLetter + " shift was " + str(shift)

    return(dictForCipher)

#buildCoder(3)
#buildCoder(9)
