

    def nuggets_counts(n):
    """
    n is an int
    Returns tupple of number of twenties, niners and sixpacks if some integer combination of 6, 9 and 20 equals n
    Otherwise returns empty tupple.
    """
    for twenties in reversed(range(n // 20 +1)):
    left = n - 20 * twenties
    if left == 0:
    return twenties, 0, 0
    for niners in reversed(range(left // 9 +1)):
    left2 = left - niners * 9
    if left2 % 6 == 0:
    return twenties, niners , left2 // 6
    return ()
    def nuggets(n):
    """ n int -> True if can be ordered with 6, 9, 20 pack combination else False
    """
    return n >= 0 and (n == 0 or (nuggets(n - 20) or nuggets(n - 9) or nuggets(n - 6)))
    def nuggets2(n):
    """ n int -> True if can be ordered with 6, 9, 20 pack combination else False
    """
    return n >= 0 and (any(n % size == 0 for size in (6, 9, 20)) or (nuggets2(n - 20) or nuggets2(n - 9) or nuggets2(n - 6)))
    def nug(a,b,c):
    return 6*a + 9*b + 20*c
    for t in (60, 15, 16, 19, 18, 10001):
    result = nuggets_counts(t)
    print 'Recursively:', nuggets(t)
    if not result:
    print t, 'not possible but you can'
    t, result = next((t + more, nuggets_counts(t + more)) for more in range(1, 6) if nuggets_counts(t+more))
    print 'buy {t}: {result[0]} twenties, {result[1]} niners and {result[2]} sixpacks.'.format(t=t, result=result)
    print

