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
    print 'length list polynomial = ' + str(lenPoly)
    xpower = 0.0
    print 'poly in string is {0:.2f}'.format(poly[0])
    print 'at power coefficient = ' + str(0)
    print 'eval at x = {0:.2f}'.format(x)

    if (lenPoly == 1):
        return value
    else:
        index = 1
        while (index < lenPoly):
            xpower = x**index
            value += poly[index] * xpower
            print 'poly in string is {0:.2f}'.format(poly[index])
            print 'value of poly {0:.2f}'.format(value)
            print 'at power coefficient = ' + str(index)
            print 'eval at xpower = {0:.2f}'.format(xpower)
            index += 1
    
    print 'evaluate Poly = {0:.20f}'.format(value)
    return float(value)

#print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
#print evaluatePoly([2, 0, 7, 1], 4)
print evaluatePoly([-12], 3.7)
