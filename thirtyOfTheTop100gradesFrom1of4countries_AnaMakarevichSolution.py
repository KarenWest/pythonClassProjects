def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # Your Code Here
    anyReg = 0.0
    for trial in range(numTrials):
        regions = [0.0]*4 #four different regions
        for i in range(100): #range - all top grades
            regions[random.choice([0, 1, 2, 3])] += 1
        if max(regions) >= 30:
            anyReg += 1
        regionprob = anyReg/numTrials
    return regionprob