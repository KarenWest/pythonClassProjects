import pylab
import numpy

def findOrder(xVals, yVals, accuracy = 1.0e-1):
'''
We have created a set of data values that sample a function y(x). The sample points are stored
in two arrays: xVals and yVals. These represent measurements of a physical process that is
subject to noise so that if a is the i'th entry of xVals (i.e. a = xVals[i]) then yVals[i] is
an approximation of y(a).

Write a procedure called findOrder that finds the lowest order polynomial model that fits the
data to an accuracy of 1.0e-1, as measured by the residual error. findOrder should return the
array of coefficients provided by pylab.polyfit. Recall that pylab.polyfit takes as arguments an
array of x values, an array of y values, a degree of polynomial fit, and an optional argument full,
which, if True, will cause pylab.polyfit to return:

    an array of coefficients
    the residual of the fit
    Three additional parameters that should not concern you.

You may assume that the modules pylab and numpy are already imported into the environment. You
may use anything you wish from the numpy module, but only pylab.polyfit and pylab.array are
available from the pylab module.

numpy.polyfit(x, y, deg, rcond=None, full=False)

Parameters:

x : array_like, shape (M,)
x-coordinates of the M sample points (x[i], y[i]).

y : array_like, shape (M,) or (M, K)
y-coordinates of the sample points. Several data sets of sample points sharing the same x-coordinates
can be fitted at once by passing in a 2D-array that contains one dataset per column.

deg : int
Degree of the fitting polynomial

rcond : float, optional
Relative condition number of the fit. Singular values smaller than this relative to the largest singular
value will be ignored. The default value is len(x)*eps, where eps is the relative precision of the float
type, about 2e-16 in most cases.

full : bool, optional
Switch determining nature of return value. When it is False (the default) just the coefficients are
returned, when True diagnostic information from the singular value decomposition is also returned.

Returns:

p : ndarray, shape (M,) or (M, K)
Polynomial coefficients, highest power first. If y was 2-D, the coefficients for k-th data set are in p[:,k].

residuals, rank, singular_values, rcond : present only if full = True
Residuals of the least-squares fit, the effective rank of the scaled Vandermonde coefficient matrix, its singular
values, and the specified value of rcond. For more details, see linalg.lstsq.

'''
# Your Code Here
   #a = 3.0
   #b = 2.0
   #c = 1.0
   #yVals = []
   #xVals = range(-20, 20)
   #for x in xVals:
       #yVals.append(a*x**2 + b*x + c)
   #yVals = pylab.array(yVals)
   #xVals = 2*pylab.array(xVals)
   try:
       #pylab.polyfit(x,y,degree_of_polynomial)
       a, b, c, d = pylab.polyfit(xVals, yVals, 3)
       print a, b, c, d
   except:
       print 'unable to fit'
    
# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    count = 0
    result = 0.0
    for a in poly:
        result += a if count == 0 else a*x**count
        count += 1
    return result


# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    b = 0.0
    result = []
    for a in poly[1:]:
        b+=1.0
        result.append(a*b)
    if b == 0.0:
        result = [0.0]
    return result


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
    count = 0
    x = x_0
    while abs(evaluatePoly(poly, x)) >= epsilon:
        x = x - (evaluatePoly(poly, x) / evaluatePoly(computeDeriv(poly), x))
        count += 1

    return [x, count]
