# Karen West - Problem 1 - Paying the Minimum - Oct. 15th, 2012

#for test purpose only - they provide these test values - so try mine!
#accrued while unemployed now for 3 years and 2 months, depending only on husband's income!
#balance = 35263 #as of the start of Oct. 2012
#annualInterestRate = 0.2 #18% annual interest rate
#monthlyPaymentRate = 0.04

#Test cases given in assignment:
#Test Case 1:
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#Test Case 2:
#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
prevBal = balance #to start
totalPaidOneYear = 0

for month in range(12):
  minMonthlyPayment = monthlyPaymentRate * prevBal
  totalPaidOneYear += minMonthlyPayment
  prevBal = (prevBal - minMonthlyPayment) * (1 + monthlyInterestRate)
  print "Month: " + str(month + 1)
  print 'Minimum monthly payment: {0:.2f}'.format(minMonthlyPayment)
  print 'Remaining Balance: {0:.2f}'.format(prevBal)

print 'Balance at Start (input): {0:.2f}'.format(balance)
print 'With annual interest rate (input) : {0:.2f}'.format(annualInterestRate)
print 'With monthly interest rate (annualIntRate/12): {0:.2f}'.format(monthlyInterestRate)
print 'With Monthly Payment rate (input): {0:.2f}'.format(monthlyPaymentRate)
print 'Total Paid: {0:.2f}'.format(totalPaidOneYear)
print 'Remaining balance: {0:.2f}'.format(prevBal)

