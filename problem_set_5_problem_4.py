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
    if x == '':
        return True
    index = word.find(x[0])
    if index == -1:
        return False
    return x_ian(x[1:], word[index + 1:])
#    --------
    if x == '':
        return True
    index = word.rfind(x[-1])
    if index == -1:
        return False
    return x_ian(x[:-1], word[:index])
#    --------
    if x == '':
        return True
    if word == '':
        return False
    if x[0] == word[0]:
        return x_ian(x[1:], word[1:])
    else:
        return x_ian(x, word[1:])