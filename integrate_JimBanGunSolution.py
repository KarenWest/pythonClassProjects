def successiveApproxIntegrate(f, a, b, epsilon):

    def integrate(func, x, y, parts):
        spacing = float(y-x)/parts
        current = 0
        for i in range(parts):
            current += spacing * func(x+ i*spacing)
        return current

    N = 2
    M = 1
    
    while True:
        x = integrate(f, a, b, N)
        y = integrate(f, a, b, M)
        if abs(x - y) >= epsilon:
            M *= 2
            N = 2*M
        else:
            break
    return x