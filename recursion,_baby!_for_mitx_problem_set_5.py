import decorators
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
    if len(aStr) < 2:
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
    return not x if not x or len(x) > len(word) else x_ian(x[(x[0] == word[0]):], word[1:])

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength, line=''):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    line: accumulator parameter for the current line
    returns: a string, with newline characters inserted appropriately. 
    """
    if not text or len(line) + len(text) <= lineLength:
        return line + text
    elif text[0] in tuple(" \n") and len(line) >= lineLength - 1:
        return line + '\n' + insertNewlines(text[1:], lineLength, '')
    else:
        return insertNewlines(text[1:], lineLength, line + text[0])