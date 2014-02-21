import string

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
    #can't do this way according to directions:
    #return aStr[::-1]
    '''also cannot do it with a helper function according to directions
    def helpReverseString(inStr, outStr):
        if inStr == '':
            print outStr
            return outStr
        else:
            lenStr = len(inStr)
            outStr += inStr[-1]
            helpReverseString(inStr[0:(lenStr-1)], outStr )
    return helpReverseString(aStr, '')
    '''
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]
    
print "reversing string: " + "abcdefg"
print reverseString('abcdefg')
