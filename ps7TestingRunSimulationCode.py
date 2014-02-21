#This is a test of known good code for the runSimulation test
import ps7All4ProbsOneFile
import random
print "Testing the various simulation test cases"
##
'''
random.seed(17)
mean_1=ps7All4ProbsOneFile.runSimulation(1,1,5,5,1.0,5,ps7All4ProbsOneFile.StandardRobot)
print "Should get close to 150 clock ticks: ",mean_1,"; Good code got 166.4"
random.seed(24)
mean_2=ps7All4ProbsOneFile.runSimulation(1,1,10,10,.75,5,ps7All4ProbsOneFile.StandardRobot)
print "Should get close to 190 clock ticks: ",mean_2,"; Good code got 186.0"
random.seed(88)
mean_3=ps7All4ProbsOneFile.runSimulation(1,1,10,10,.90,5,ps7All4ProbsOneFile.StandardRobot)
print "Should get close to 310 clock ticks: ",mean_3,"; Good code got 306.2"
random.seed(13)
mean_4=ps7All4ProbsOneFile.runSimulation(1,1,20,20,1.0,5,ps7All4ProbsOneFile.StandardRobot)
print 'Should get close to 3322 clock ticks: ',mean_4,"; Good code got 3119.2"
random.seed(42)
mean_5=ps7All4ProbsOneFile.runSimulation(3,1,20,20,1.0,5,ps7All4ProbsOneFile.StandardRobot)
print 'Should get close to 1105 clock ticks: ',mean_5,"; Good code got 1217.0"
'''
random.seed(17)
mean_random=ps7All4ProbsOneFile.runSimulation(1,1,5,5,1.0,5,ps7All4ProbsOneFile.RandomWalkRobot)
print "Got from random walk robot clock ticks: ",mean_random,"; good??"
