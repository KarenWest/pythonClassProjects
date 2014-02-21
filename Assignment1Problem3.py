# Karen West - Problem 3 - Paying Debt Off in a Year Using Bisection Search
# Oct. 16th, 2012

#for test purpose only - they provide these test values - so try mine!
#accrued while unemployed now for 3 years,2+ months, depending on husband's income!
#balance = 35263 #as of the start of Oct. 2012
#annualInterestRate = 0.2 #20% annual interest rate

#These are the provided test cases for this problem:
#Test Case 1:
#balance = 320000
#annualInterestRate = 0.2

#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 29157.09
      
#Test Case 2:
#balance = 999999
#annualInterestRate = 0.18
	      
#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 90325.07

#Although I got the correct answers with this code, when I submitted it,
#it said the following:
#    Your code took too long to run, and was terminated. Perhaps you have an infinite loop?
#
#    We couldn't run your solution.
   
monthlyInterestRate = annualInterestRate / 12
monthlyPaymentLowBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12
intOnTotalBalAnnualIntRate = (annualInterestRate * balance)
totalBalWithOneYrInt  = balance + intOnTotalBalAnnualIntRate

#print "Lower Bound and Upper Bound to start Monthly Payment for bisection search: "
#print monthlyPaymentLowBound
#print monthlyPaymentUpperBound
#print "total balance with 1 yr interest on whole year"
#print totalBalWithOneYrInt

x = balance
epsilon = .01 #to the 1 cent rather than in problem 2 where it was to the $10
numGuesses = 0
low = monthlyPaymentLowBound
high = monthlyPaymentUpperBound
ans = (high + low) / 2.0
prevBal = balance #to start
totalPaidOneYear = 0

notMadeBestMonthlyPyMtGuess = True
prevBal = x
fixPymtGuessOneYearPayoff = ans
amountOverOrUnderPaid = 0
interestToAddEst = 0
totalAddedIntEst = 0

while (notMadeBestMonthlyPyMtGuess == True):      
    for month in range(12):
        interestToAddEst = (prevBal - fixPymtGuessOneYearPayoff) * monthlyInterestRate
        totalAddedIntEst += interestToAddEst
        prevBal = int((prevBal - fixPymtGuessOneYearPayoff) * (1 + monthlyInterestRate))
        totalPaidOneYear = totalPaidOneYear + fixPymtGuessOneYearPayoff
        #print "After Month: " + str(month + 1) + " was paid"
        #print 'Fixed monthly payment: {0:.2f}'.format(fixPymtGuessOneYearPayoff)
        #print 'Remaining Balance with monthly int added: {0:.2f}'.format(prevBal)
        #print 'paid so far: {0:.2f}'.format(totalPaidOneYear)

    #print 'Balance at Start (input): ' + str(balance)
    #print 'With annual interest rate (input) : {0:.2f}'.format(annualInterestRate)
    #print 'With monthly interest rate (annualIntRate/12): {0:.2f}'.format(monthlyInterestRate)
    #print 'Total Paid: {0:.2f}'.format(totalPaidOneYear)
    #print 'Remaining balance: {0:.2f}'.format(prevBal)
    #print 'Total added interest estimtate: {0:.2f}'.format(totalAddedIntEst)
            
    #if (abs(totalPaidOneYear - totalBalWithOneYrInt) >= epsilon):
    if (abs(totalPaidOneYear - (balance + totalAddedIntEst)) >= epsilon):
         amountOverOrUnderPaid = abs(prevBal)
         #saveClosestToBalNum = amountOverOrUnderPaid
    else: # paid off balance within one cent - done!
        high = ans
        #print "total paid 1 yr - balance < 1 cent!"
        #print 'total paid 1 yr: {0:.2f}'.format(totalPaidOneYear)
        #print 'balance: {0:.2f}'.format(totalBalWithOneYrInt)
        #print 'epsilon: {0:.2f}'.format(epsilon)
        notMadeBestMonthlyPyMtGuess = False

    #print 'How much more or less did you pay this way than the total balance?: ' + str(amountOverOrUnderPaid)
    if (notMadeBestMonthlyPyMtGuess == True):
        #if (abs(totalPaidOneYear < totalBalWithOneYrInt)):
        if (abs(totalPaidOneYear < (balance + totalAddedIntEst))):
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
        fixPymtGuessOneYearPayoff = ans
        #print 'Try increasing-decreasing fixed payment per month to: ' + str(fixPymtGuessOneYearPayoff)
        prevBal = balance #restore original balance to pay off and try again
        totalPaidOneYear = 0
        totalAddedIntEst = 0
        interestToAddToEst = 0
        numGuesses =  numGuesses + 1

    #print 'ending exact  balance paid over or under = ' + str(prevBal)
    #print 'TotalPaidOneYear = ' + str(totalPaidOneYear)

#debug statement
    #if (numGuesses >= 5):
       #notMadeBestMonthlyPyMtGuess = False

#print "Number of guesses to get lowest monthly payment to pay off entire year's balance with 0 left or negative bal:"
#print numGuesses
print 'Lowest Payment: {0:.2f}'.format(fixPymtGuessOneYearPayoff)

