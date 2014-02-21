def findOrder(xVals, yVals, accuracy = 1.0e-1):
    degree = 0
    residual = accuracy + 1
    while residual > accuracy: #residual is less that accuracy
        candidates = pylab.polyfit(xVals, yVals, degree, full = True)
        coeffs = candidates[0]
        residual = candidates[1]
        degree += 1
    return coeffs