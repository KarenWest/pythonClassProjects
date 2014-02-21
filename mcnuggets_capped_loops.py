def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # LCM of the three is 180
    # can work with the remainder after dividing by 180
    newVariable = n
    if n > 180:
        newVariable = n%180
    numSix=0
    numNine=0
    numTwenty=0
    # max of numSix in 180 is 30
    # max of numNine is 20
    # max of numTwenty is 9
    for numSix in range(0,30):
        for numNine in range(0,20):
            for numTwenty in range(0,9):
                if (numSix*6+numNine*9+numTwenty*20)-newVariable == 0:
                    #print(str(numSix) + '*6+' + str(numNine) + '*9+' + str(numTwenty) + '*20= ' + str(numSix*6+numNine*9+numTwenty*20))
                    return True
    return False