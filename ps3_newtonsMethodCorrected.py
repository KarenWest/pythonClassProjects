# Problem 3: Newton's Method

def computeRoot(poly, x_0, epsilon):

'''

Uses Newton's method to find and return a root of a polynomial function.

Returns a list containing the root and the number of iterations required

to get to the root.

poly: list of numbers, length >= 1.

Represents a polynomial function containing at least one real root.

The derivative of this polynomial function at x_0 is not 0.

x_0: float

epsilon: float > 0

returns: list [float, int]

'''

# If our polynomial at x_0 evaluates to a value close enough to 0

if abs(evaluatePoly(poly, x_0)) < epsilon:

# return root and '0' for number of iterations

return [x_0, 0]

# If polynomial at x_0 is not close enough to 0, make new guess for

# x_0. New guess 'x_0' should be of the form:

# x_0 = x_0 - ( f(x_0) / df(x_0) )

x_0 = x_0 - evaluatePoly(poly, x_0) / evaluatePoly(computeDeriv(poly), x_0)

# Recursive call

result = computeRoot(poly, x_0, epsilon)

# Increment counter, which is the 2nd int (index 1) in the list

result[1] += 1

return result
