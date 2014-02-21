import random
def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    results=[]
    def go(conts,grades):
        '''conts int num of continents, grades int min top grades'''
        cont=[0 for x in xrange(conts)]        
        for x in xrange(100):
            c=random.randrange(conts)
            cont[c]+=1
        if any(continent>=grades for continent in cont):
            return 1
        else:
            return 0
        
    for num in xrange(numTrials):
        results.append(go(4,30))
    return sum(results)/float(len(results))

    
