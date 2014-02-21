# Karen West - Problem 2 - Paying Debt Off in a Year - Oct. 16th, 2012

#for test purpose only - they provide these test values - so try mine!
#accrued while unemployed now for 3 years,2+ months, depending on husband's income!
#balance = 35263 #as of the start of Oct. 2012
#annualInterestRate = 0.2 #20% annual interest rate

#These are the provided test cases for this problem:
#Test Case 1:
#balance = 3329
#annualInterestRate = 0.2

#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 310

#Test Case 2:
#balance = 4773
#annualInterestRate = 0.2
              
#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 440

#Test Case 3:
#balance = 3926
#annualInterestRate = 0.2

#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 360

#OUTPUT FROM YOUR ONLINE CODE CHECKER--some test cases do not work
#Test Case 1

#balance = 3329; annualInterestRate = 0.2

#Output:

#    Lowest Payment: 310


#Test Case 2

#balance = 4773; annualInterestRate = 0.2

#Output:

#    Lowest Payment: 440


#Test Case 3

#balance = 3926; annualInterestRate = 0.2

#Output:

#    Lowest Payment: 360


#Randomized Test Case 1

#balance = 495; annualInterestRate = 0.2

#Your output:

#    Lowest Payment: 0


#Correct output:

#    Lowest Payment: 50


#Randomized Test Case 2

#balance = 139; annualInterestRate = 0.18

#Your output:

#    Lowest Payment: 10


#Correct output:

#    Lowest Payment: 20


#Randomized Test Case 3

#balance = 50; annualInterestRate = 0.25

#Your output:

#    Lowest Payment: 0


#Correct output:

#    Lowest Payment: 10


#Randomized Test Case 4

#balance = 206; annualInterestRate = 0.18

#Your output:

#    Lowest Payment: 0


#Correct output:

#    Lowest Payment: 20


#Randomized Test Case 5

#balance = 4440; annualInterestRate = 0.15

#Your output:

#    Lowest Payment: 410


#Correct output:

#    Lowest Payment: 400


#Randomized Test Case 6

#balance = 4497; annualInterestRate = 0.04

#Output:

#    Lowest Payment: 390


#Randomized Test Case 7

#balance = 4962; annualInterestRate = 0.18

#Your output:

#    Lowest Payment: 460


#Correct output:

#    Lowest Payment: 450


#Randomized Test Case 8

#balance = 3488; annualInterestRate = 0.18

#Your output:

#    Lowest Payment: 340


#Correct output:

#    Lowest Payment: 320


#Randomized Test Case 9

#balance = 3308; annualInterestRate = 0.2

#Your output:

#    Lowest Payment: 300


#Correct output:

#    Lowest Payment: 310


#Randomized Test Case 10

#balance = 4055; annualInterestRate = 0.18

#Output:

#    Lowest Payment: 370


#Randomized Test Case 11

#balance = 3527; annualInterestRate = 0.18

#Output:

#    Lowest Payment: 320


#Randomized Test Case 12

#balance = 4003; annualInterestRate = 0.04

#Your output:

#    Lowest Payment: 350


#Correct output:

#    Lowest Payment: 340


#Note that this guess of a fixed payment to pay each month is too much,
#since it was calculated with an annual interest on the balance, and
#divided by 12 months to pay off the balance.  However, interest is
#actually compounded monthly, so you are deducting too much each month
#in this manner of fixed payment, since you reduce the balance first with
#monthly compounding of interest, before multiplying the interest on the
#balance, so the very last payment will be the least of all, since
#you will have paid too much each month with this type of fixed payment guess.
   
monthlyInterestRate = annualInterestRate / 12
intOnTotalBalAnnualIntRate = (annualInterestRate * balance)
totalBalWithOneYrInt  = balance + intOnTotalBalAnnualIntRate
fixPymtGuessOneYearPayoff = int((totalBalWithOneYrInt / 12))
if ((fixPymtGuessOneYearPayoff % 10) != 0):
    fixPymtGuessOneYearPayoff = int(round(fixPymtGuessOneYearPayoff, -1))
#print "Guess of fixed payment for one year payoff (this method is either exact or too much for first guess): "
#print fixPymtGuessOneYearPayoff

prevBal = balance #to start
totalPaidOneYear = 0
numGuesses = 1
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

while (notMadeBestMonthlyPyMtGuess == True):

    for month in range(11):
        prevBal = int((prevBal - fixPymtGuessOneYearPayoff) * (1 + monthlyInterestRate))
        totalPaidOneYear = int(totalPaidOneYear + fixPymtGuessOneYearPayoff)
        #print "After Month: " + str(month + 1) + " was paid"
        #print 'Fixed monthly payment: ' + str(int(fixPymtGuessOneYearPayoff))
        #print 'Remaining Balance with monthly int added: ' + str(prevBal)
        #print 'paid so far: ' + str(totalPaidOneYear)

    #print 'Balance at Start (input): ' + str(balance)
    #print 'With annual interest rate (input) : {0:.2f}'.format(annualInterestRate)
    #print 'With monthly interest rate (annualIntRate/12): {0:.2f}'.format(monthlyInterestRate)
    #print 'Total Paid: ' + str(totalPaidOneYear)
    #print 'Remaining balance: ' + str(prevBal)
    
    if (totalPaidOneYear > balance) and (prevBal < 0): #paid too much each month
        if (anotherOverPymtCameCloser == False):
            amountOverPaid = abs(prevBal)
            #amountOverPaid = totalPaidOneYear - balance
            if (amountOverPaid < saveClosestToBalNum) and (saveClosestToBalNum > 0):
                saveClosestToBalNum = amountOverPaid
                #print "BAL LEFT!!! = " + str(saveClosestToBalNum)
                #print "AMOUNT PAID!!! each month was " + str(fixPymtGuessOneYearPayoff)
            elif (saveClosestToBalNum == 0):
                saveClosestToBalNum = amountOverPaid
            else: #a previous payment amount came closer to paying off the balance with less bal left at end
                #print "ANOTHER OVERPAYMENT CAME CLOSER !!!"
                anotherOverPymtCameCloser = True
            #print 'saveClosestToBalNum ' + str(saveClosestToBalNum)
            #print 'anotherOverPymtCameCloser bool = '
            #print anotherOverPymtCameCloser
            #print 'How much more did you pay this way than the total balance?: ' + str(amountOverPaid)
            if (anotherOverPymtCameCloser == False):
                numToDecPymtPerMonth = int((totalPaidOneYear - balance) / 12)
                if (numToDecPymtPerMonth > 0):
                    saveRemainingBal = int(prevBal)
                    saveLowPayment = int(fixPymtGuessOneYearPayoff)
                    fixPymtGuessOneYearPayoff = int(fixPymtGuessOneYearPayoff - numToDecPymtPerMonth)
                    if ((fixPymtGuessOneYearPayoff % 10) != 0):
                        fixPymtGuessOneYearPayoff = int(round(fixPymtGuessOneYearPayoff, -1))
                    #print 'Try decreasing fixed payment per month to: ' + str(fixPymtGuessOneYearPayoff)
                    prevBal = balance #restore original balance to pay off and try again
                    totalPaidOneYear = 0
                    numGuesses =  numGuesses + 1
                else:
                    notMadeMonthlyPyMtGuess = False
                    saveRemainingBal = int(prevBal)
                    saveLowPayment = int(fixPymtGuessOneYearPayoff)
        else:
            notMadeBestMonthlyPyMtGuess = False
    elif (prevBal > 0): # paid too little each month so some left over to pay
        amountUnderPaid = prevBal

        #print 'How much less did you pay this way than the total balance?: ' + str(amountUnderPaid)
        if (anotherOverPymtCameCloser == False):
                #print "ANOTHEROVERPAYMENT CAME CLOSER is FALSE"
                if (int(balance) > int(totalPaidOneYear)):
                    numToIncPymtPerMonth = int((balance - totalPaidOneYear) / 12)
                elif (int(balance) < int(totalPaidOneYear)):
                    numToIncPymtPerMonth = int((totalPaidOneYear - balance) / 12)
                #else:
                    #print "HUH???????"
                if (prevPymt == 0):
                    prevPymt = int(fixPymtGuessOneYearPayoff)
                    prevTotalPaidOneYear = totalPaidOneYear
                    prevBalAboveZero = int(prevBal)
                if (prevPymt <= int(fixPymtGuessOneYearPayoff)):
                    saveLowPaymentAboveZero = prevPymt
                    saveTotalPaidOneYear = prevTotalPaidOneYear
                    saveRemainingBalAboveZero = prevBalAboveZero
                prevRoundPymt = int(fixPymtGuessOneYearPayoff)
                #if (saveTotalPaidOneYear < totalPaidOneYear): #did not pay enough, but paid less than last time to pay off
                    #print "PREVIOUS PAYMENT BETTER ANSWER--should exit loop next time"
                fixPymtGuessOneYearPayoff = int(fixPymtGuessOneYearPayoff + numToIncPymtPerMonth)
                if ((fixPymtGuessOneYearPayoff % 10) != 0):
                    fixPymtGuessOneYearPayoff = int(round(fixPymtGuessOneYearPayoff, -1))
                if (int(fixPymtGuessOneYearPayoff) == prevRoundPymt):
                    notMadeBestMonthlyPyMtGuess = False
                #print 'Try increasing fixed payment per month to: ' + str(fixPymtGuessOneYearPayoff)
                prevBal = balance #restore original balance to pay off and try again
                totalPaidOneYear = 0
                numGuesses =  numGuesses + 1
        else: #should be done here
                #print "SHOULD BE DONE HERE"
                notMadeBestMonthlyPyMtGuess = False
    else: #monthly payment was an exact guess of paying off debt in one year's time
        #print "total paid on monthly payment guess was an exact fit to pay off entire balance in one year's time"
        notMadeBestMonthlyPyMtGuess = False
    #print 'saveRemainingBalAboveZero = ' + str(saveRemainingBalAboveZero)
    #print 'saveLowPaymentAboveZero = ' + str(saveLowPaymentAboveZero)
    #print 'prevTotalPaidOneYear = ' + str(prevTotalPaidOneYear)

#debug statement
    #if (numGuesses >= 5):
       #notMadeBestMonthlyPyMtGuess = False

#print "Number of guesses to get lowest monthly payment to pay off entire year's balance with 0 left or negative bal:"
#print numGuesses
print 'Lowest Payment: ' + str(saveLowPaymentAboveZero)    

    
