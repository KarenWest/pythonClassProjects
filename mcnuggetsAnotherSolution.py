def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n%6 == 0 or n%9 == 0 or n%20 == 0: #if no remainder, it works
        return True
    if n < 6: #obvious
        return False
    if n > 6 and n%3 == 0: #any higher than 6, evenly divisible by 3 can be done with 6&9 combinations
        return True
    if (n-20) >= 6 and (n-20)%3 == 0: #if not divisible by 3, subtract a 20pc nugget & recheck
        return True
    if (n-20-20) >= 6 and (n-20-20)%3 == 0: #if still not divisible by 3, subtract 2 20pc nuggets & recheck
        return True
    else: #if a number (n), n-20, and n-40 are all not divisible by 3 or 20, cannot be done with 3,6,20. 
        return False