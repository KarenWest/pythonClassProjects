# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#
#Test cases for evaluatePoly function:
#>>>print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
#   180339.9
#>>> print evaluatePoly([2, 0, 7, 1], 4)
#   178.0
#>>> print evaluatePoly([-12], 3.7)
#   -12.0

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






#Test cases for computeDeriv function:
#	>>> print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
#	[0.0, 35.0, 9.0, 4.0]
#	>>> print computeDeriv([6, 1, 3, 0])
#	[1.0, 6.0, 0.0]
#	>>> print computeDeriv([20])
#	[0.0]
# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...



#Test cases for computeRoot function:
#	>>> print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
#	[0.806790753796352, 7]
#	>>> print computeRoot([1, 9, 8], -3, .01)
#	[-1.0000079170005467, 5]
#	>>> print computeRoot([1, -1, 1, -1], 2, .001)
#	[1.0002210630197605, 4]

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
