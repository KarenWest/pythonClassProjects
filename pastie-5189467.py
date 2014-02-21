## Problem 3 [python]
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    assert(x > 0)
    assert(b >= 2)

    bestLog = 0
    while (b**(bestLog+1) <= x):
        bestLog += 1
    return bestLog

def assertThat(tst, result):
    print "Testing", tst, ":",
    try:
        res = eval(tst)
    except AssertionError:
        res = "error"
    print "Success" if res == result else ("Expected:", result, "got", res)

assertThat("myLog(16,2)", 4)
assertThat("myLog(15,3)", 2)
assertThat("myLog(0,3)", "error")
assertThat("myLog(1,2)", 0)
assertThat("myLog(1,1)", "error")
