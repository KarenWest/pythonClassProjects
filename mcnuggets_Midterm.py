'''
McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets. Thus,
it is possible, for example, to buy exactly 15 McNuggets (with one package of
6 and a second package of 9), but it is not possible to buy exactly 16
McNuggets, since no non- negative integer combination of 6's, 9's and 20's
add up to 16. To determine if it is possible to buy exactly n McNuggets, one
has to find non-negative integer values of a, b, and c such that

6a+9b+20c=n

Write a function, called McNuggets that takes one argument, n, and returns
True if it is possible to buy a combination of 6, 9 and 20 pack units such
that the total number of McNuggets equals n, and otherwise returns False.
Hint: use a guess and check approach.
'''
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    foundCombo = False
    mcnugget_6pack_combo = False
    mcnugget_9pack_combo = False
    mcnugget_20pack_combo = False
    mcnugget_6_9_pack_combo = False
    mcnugget_6_20_pack_combo = False
    mcnugget_9_20_pack_combo = False
    mcnugget_6_9_20_pack_combo = False
    def willCombosWork(a,b,c, whichComboToVary):    
        mcnugget_6pack = 0
        mcnugget_6_9_packs = 0
        mcnugget_6_9_20_packs = 0
        mcnugget_6_9_20_combo = False
        mcnugget_9pack = 0
        mcnugget_20pack = 0
        mcnugget_6_9_packs = 0
        mcnugget_6_20_packs = 0
        mcnugget_9_20_packs = 0
        mcnugget_6_9_20_packs = 0
        mcnugget_combo_found = False
        keepLooping = True
        
        while (a <= 6) and (b <= 9) and (c <= 20) and (keepLooping == True):
            mcnugget_6pack = 6 * a
            mcnugget_9pack = 9 * b
            mcnugget_20pack = 20 * c
            mcnugget_6_9_packs = (6 * a) + (9 * b)
            mcnugget_6_20_packs = (6 * a) + (20 * c)
            mcnugget_9_20_packs = (9 * b) + (20 * c)
            mcnugget_6_9_20_packs = (6 * a) + (9 * b) + (20 * c)
            if (mcnugget_6pack == n) or (mcnugget_9pack == n) or (mcnugget_20pack == n) or (mcnugget_6_9_packs == n) or (mcnugget_6_20_packs == n) or (mcnugget_9_20_packs == n) or (mcnugget_6_9_20_packs == n):
                mcnugget_combo_found = True
                keepLooking = False
            elif (mcnugget_6_9_20_packs >= upper_limit_factorChk):
                print "exceeded upper limit factor check " + str(mcnugget_6_9_20_packs)
                keepLooping = False
            if ('a' in whichComboToVary) and (keepLooping == True):
                if (a >= 6) and ('b' not in whichComboToVary) and ('c' not in whichComboToVary):
                    keepLooping = False
                else:
                    a += 1
            if ('b' in whichComboToVary) and (keepLooping == True):
                if (b >= 9) and ('c' not in whichComboToVary):
                    keepLooping = False
                else:
                    b += 1
            if ('c' in whichComboToVary) and (keepLooping == True):
                if (c >= 20):
                    keepLooping = False
                else:
                    c += 1
        return mcnugget_combo_found
    
    upper_limit_factorChk = 20 * 10 * 6
    print "upper limit mcnugget combo check = " + str(upper_limit_factorChk)
    print "trying to find combo of mcnuggets = " + str(n)
    a = 1
    b = 0
    c = 0
    mcnugget_6pack_combo = willCombosWork(a,b,c, 'a')
    if (mcnugget_6pack_combo == True):
        print "6 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
        foundCombo = True
    if (foundCombo == False):
        a = 0
        b = 1
        c = 0
        mcnugget_9pack_combo = willCombosWork(a,b,c, 'b')
        if (mcnugget_9pack_combo == True):
            print "9 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
    if (foundCombo == False):
        a = 0
        b = 0
        c = 1
        mcnugget_20pack_combo = willCombosWork(a,b,c, 'c')
        if (mcnugget_20pack_combo == True):
            print "20 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
    if (foundCombo == False):
        a = 1
        b = 1
        c = 0
        mcnugget_6_9_pack_combo = willCombosWork(a,b,c, 'ab')
        if (mcnugget_6_9_pack_combo == True):
            print "6 and 9 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
    if (foundCombo == False):
        a = 1
        b = 0
        c = 1
        mcnugget_6_20_pack_combo = willCombosWork(a,b,c, 'ac')
        if (mcnugget_6_20_pack_combo == True):
            print "6 and 20 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
    if (foundCombo == False):
        a = 0
        b = 1
        c = 1
        mcnugget_9_20_pack_combo = willCombosWork(a,b,c, 'bc')
        if (mcnugget_9_20_pack_combo == True):
            print "9 and 20 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
    if (foundCombo == False):
        a = 1
        b = 1
        c = 2
        mcnugget_6_9_20_pack_combo = willCombosWork(a,b,c, 'abc')
        if (mcnugget_6_9_20_pack_combo == True):
            print "6 9 20 pack combo pack found to work for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            foundCombo = True
  
    if (foundCombo == False):
        print "Did not find mcnugget combo for n = " + str(n) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c)
    return (foundCombo)
            
McNuggets(15)
McNuggets(16)
'''
Test case output--see correct solutions other file:
 INCORRECT Hide output
McNuggets(236)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 236
    Did not find mcnugget combo for n = 236 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(146)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 146
    Did not find mcnugget combo for n = 146 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(17)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 17
    Did not find mcnugget combo for n = 17 a = 1 b = 1 c = 2
    False

Correct output:

    False

McNuggets(45)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 45
    9 pack combo pack found to work for n = 45 a = 0 b = 1 c = 0
    True

Correct output:

    True

McNuggets(133)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 133
    Did not find mcnugget combo for n = 133 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(28)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 28
    Did not find mcnugget combo for n = 28 a = 1 b = 1 c = 2
    False

Correct output:

    False

McNuggets(239)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 239
    Did not find mcnugget combo for n = 239 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(16)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 16
    Did not find mcnugget combo for n = 16 a = 1 b = 1 c = 2
    False

Correct output:

    False

McNuggets(32)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 32
    Did not find mcnugget combo for n = 32 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(62)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 62
    Did not find mcnugget combo for n = 62 a = 1 b = 1 c = 2
    False

Correct output:

    True

McNuggets(1)

Your output:

    upper limit mcnugget combo check = 1200
    trying to find combo of mcnuggets = 1
    Did not find mcnugget combo for n = 1 a = 1 b = 1 c = 2
    False

Correct output:

    False
'''
