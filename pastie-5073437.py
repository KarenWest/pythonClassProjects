#balance = 5000
#annualInterestRate = 0.18
#monthlyPaymentRate = 0.02

months = range(1, 13) # 1, 2, ... , 11, 12
owe = balance # It made sense to me to call this total amount oweing
totalPaid = 0

for month in months:
    minPay = owe * monthlyPaymentRate # calculate our minimum payment
    interest = (owe - minPay) * (annualInterestRate / 12) # same for interest
    owe = owe - minPay + interest # calculate our new balance
    totalPaid += minPay # Sum up how much we've paid so far
    print('Month: %d' % month) # %d will be replaced by month
    print('Minimum monthly payment: %.2f' % minPay) # %.2f replaced by minPay, with 2 decimal places
    print('Remaining balance: %.2f' % owe)

print('Total paid %.2f' % totalPaid)
print('Remaining balance: %.2f' % owe)
