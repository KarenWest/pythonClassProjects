'''
Problem 3 from Midterm - Karen West - due 11/4/12

Write a simple procedure, myLog(x, b), that computes the logarithm of a number
x relative to a base b.  For example, if x = 16 and b = 2, then result is
4 - because 2**4 = 16.  If x = 15 and b = 3, then the result is 2 - 3**2 is
the largest power of 3 less than 15.

In other words, myLog should return the largest power of b such that b to that
power is still less than x.

Do NOT use Python's log functions.  Instead, please use an iterative or
recursive solution to this problem that uses simple arithmetic operators
and conditional testing.

Note: Thoroughly test your code -- test cases not provided for a mid term
as they are for programming assignments.

'''

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''

    #iterative solution:
    
    logx_baseb = 0
    # Note: x = positive integer, so it's greater than zero
    i = 0
    findingLog = False
    while (findingLog == False):
        num = b**i
        if (num == x):
            findingLog = True
            logx_baseb = i
        elif (num > x):
            findingLog = True
        else:
            logx_baseb = i
            print "at i = " + str(i) + " x = " + str(x) + " b = base of log = " + str(b) + " log = " + str(logx_baseb)
            i += 1
    print "at end x = " + str(x) + " b = base of log = " + str(b) + " log = " + str(logx_baseb)
    return logx_baseb


#test myLog():
myLog(16, 2)
myLog(15, 3)

'''
Test case output (my solution correct):
 CORRECT Hide output
myLog(27, 3)

Output:

    3

myLog(26, 3)

Output:

    2

myLog(28, 3)

Output:

    3

myLog(4, 16)

Output:

    0

myLog(13, 13)

Output:

    1

myLog(50, 2)

Output:

    5

myLog(99, 5)

Output:

    2

myLog(66, 5)

Output:

    2
'''
