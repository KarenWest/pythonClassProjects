import math
import random
import pylab

def MidTerm1Grade():
    gradeRange = range(50,81)
    grade = random.choice(gradeRange)
    return grade
def MidTerm2Grade():
    gradeRange = range(60,91)
    grade = random.choice(gradeRange)
    return grade
def FinalExamGrade():
    gradeRange = range(55,96)
    grade = random.choice(gradeRange) 
    return grade
def getTarget():
    midTerm1_grade = MidTerm1Grade()
    midTerm2_grade = MidTerm2Grade()
    finalExam_grade = FinalExamGrade()        
    result = midTerm1_grade * 0.25 + midTerm2_grade * 0.25 + finalExam_grade * 0.5
    return result

def sampleQuizzes():
    # Your code here
    examAvg = 0
    quizScores = []
    numTrials = 10000
    for i in range(numTrials):
        examAvg = getTarget()
        quizScores.append(examAvg)
    return quizScores

def labelPlot(numTrials):
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    
def plotQuizzes():
    # Your code here
    quizScoreList = []
    numTrials = 10000
    #quizScores = generateScores(numTrials)---on midTerm
    #my own code to test it:
    quizScoreList = sampleQuizzes()
    pylab.hist(quizScoreList, bins=7)
    labelPlot(numTrials)
    pylab.show()

plotQuizzes()
