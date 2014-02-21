def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
#    return aStr[::-1] # Wrong! Not recursive.
#    --------
    if len(aStr) <= 1:
        return aStr
    return reverseString(aStr[1:]) + aStr[0]
#    --------
    if len(aStr) <= 1:
        return aStr
    return  aStr[-1] + reverseString(aStr[:-1])
#    --------
    if len(aStr) <= 1:
        return aStr
    if len(aStr) == 2:                      #
        return aStr[1] + aStr[0]            # This is all
    if len(aStr) == 3:                      # redundant
        return aStr[2] + aStr[1] + aStr[0]  #
    return aStr[-1] + reverseString(aStr[1:-1]) + aStr[0]
#    --------
    if len(aStr) <= 1:
        return aStr
    half = len(aStr) / 2
    return reverseString(aStr[half:]) + reverseString(aStr[:half])
#    --------
    if len(aStr) <= 1:
        return aStr
    if len(aStr) % 2 == 0:
        return reverseString(aStr[1:]) + aStr[0]
    else:
        middle = len(aStr) / 2
        return (reverseString(aStr[middle + 1:]) + 
                aStr[middle] + 
                reverseString(aStr[:middle]))