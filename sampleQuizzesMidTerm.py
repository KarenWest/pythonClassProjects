import math
import random

def MidTerm1Grade():
    gradeRange = range(50,81)
    grade = random.choice(gradeRange)
    #print "MidTerm 1 grade " + str(grade)
    return grade
def MidTerm2Grade():
    gradeRange = range(60,91)
    grade = random.choice(gradeRange)
    #print "MidTerm 2 grade " + str(grade)
    return grade
def FinalExamGrade():
    gradeRange = range(55,96)
    grade = random.choice(gradeRange) 
    #print "Final Exam grade " + str(grade)
    return grade
def getTarget(goal):
    numTries = 0
    lenGradeRange = len(goal)
    lowGradeRange = float(goal[0])
    highGradeRange = float(goal[lenGradeRange - 1])
    while True:
        numTries += 1
        #print "num tries = " + str(numTries)
        midTerm1_grade = MidTerm1Grade()
        #print "midTerm1 grade " + str(midTerm1_grade)
        midTerm2_grade = MidTerm2Grade()
        #print "midTerm2 grade " + str(midTerm2_grade)
        finalExam_grade = FinalExamGrade()        
        #print "final exam grade " + str(finalExam_grade)
        result = midTerm1_grade * 0.25 + midTerm2_grade * 0.25 + finalExam_grade * 0.5
        #print "result grade average = " + str(result)
        if (result >= lowGradeRange) and (result <= highGradeRange):
            return numTries
def sampleQuizzes():
    # Your code here
    total = 0
    numTrials = 10000
    goal = range(70,76)
    #print goal[0]
    for i in range(numTrials):
        total += getTarget(goal)
        #print "total = " + str(total) + " trial num = " + str(i)
    avgNumTries = total / float(numTrials)
    #print "Probability = " + str(1.0/avgNumTries)
    print 'Probability = {0:.2f}'.format(1.0/avgNumTries)
    return (1.0/avgNumTries)

sampleQuizzes()
'''
Test case output--my solution correct:
 CORRECT Hide output
Test: sampleQuizzes()

Output:

    0.25489396411092985
'''
