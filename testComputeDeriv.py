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
        print "derivative is zero for length 1 polynomial, a constant"
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
    
#print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
#print computeDeriv([6, 1, 3, 0])
print computeDeriv([20])
