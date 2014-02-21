#balance = 5000
#annualInterestRate = 0.18

monInt = annualInterestRate / 12 # monthly interest
owing = 1 # make sure we enter the while loop
minPay = 0 # Will be incremented to 10 on the first pass

while owing > 0: # If we have negative owing, then we've paid enough!
    minPay += 10 # Increment each time to see
    owing = balance # (re)set owing to original balance
    for month in range(12):
        owing = (owing - minPay) * (1 + monInt) # calculate owing using the PS formula, easy!

print('Lowest Payment: %d' % minPay) # %d is replaced by minPay
