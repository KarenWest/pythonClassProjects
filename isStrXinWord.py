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

#Test cases
print x_ian('eric', 'algebraic')
print x_ian('john', 'mahjong')
print x_ian('alvin', 'palavering')
print x_ian('sarina', 'czarina')
