# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#

#	>>> print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
#	180339.9
#	>>> print evaluatePoly([2, 0, 7, 1], 4)
#	178.0
#	>>> print evaluatePoly([-12], 3.7)
#	-12.0

# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    value = poly[0]
    lenPoly = len(poly)
    #print 'length list polynomial = ' + str(lenPoly)
    xpower = 0.0
    #print 'poly in string is {0:.2f}'.format(poly[0])
    #print 'at power coefficient = ' + str(0)
    #print 'eval at x = {0:.2f}'.format(x)

    if (lenPoly == 1):
        return value
    else:
        index = 1
        while (index < lenPoly):
            xpower = x**index
            value += poly[index] * xpower
            #print 'poly in string is {0:.2f}'.format(poly[index])
            #print 'value of poly {0:.2f}'.format(value)
            #print 'at power coefficient = ' + str(index)
            #print 'eval at xpower = {0:.2f}'.format(xpower)
            index += 1
    
    print 'evaluate Poly = {0:.20f}'.format(value)
    return float(value)

# Problem 2: Derivatives
#	>>> print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
#	[0.0, 35.0, 9.0, 4.0]
#	>>> print computeDeriv([6, 1, 3, 0])
#	[1.0, 6.0, 0.0]
#	>>> print computeDeriv([20])
#	[0.0]

def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length > 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    derivPoly = [0.0] #derivative of constant = 0.0 at power coeff zero
    lenPoly = len(poly)
    if (lenPoly == 1):
        #print "derivative is zero for length 1 polynomial, a constant"
        return derivPoly # derivative of one number in the zero position in list is
                         # a constant so the derivative is zero
    else: # there are higher order terms in the polynomial so not zero for
          # derivative
        derivPoly = [float(poly[1])]
        index = 2
        while (index < lenPoly):
            derivPoly.append(float(index * poly[index]))
            print 'derivPoly in string is {0:.2f}'.format(derivPoly[index-1])
            index += 1
        return derivPoly
        
# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    i = 1
    rootList = []
    xGuessList = [x_0]
    newXguess = 0.0
    value = abs(evaluatePoly(poly, x_0))
    if (value <= epsilon): #root value is close enough to be a root, since
                           #when x_0 evaluated in polynomial, root value<=epsilon
        rootList.append(value)
        rootList.append(1)
        return rootList
    else: # root value not good enough, so need better guess using Newton-Raphson
        maxGuesses = 7
        derivPoly = computeDeriv(poly)
        while (i <= maxGuesses):
           numeratorFuncEval = abs(evaluatePoly(poly, xGuessList[i-1]))
           denominatorFuncEval = abs(evaluatePoly(derivPoly, xGuessList[i-1]))
           if (denominatorFuncEval == 0): #cannot compute derivative
               i = maxGuesses #done best we can then
           else:
               newXguess = xGuessList[i-1] - numeratorFuncEval / denominatorFuncEval
               xGuessList.append(newXguess)
               value = abs(evaluatePoly(poly, newXguess))
               print 'value = {0:.10f}'.format(value)
               print 'newXguess = {0:.2f}'.format(newXguess)
               if (value <= epsilon):
                   rootList.append(value)
                   rootList.append(i+1)
                   return rootList
           i += 1
           
#Test Code
#poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
#x_0 = 0.1
#epsilon = .0001
#print computeRoot(poly, x_0, epsilon)
#	>>> print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
#	[0.806790753796352, 7]
#	>>> print computeRoot([1, 9, 8], -3, .01)
#	[-1.0000079170005467, 5]
#	>>> print computeRoot([1, -1, 1, -1], 2, .001)
#	[1.0002210630197605, 4]
#test cases from submission:
'''
Test 1

Function call: computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1, 0.0001)

Your output:

    value = 236.7551507741
    newXguess = -3.58
    value = 590.0122619169
    newXguess = -4.80
    value = 1475.9680591347
    newXguess = -6.26
    value = 3670.2751942593
    newXguess = -8.00
    value = 9070.3959993820
    newXguess = -10.10
    value = 22315.9207435314
    newXguess = -12.65
    value = 54744.6425849246
    newXguess = -15.79
    None

Correct output:

    [0.806790753796352, 7]

Test 2

Function call: computeRoot([1, 9, 8], -3, 0.01)

Your output:

    value = 103.1295200526
    newXguess = -4.18
    value = 231.6642083954
    newXguess = -5.96
    value = 520.8641700820
    newXguess = -8.64
    value = 1171.5626922879
    newXguess = -12.67
    value = 2635.6337448363
    newXguess = -18.72
    value = 5929.7933356589
    newXguess = -27.79
    value = 13341.6522915607
    newXguess = -41.40
    None

Correct output:

    [-1.0000079170005467, 5]

Test 3

Function call: computeRoot([1, -1, 1, -1], 2, 0.001)

Your output:

    value = 1.3717421125
    newXguess = 1.44
    value = 0.2974662905
    newXguess = 1.13
    value = 0.0304120640
    newXguess = 1.01
    value = 0.0004422238
    newXguess = 1.00
    [0.00044222378804148477, 5]

Correct output:

    [1.0002210630197605, 4]

Test 4

Function call: computeRoot([1, 2, 3, 4.3, -5], 0.3, 0.0001)

Your output:

    value = 0.7649604882
    newXguess = -0.14
    value = 1.2104905279
    newXguess = -0.66
    value = 2.7645860293
    newXguess = -0.79
    value = 6.5203426626
    newXguess = -0.97
    value = 15.6592353718
    newXguess = -1.22
    value = 37.9149683819
    newXguess = -1.53
    value = 92.1188562062
    newXguess = -1.93
    None

Correct output:

    [-0.47771869826311336, 6]

Test 5

Function call: computeRoot([-8, 2, 1], 20, 0.0001)

Your output:

    value = 105.7959183673
    newXguess = 9.71
    value = 24.3753795918
    newXguess = 4.78
    value = 4.4505795703
    newXguess = 2.67
    value = 0.3681562272
    newXguess = 2.06
    value = 0.0036170140
    newXguess = 2.00
    value = 0.0000003633
    newXguess = 2.00
    [3.6326484043058827e-07, 7]

Correct output:

    [2.0000000605441395, 6]

Test 6

Function call: computeRoot([-8, 2, 1], 2, 0.0001)

Your output:

    [0.0, 1]

Correct output:

    [2, 0]

Test 7

Function call: computeRoot([-8, 2, 1], -20, 0.0001)

Your output:

    value = 789.8060941828
    newXguess = -29.26
    value = 1774.8390622437
    newXguess = -43.24
    value = 3991.1492419694
    newXguess = -64.25
    value = 8977.8408567422
    newXguess = -95.80
    value = 20197.8941809645
    newXguess = -143.15
    value = 45443.0129093034
    newXguess = -214.19
    value = 102244.5294914575
    newXguess = -320.77
    None

Correct output:

    [-4.00000000844848, 6]

Test 8

Function call: computeRoot([-8, 2, 1], -4, 0.0001)

Your output:

    [0.0, 1]

Correct output:

    [-4, 0]

Test 9

Function call: computeRoot([4, 56, 0, 28, 0, 14, 0, 1], 1, 0.0001)

Your output:

    value = 38.0503069232
    newXguess = 0.53
    value = 8.2631185878
    newXguess = 0.08
    value = 0.0490770014
    newXguess = -0.07
    value = 0.0000045292
    newXguess = -0.07
    [4.5292402474410125e-06, 5]

Correct output:

    [-0.07124736072967754, 4]
'''
print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)

