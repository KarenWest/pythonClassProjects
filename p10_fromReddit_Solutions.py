def successiveApproxIntegrate(f, a, b, epsilon):
    parts = 1
    last = integrate(f, a, b, parts)
    parts *= 2
    estimate = integrate(f, a, b, parts)
    while abs(last - estimate) >= epsilon:
        last = estimate
        parts *= 2
        estimate = integrate(f, a, b, parts)

    return estimate