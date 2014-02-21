def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    count = 0
    while x >= b:
        count += 1
        x /= b
    return count
