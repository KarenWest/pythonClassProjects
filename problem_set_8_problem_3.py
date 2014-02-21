#
# PROBLEM 3
#

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    steps = 300
    averages = [0.0] * steps
    for t in range(numTrials):
        viruses = [SimpleVirus(maxBirthProb, clearProb) 
                   for _ in range(numViruses)]
        p = Patient(viruses, maxPop)
        for step in range(steps):
            averages[step] += p.update()
        #print('Trial: ' + str(t))
    for i in range(steps):
        averages[i] /= numTrials
    pylab.plot(averages, label='SimpleVirus')
    pylab.title('Simulation without drugs')
    pylab.xlabel('Steps')
    pylab.ylabel('Average virus population size')
    pylab.legend()
    pylab.show()
#from ps8b_precompiled_27 import *
#import time
#t1 = time.time()
#simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
#print(time.time() - t1)