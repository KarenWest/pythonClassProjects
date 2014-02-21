def findOrder(xVals, yVals, accuracy = 1.0e-1):
    yVals = pylab.array(yVals)
    xVals = pylab.array(xVals)
    counter = 0
    temp = []
    
    while True:
        try:
            temp = pylab.polyfit(xVals, yVals, counter, full = True)
            if abs(temp[1]) <= accuracy:
                return temp[0]
        finally:
            counter += 1