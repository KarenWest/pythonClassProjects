#balance = 320000
#annualInterestRate = 0.2

# Use the formulas provided on the page!
monInt = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monInt) ** 12) / 12


# Use a function to simplify the code after
def paid_off(bal, annualInt, pay):
    '''
    bal: the balance to pay off
    annualInt: the interest rate of the loan
    pay: how much to pay off monthly
    returns: whether the balance was paid off after 12 months
    '''
    monInt = annualInt / 12
    for month in range(12):
        bal = (bal - pay) * (1 + monInt) # Use same forumla as for p2
    return bal <= 0


while True: # we will break when finish
    bisec = (upperBound + lowerBound) / 2 # find the bisection of monthlyPay
    if paid_off(balance, annualInterestRate, bisec): # did we pay it off?
        upperBound = bisec # Then maybe we could pay a lower amount, decrease upper bound
    else:
        lowerBound = bisec # Otherwise, we need to pay more, increase lower bound
    # This is a debugging print line I used
    #print('%6.2d -- %6.2d -- %6.2d' % (lowerBound, bisec, upperBound))
    if (upperBound - lowerBound) < 0.01: # Have UpBo and LoBo converged?
        break
# We've now found the best payment then
print("Lowest Payment: {:.2f}".format(bisec)) # {:.2f} is replaced by bisec, to 2 decimal places
