import math
import random
import pylab

# Problem 7-1
def sampleQuizzes():
    numTrials = 10000
    yes = 0
    for i in range(numTrials):
        m1 = random.uniform(50, 80)
        m2 = random.uniform(60, 90)
        f = random.uniform(55, 95)
        score = 0.25 * m1 + 0.25 * m2 + 0.5 * f
        if 70 <= score <= 75:
            yes += 1
    return float(yes) / numTrials

#print(sampleQuizzes())


# Problem 7-2
def generateScores(numTrials):
    scores = []
    for i in range(numTrials):
        m1 = random.uniform(50, 80)
        m2 = random.uniform(60, 90)
        f = random.uniform(55, 95)
        score = 0.25 * m1 + 0.25 * m2 + 0.5 * f
        scores.append(score)
    mean = 0
    for score in scores:
        mean += score
    scores.append(float(mean) / numTrials)
    for score in scores:
        print score
    return scores

def plotQuizzes():
    scores = generateScores(10)
    pylab.figure()
    pylab.hist(scores, bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

plotQuizzes()
