def ProbOfRollOneOnDie(n):
    if (n == 1):
        prob = float(1/6)
    else:
        probNoOne = float((5/6) * (n - 1))
        prob = float(probNoOne * (1/6))
    print "prob = " + str(prob)
    return prob

def probTest(limit):
    numRolls = 1
    goalMet = False
    while (goalMet == False):
        prob = ProbOfRollOneOnDie(numRolls)
        if (prob < limit):
            print "num rolls to meet limit " + str(numRolls)
            goalMet = True
        else:
            numRolls += 1
    return numRolls
probTest(0.1)
'''
Test case output -- see other file for correct solutions:
 INCORRECT Hide output
probTest(0.5)

Output:

    1

probTest(0.15)

Your output:

    1

Correct output:

    2

probTest(0.12)

Your output:

    1

Correct output:

    3

probTest(0.11)

Your output:

    1

Correct output:

    4

probTest(0.1)

Your output:

    1

Correct output:

    4

probTest(0.05)

Your output:

    1

Correct output:

    8

probTest(0.01)

Your output:

    1

Correct output:

    17

probTest(0.005)

Your output:

    1

Correct output:

    21

probTest(0.001)

Your output:

    1

Correct output:

    30

probTest(0.0001)

Your output:

    1

Correct output:

    42
'''
