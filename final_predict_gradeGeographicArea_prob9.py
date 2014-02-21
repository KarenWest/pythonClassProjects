'''
Problem 9 : 10.0 points

1,000 students took an online course.  0.25 of them were from Africa, 0.25 from Europe,
0.25 from South America, and 0.25 from Asia. At the end of the course, the instructor
observed that of the top 100 grades, 30 belonged to students from a single geographical
area. He argued that since the expected number of students from each area in the top 100
was 25, this was unlikely to have happened by pure chance. Write a function that uses
simulation to compute and return an estimate of the probability of at least 30 of the
top 100 grades coming from a single geographical area purely by chance.

You may assume that random has already been imported. 
'''
import math
import random

def AfricanGrades(numStudents):
    #250 Africans/1000 total students
    gradeRange = range(0,101)
    gradesForStudents = []
    while (numStudents > 0):
        gradesForStudents.append(random.choice(gradeRange))
        numStudents -= 1
    #print "African grade " + str(grade)
    return gradesForStudents
def EuropeanGrades(numStudents):
    #250 European/1000 total students
    gradeRange = range(0,101)
    gradesForStudents = []
    while (numStudents > 0):
        gradesForStudents.append(random.choice(gradeRange))
        numStudents -= 1
    #print "European grade " + str(grade)
    return gradesForStudents
def SouthAmericanGrades(numStudents):
    #250 South American/1000 total students
    gradeRange = range(0,101)
    gradesForStudents = []
    while (numStudents > 0):
        gradesForStudents.append(random.choice(gradeRange))
        numStudents -= 1
    #print "South American grade " + str(grade)
    return gradesForStudents
def AsianGrades(numStudents):
    #250 Asian/1000 total students
    gradeRange = range(0,101)
    gradesForStudents = []
    while (numStudents > 0):
        gradesForStudents.append(random.choice(gradeRange))
        numStudents -= 1
    #print "Asian grade " + str(grade)
    return gradesForStudents
def getTarget(goal):
    numTries = 0
    AtLeast30Range = goal
    numStudents = 250 #250 from each of the 4 geographic areas, making 1000 total students
    while True:
        AfricansBool = False
        EuropeansBool = False
        SouthAmericansBool = False
        AsiansBool = False
        JustAfricans = False
        JustEuropeans = False
        JustSouthAmericans = False
        JustAsians = False
        gradesFor1000Students = []
        sortedGradesFor1000Students = []
        top100grades = []
        numAfricansInTop100Grades = 0
        numEuropeansInTop100Grades = 0
        numSouthAmericansInTop100Grades = 0
        numAsiansInTop100Grades = 0
        numTries += 1
        #print "num tries = " + str(numTries)
        Africans_grades = AfricanGrades(numStudents)
        #print "Africans grade " + str(Africans_grade)
        Europeans_grades = EuropeanGrades(numStudents)
        #print "Europeans grade " + str(Europeans_grade)
        SouthAmericans_grades = SouthAmericanGrades(numStudents)        
        #print "South Americans grade " + str(SouthAmericans_grade)
        Asians_grades = AsianGrades(numStudents)
        for grade in Africans_grades:
            gradesFor1000Students.append(grade)
        for grade in Europeans_grades:
            gradesFor1000Students.append(grade)
        for grade in SouthAmericans_grades:
            gradesFor1000Students.append(grade)
        for grade in Asians_grades:
            gradesFor1000Students.append(grade)
        sortedGradesFor1000Students = sorted(gradesFor1000Students)
        for i in range(100):
            top100grades.append(sortedGradesFor1000Students[i])
        for grade in Africans_grades:
            if grade in top100grades:
                numAfricansInTop100Grades += 1
        for grade in Europeans_grades:
            if grade in top100grades:
                numEuropeansInTop100Grades += 1
        for grade in SouthAmericans_grades:
            if grade in top100grades:
                numSouthAmericansInTop100Grades += 1
        for grade in Asians_grades:
            if grade in top100grades:
                numAsiansInTop100Grades += 1
        if (numAfricansInTop100Grades >= AtLeast30Range):
            AfricansBool = True
        if (numEuropeansInTop100Grades >= AtLeast30Range):
            EuropeansBool = True
        if (numSouthAmericansInTop100Grades >= AtLeast30Range):
            SouthAmericansBool = True
        if (numAsiansInTop100Grades >= AtLeast30Range):
            AsiansBool = True
        JustAfricans = (AfricansBool == True) and (EuropeansBool == False) and (SouthAmericansBool == False) and (AsiansBool == False)
        JustEuropeans = (AfricansBool == False) and (EuropeansBool == True) and (SouthAmericansBool == False) and (AsiansBool == False)
        JustSouthAmericans = (AfricansBool == False) and (EuropeansBool == False) and (SouthAmericansBool == True) and (AsiansBool == False)
        JustAsians = (AfricansBool == False) and (EuropeansBool == False) and (SouthAmericansBool == False) and (AsiansBool == True)
        
        result = JustAfricans or JustEuropeans or JustSouthAmericans or JustAsians
        #print "result grade average = " + str(result)
        if (result == True):
            return numTries
def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # Your code here
    total = 0
    goal = 30
    #print goal[0]
    for i in range(numTrials):
        total += getTarget(goal)
        #print "total = " + str(total) + " trial num = " + str(i)
    avgNumTries = total / float(numTrials)
    #print "Probability = " + str(1.0/avgNumTries)
    print 'Probability = {0:.2f}'.format(1.0/avgNumTries)
    return (1.0/avgNumTries)

test(10000)
'''
Test case output posted after due date--better solutions in other file--note
that when I ran this, my probability (before submission) was 0.58, very close
to what is here, but somehow off a bit.

 INCORRECT Hide output
test(95)

Your answer should be within 0.2 of the calculated probability of 0.5166.

Your output:

    Probability = 0.65
    0.6462585034013606

Correct output:

    0.5789473684210527

test(100)

Your answer should be within 0.2 of the calculated probability of 0.5166.

Your output:

    Probability = 0.63
    0.6289308176100629

Correct output:

    0.56
'''
