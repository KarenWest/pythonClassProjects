def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    students = 1000
    top = 100
    nat = 4
    threshold = 30
    total = 0.0
    for t in range(numTrials):
        grades = []
        for s in range(students):
            grades.append((random.random(), s % nat))
        grades = sorted(grades, key=lambda x:x[0])
        count = nat * [0]
        for s in grades[:top]:
            count[s[1]] += 1
        if any([c >= threshold for c in count]):
            total += 1
    return total / numTrials