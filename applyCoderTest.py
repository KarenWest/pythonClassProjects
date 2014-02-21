from buildCoderTest import *
import string

#" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"" --all but the numerics below
PUNCTUATION_NUMERICS_SPACE = " " + string.punctuation + "0123456789"

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedText = ""
    coderCopy = coder.copy()

    for letter in text:
        if letter not in PUNCTUATION_NUMERICS_SPACE:
            for ltrKey, ltrVal in coderCopy.items():
                if ltrKey == letter:
                    encodedText += ltrVal
        else:
            encodedText += letter
    #print PUNCTUATION_NUMERICS_SPACE
    #print " !@#$%^&*()-_+={}[]|\\:;'<>?,./\""
    return encodedText

#print applyCoder("Hello, world!", buildCoder(3))
#print applyCoder("Khoor, zruog!", buildCoder(23))
#print applyCoder("Hello, world 12345!", buildCoder(3))
