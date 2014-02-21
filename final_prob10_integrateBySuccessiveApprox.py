'''
 Problem 10 : 10.0 points

A standard problem in mathematics is to measure the area under a curve (or to
integrate the function defining the curve). A simple way to do this is to
approximate the area with a series of rectangles (whose areas are easy to
compute).

For example, given the curve on the left of the diagram below, we could
split the range into two parts, then fit a rectangle whose height is the
value of the function at the start of the range to the left half, and fit a
rectangle whose height is the value of the function at the middle of the
range to the right half (see the 2nd image in the diagram). If we decide this
is not a sufficiently accurate estimate of the area under the curve, we could
split each part in half and repeat the process (see the 3rd image in the
diagram in documentation file).
'''
def integrate(f, a, b, parts):
    '''
    Here is a function that estimates the area under a curve defined by a
    function f, between points a and b:
    '''
    spacing = float(b-a)/parts
    current = 0
    for i in range(parts):
        current += spacing * f(a+ i*spacing)
    return current
'''
Your job is to fill in the following function definition.
To do so, use successive refinement to find the area under a curve to within
a specific level of accuracy. Complete the function definition so that the
procedure successiveApproxIntegrate returns an estimate of the area under the
curve f. Your final estimate, using N parts, must be less than epsilon away
from the estimate using N/2 parts.

Note: For this problem, no libraries have been imported for you; you should
not need to import any libraries for this problem.
'''
def successiveApproxIntegrate(f, a, b, epsilon):
    # Your Code Here
    # bisection search for integration

    x = 5
    epsilon = 0.01
    numGuesses = 0
    low = x #for num parts
    high = 100
    ans = (high + low)/2.0
    keepVaryingIntegralParts = True
    while (keepVaryingIntegralParts == True):
        func_ans = integrate(f,a,b,ans)
        if ((func_ans - x) < epsilon):
            keepVaryingIntegralParts = False
        else:
            print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
            numGuesses += 1
            if  ans < x:
                low = ans
            else:
                high = ans
            ans = (high + low)/2.0
        print('numGuesses = ' + str(numGuesses))
        print(str(func_ans) + ' is close to the integral of f(a,b) in num parts ' + str(ans))
    return func_ans
'''
Test case output posted for my code after due date--correct solutions other file:
 INCORRECT Hide output
successiveApproxIntegrate(a,0,5,0.01)

def a(x): return x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    12.493896484375

successiveApproxIntegrate(a,-5,5,0.01)

def a(x): return x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    -0.006103515625

successiveApproxIntegrate(b,0,5,0.01)

def b(x): return 100 - x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    487.506103515625

successiveApproxIntegrate(b,0,200,5)

def b(x): return 100 - x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    4.8828125

successiveApproxIntegrate(c,-5,5,0.01)

def c(x): return x**2

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    83.33587646484375

successiveApproxIntegrate(d,-5,5,0.01)

def d(x): return 0.25*x**4-3.25*x**2+5

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    91.66813691381304

successiveApproxIntegrate(e,0,5,1)

def e(x): return 5**x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    1940.097122509662

successiveApproxIntegrate(f,0,5,1)

def f(x): return -5**x

Your output:

    Traceback (most recent call last):
      File "submission.py", line 19, in successiveApproxIntegrate
        func_ans = integrate(f,a,b,ans)
      File "submission.py", line 6, in integrate
        for i in range(parts):
    TypeError: range() integer end argument expected, got float.

Correct output:

    -1940.097122509662
'''
