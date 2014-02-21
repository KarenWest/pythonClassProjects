def findOrder(xVals, yVals, accuracy = 1.0e-1):
    order = 0
    residual = [accuracy]
    coeficients = []
    while residual and residual[0] >= accuracy:
        coeficients, residual, _, _, _ = pylab.polyfit(xVals, yVals, order, full = True)
        order += 1
    return coeficients