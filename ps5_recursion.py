# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]


#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    else:
        letWordLoc = word.find(x[0])
        if (letWordLoc != -1):
            return x_ian(x[1:], word[(letWordLoc + 1):])
        else:
            return False


#
# Problem 5: Typewriter
#
'''
    Write helper functions as appropriate. If you wish to use insertNewlines
    as a wrapper function that makes an appropriate call to a recursive
    function, please name your recursive helper function insertNewlinesRec so
    it can be properly graded by our automatic grader.
    
    lineLength is not the maximum number of characters in the line. It is the
    length after which the next word should be wrapped to the next line.
    
    Make sure that if a space occurs on the index of the desired line length,
    the next word is wrapped to the next line.
'''    
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if (lineLength >= len(text)):
        return text
    else: #lineLength where to insert is less than length of rest of text
        if (len(text) == (lineLength + 1)) or (len(text) == (lineLength + 2)) or (len(text) == (lineLength + 3)):
            return text
        elif (len(text) < (2*lineLength)):
            textLineLengthIndex = text.find(" ", lineLength)
            if (textLineLengthIndex != -1):
                textLineLength = text[0:textLineLengthIndex]
                textRestOfLine = text[(textLineLengthIndex + 1):]
                textLineLength += "\n"
                return textLineLength + textRestOfLine
            else:
                return text
        textLineLength = text[0:lineLength]
        textRestOfLine = text[lineLength:]
        #print textLineLength
        #print textRestOfLine
        if (textLineLength[-1] == " "): #last char is a space in line
            textLineLength += "\n"
        else: #in the middle of a word -- finish this word first before \n
            textLineLengthIndex = text.find(" ", lineLength)
            textLineLength = text[0:textLineLengthIndex]
            textRestOfLine = text[(textLineLengthIndex + 1):]
            textLineLength += "\n"
        return textLineLength + insertNewlines(textRestOfLine, lineLength)
