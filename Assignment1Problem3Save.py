# Karen West - Problem 3 - Paying Debt Off in a Year Using Bisection Search
# Oct. 16th, 2012

#for test purpose only - they provide these test values - so try mine!
#accrued while unemployed now for 3 years,2+ months, depending on husband's income!
#balance = 35263 #as of the start of Oct. 2012
#annualInterestRate = 0.2 #20% annual interest rate

#These are the provided test cases for this problem:
#Test Case 1:
balance = 320000
annualInterestRate = 0.2

#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 29157.09
      
#Test Case 2:
#balance = 999999
#annualInterestRate = 0.18
	      
#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 90325.07
   
monthlyInterestRate = annualInterestRate / 12
monthlyPaymentLowBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12

#if ((monthlyPaymentLowBound % 10) != 0):
#    monthlyPaymentLowBound = int(round(monthlyPaymentLowBound, -1))
#if ((monthlyPaymentHighBound % 10) != 0):
#    monthlyPaymentHighBound = int(round(monthlyPaymentHighBound, -1))
print "Lower Bound and Upper Bound to start Monthly Payment for bisection search: "
print monthlyPaymentLowBound
print monthlyPaymentUpperBound

x = balance
epsilon = .01 #to the 1 cent rather than in problem 2 where it was to the $10
numGuesses = 0
low = monthlyPaymentLowBound
high = monthlyPaymentUpperBound
ans = (high + low) / 2.0
prevBal = balance #to start
totalPaidOneYear = 0

notMadeBestMonthlyPyMtGuess = True
saveRemainingBal = 0
saveLowPayment = 0
saveClosestToBalNum = 0
anotherOverPymtCameCloser = False
saveRemainingBalAboveZero = 0
saveLowPaymentAboveZero = 0
prevTotalPaidOneYear = 0
prevPymt = 0
saveTotalPaidOneYear = 0
prevBalAboveZero = 0
prevRoundPymt = 0
prevBal = x
fixPymtGuessOneYearPayoff = ans
while (notMadeBestMonthlyPyMtGuess == True):      
    for month in range(11):
        prevBal = int((prevBal - fixPymtGuessOneYearPayoff) * (1 + monthlyInterestRate))
        totalPaidOneYear = totalPaidOneYear + fixPymtGuessOneYearPayoff
        print "After Month: " + str(month + 1) + " was paid"
        print 'Fixed monthly payment: ' + str(int(fixPymtGuessOneYearPayoff))
        print 'Remaining Balance with monthly int added: ' + str(prevBal)
        print 'paid so far: ' + str(totalPaidOneYear)

    print 'Balance at Start (input): ' + str(balance)
    print 'With annual interest rate (input) : {0:.2f}'.format(annualInterestRate)
    print 'With monthly interest rate (annualIntRate/12): {0:.2f}'.format(monthlyInterestRate)
    print 'Total Paid: ' + str(totalPaidOneYear)
    print 'Remaining balance: ' + str(prevBal)
    
    if (totalPaidOneYear > balance) and (prevBal < 0): #paid too much each month
        print "PAID TOO MUCH PER MONTH"
        if (anotherOverPymtCameCloser == False):
            amountOverPaid = abs(prevBal)
            if ((totalPaidOneYear - balance)>= epsilon):
                saveClosestToBalNum = amountOverPaid
            else: # paid off balance within one cent - done!
                notMadeBestMonthlyPyMtGuess = False
            print 'How much more did you pay this way than the total balance?: ' + str(amountOverPaid)
            if (notMadeBestMonthlyPyMtGuess == True):
                high = ans
                ans = (low + high) / 2.0
                fixPymtGuessOneYearPayoff = ans
                print 'Try decreasing fixed payment per month to: ' + str(fixPymtGuessOneYearPayoff)
                prevBal = balance #restore original balance to pay off and try again
                totalPaidOneYear = 0
                numGuesses =  numGuesses + 1
        else:
            notMadeBestMonthlyPyMtGuess = False
    elif (prevBal > 0): # paid too little each month so some left over to pay
        amountUnderPaid = prevBal

        print 'How much less did you pay this way than the total balance?: ' + str(amountUnderPaid)
        if (anotherOverPymtCameCloser == False):
                low = ans
                ans = (low + high) / 2.0
                fixPymtGuessOneYearPayoff = ans
                if (prevPymt == 0):
                    prevPymt = fixPymtGuessOneYearPayoff
                    prevTotalPaidOneYear = totalPaidOneYear
                    prevBalAboveZero = int(prevBal)
                if ((totalPaidOneYear - balance)>= epsilon):
                #if (prevPymt <= int(fixPymtGuessOneYearPayoff)):
                    saveLowPaymentAboveZero = prevPymt
                    saveTotalPaidOneYear = prevTotalPaidOneYear
                    saveRemainingBalAboveZero = prevBalAboveZero
                prevRoundPymt = fixPymtGuessOneYearPayoff
                if (saveTotalPaidOneYear < totalPaidOneYear): #did not pay enough, but paid less than last time to pay off
                    print "PREVIOUS PAYMENT BETTER ANSWER--should exit loop next time"
                if (fixPymtGuessOneYearPayoff == prevRoundPymt):
                    notMadeBestMonthlyPyMtGuess = False
                print 'Try increasing fixed payment per month to: ' + str(fixPymtGuessOneYearPayoff)
                prevBal = balance #restore original balance to pay off and try again
                totalPaidOneYear = 0
                numGuesses =  numGuesses + 1
        else: #should be done here
                notMadeBestMonthlyPyMtGuess = False
    else: #monthly payment was an exact guess of paying off debt in one year's time
        print "total paid on monthly payment guess was an exact fit to pay off entire balance in one year's time"
        notMadeBestMonthlyPyMtGuess = False
    print 'saveRemainingBalAboveZero = ' + str(saveRemainingBalAboveZero)
    print 'saveLowPaymentAboveZero = ' + str(saveLowPaymentAboveZero)
    print 'prevTotalPaidOneYear = ' + str(prevTotalPaidOneYear)

#debug statement
    #if (numGuesses >= 5):
       #notMadeBestMonthlyPyMtGuess = False

print "Number of guesses to get lowest monthly payment to pay off entire year's balance with 0 left or negative bal:"
print numGuesses
print 'Lowest Payment: ' + str(saveLowPaymentAboveZero)

