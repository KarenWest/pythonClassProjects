import string

class Person(object):
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

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
            return Person.__lt__(self, other)
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

class Subject(object):
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
    def allStudents(self):
        studentNum = 0
        sortStudents = []
        numStudents = len(self.students)
        sortStudents = sorted(self.students)
        aStudent = sortStudents[studentNum]
        while (studentNum < numStudents):
            yield (aStudent.__str__())
            studentNum += 1
            if (studentNum < numStudents):
                aStudent = sortStudents[studentNum]
            
    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'

p1 = edXPerson('Fred Flintstone')
p2 = UniversityStudent('Wilma Flintstone')
p3 = Student('Betty Rubble')
p4 = SelfLearner('Barney Rubble')
p5 = SelfLearner('Dino')
p = Person('Eric Grimson')
pythonClass = Subject()
pythonClass.addStudent(p1)
pythonClass.addStudent(p2)
pythonClass.addStudent(p3)
pythonClass.addStudent(p4)
pythonClass.addStudent(p5)
for s in pythonClass.allStudents():
    print s
'''
edXPerson test cases (my solution correct:)
 CORRECT Hide output
Test: 1

Output:

    b = sm.SelfLearner("Beto")
    Beto
    a = sm.SelfLearner('Alvin')
    Alvin
    a < b? True
    b < a? False

Test: 2

Output:

    b = sm.Student("Beto")
    Beto
    a = sm.Student('Alvin')
    Alvin
    a < b? False
    b < a? True
'''
'''
Test cases output for Subject() -- my solution correct:
 CORRECT Hide output
Test: 1

p1 = edXPerson('Fred Flintstone') p2 = UniversityStudent('Wilma Flintstone') p3 = Student('Betty Rubble') p4 = SelfLearner('Barney Rubble') p5 = SelfLearner('Dino')

Output:

    Subject with 0 students.
    Adding p1 through p5
    Subject with 5 students.
    Going through the students using allStudents generator
    Barney Rubble
    Dino
    Fred Flintstone
    Wilma Flintstone
    Betty Rubble
    Successfully stopped.

Test: 2

p1 = Student('A') p2 = SelfLearner('E') p3 = edXPerson('H') p4 = UniversityStudent('D') p5 = SelfLearner('B') p6 = UniversityStudent('G') p7 = Student('F') p8 = edXPerson('C')

Output:

    Subject with 0 students.
    Adding p1 through p8
    Subject with 8 students.
    Going through the students using allStudents generator
    B
    E
    A
    H
    D
    G
    F
    C
    Successfully stopped.
'''
