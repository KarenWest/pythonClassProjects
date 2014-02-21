## Problem 7 [python]
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    def checkNuggets(a,b,c,n):
        res = (6*a + 9*b + 20*c)
        if res == n:
            return {'a':a, 'b':b, 'c':c}
        elif res < n:
            res2 = checkNuggets(a+1,b,c,n)
            if res2 == None:
                res2 = checkNuggets(a,b+1,c,n)
            if res2 == None:
                res2 = checkNuggets(a,b,c+1,n)
            return res2
        else:
            return None

    if n <=0:
        return False

    result = checkNuggets(0,0,0,n)
    #print result
    return False if result == None else True



def assertThat(tst, result):
    print "Testing", tst, ":",
    try:
        res = eval(tst)
    except AssertionError:
        res = "error"
    print "Success" if res == result else ("Expected:", result, "got", res)

assertThat("McNuggets(0)", False)
assertThat("McNuggets(15)", True)
assertThat("McNuggets(16)", False)
assertThat("McNuggets(37)", False)
assertThat("McNuggets(38)", True)
assertThat("McNuggets(39)", True)
assertThat("McNuggets(40)", True)
assertThat("McNuggets(41)", True)
assertThat("McNuggets(42)", True)
assertThat("McNuggets(43)", False)
assertThat("McNuggets(44)", True)
assertThat("McNuggets(45)", True)
assertThat("McNuggets(46)", True)
assertThat("McNuggets(47)", True)
assertThat("McNuggets(48)", True)
assertThat("McNuggets(49)", True)
assertThat("McNuggets(50)", True)
assertThat("McNuggets(51)", True)
assertThat("McNuggets(52)", True)
assertThat("McNuggets(53)", True)
assertThat("McNuggets(54)", True)
assertThat("McNuggets(55)", True)
assertThat("McNuggets(56)", True)
assertThat("McNuggets(57)", True)
assertThat("McNuggets(58)", True)
assertThat("McNuggets(59)", True)
assertThat("McNuggets(5000)", True)
assertThat("McNuggets(5001)", True)
assertThat("McNuggets(-1)", False)
