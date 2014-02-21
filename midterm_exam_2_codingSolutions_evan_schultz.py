#print(10 + 10 + 4 + 10 + 4 + 6 + 6 + 4 + 10 + 10 + 10 + 4 + 8) # 96 points

# Problem 3-2
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

#pylab.hist(xVals)
#pylab.hist(tVals)
#pylab.plot(xVals, yVals)
#pylab.plot(xVals, zVals)
#pylab.plot(sorted(xVals), yVals)
#pylab.plot(xVals, sorted(yVals))
#pylab.plot(sorted(xVals), sorted(yVals))
#pylab.show()


# Problem 4-1
class Person(object):
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

##class edXPerson(Person):
##    nextIdNum = 0
##    def __init__(self, name):
##        Person.__init__(self, name)
##        self.idNum = edXPerson.nextIdNum
##        edXPerson.nextIdNum += 1
##    def getIdNum(self):
##        return self.idNum
##    def __lt__(self, other):
##        return self.idNum < other.idNum
##    def isStudent(self):
##        return isinstance(self, Student)
## replaced this class with Problem 4-2 version!
class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        if self.idNum == other.idNum:
            return self.name < other.name
        else:
            return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)

class Student(edXPerson):
    pass

class UniversityStudent(Student):
    pass

class SelfLearner(Student):
    def __init__(self, name):
        Student.__init__(self, name)
        self.idNum = 0

p1 = edXPerson('Fred Flintstone')
p2 = UniversityStudent('Wilma Flintstone')
p3 = Student('Betty Rubble')
p4 = SelfLearner('Barney Rubble')
p5 = SelfLearner('Dino')
p = Person('Eric Grimson')

##print(p2 < p3)
##print(p2.getIdNum() < p3.getIdNum())
##print(p2.name < p3.name)
##print(p4 < p3)
##print(p4 < p5)
##print(p1.isStudent())
##print(p3.isStudent())
##print(p5.isStudent())
##print(p.isStudent())


# Problem 4-2
class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        if self.idNum == other.idNum:
            return self.name < other.name
        else:
            return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)


# Problem 4-3
class Subject(object):
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
    def allStudents(self):
        self.students.sort()
        for student in self.students:
            yield student
    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'

mySubject = Subject()
mySubject.addStudent(p1)
mySubject.addStudent(p2)
mySubject.addStudent(p3)
mySubject.addStudent(p4)
mySubject.addStudent(p5)

##for s in mySubject.allStudents():
##    print s


# Problem 5
a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
##try:
##    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
##    print a, b, c, d
##except:
##    print 'fell to here'


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
    return scores

def plotQuizzes():
    scores = generateScores(10000)
    pylab.figure()
    pylab.hist(scores, bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

##plotQuizzes()


# Problem 8-2
def probTest(limit):
    i = 1
    prob = 1.0 / 6
    while prob > limit:
        prob = float((5 ** i)) / (6 ** (i + 1))
        i += 1
    return i

##print(probTest(.5))
##print(probTest(.14))
##print(probTest(.12))
##print(probTest(.1))
##print(probTest(.018))