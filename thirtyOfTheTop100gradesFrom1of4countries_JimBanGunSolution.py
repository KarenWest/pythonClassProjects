def test(numTrials):

    if numTrials <= 0:
        raise ValueError
    
    def pick():
        students = []
        picked = []
        for i in range(250):
            students.append(1)
            students.append(2)
            students.append(3)
            students.append(4)
        for i in range(100):
            choice = random.choice(students)
            picked.append(choice)
            students.remove(choice)
        a = picked.count(1)
        b = picked.count(2)
        c = picked.count(3)
        d = picked.count(4)
        if a >= 30 or b >= 30 or c >= 30 or c >= 30:
            return 1
        else:
            return 0

    result = []
    for i in range(numTrials):
        result.append(pick())
    return float(sum(result))/numTrials