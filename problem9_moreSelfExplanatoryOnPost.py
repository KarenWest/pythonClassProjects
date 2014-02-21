def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    morethanthirty = 0
    for _ in range(numTrials):
        # Will have an outer loop of numTrials
        # have Four 250 slot lists, each for the different areas.
        # Initalize them with random floats between 0 and 100 for grades, assuming the grade distribution is uniform?
        # 
        africa = [100*random.random() for _ in range(250)]
        europe = [100*random.random() for _ in range(250)]
        southamerica = [100*random.random() for _ in range(250)]
        asia = [100*random.random() for _ in range(250)]
        
        # Combine them into a large list
        # Sort that list
        # Take the top 100 grades
        # Find where those grades came from (I assume that floats will be unique, very low chance of collision with 1000 numbers)
        # If there is a section where more than 30 came from, return 1
        totalgrades = africa + europe + southamerica + asia
        totalgrades.sort()
        africacount = europecount = southamericacount = asiacount = 0
        for grade in totalgrades[-100:]:
            if grade in africa:
                africacount += 1
            if grade in europe:
                europecount += 1
            if grade in southamerica:
                southamericacount += 1
            if grade in asia:
                asiacount += 1
        if (africacount > 30)  or (europecount > 30) or (southamericacount > 30) or (asiacount > 30):
            morethanthirty += 1

#    print morethanthirty
#    print numTrials
    return float(morethanthirty)/float(numTrials)