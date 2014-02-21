#
# PROBLEM 5
#

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    stage = 150
    steps = 300
    averages = [0.0] * steps
    avg_resist = [0.0] * steps
    for t in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, 
                                  resistances, mutProb) 
                   for _ in range(numViruses)]
        tp = TreatedPatient(viruses, maxPop)
        for step in range(steps):
            if step == stage:
                tp.addPrescription('guttagonol')
            averages[step] += tp.update()
            avg_resist[step] += tp.getResistPop(['guttagonol'])
        #print('Trial: ' + str(t))
    for i in range(steps):
        averages[i] /= numTrials
        avg_resist[i] /= numTrials
    pylab.plot(averages, label='ResistantVirus')
    pylab.plot(avg_resist, label='Resist \'guttagonol\'')
    pylab.title('Simulation with drugs')
    pylab.xlabel('Steps')
    pylab.ylabel('Average virus population size')
    pylab.legend()
    pylab.show()
#from ps8b_precompiled_27 import *
#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonal': False}, 0.005, 100)
#import time
#t = time.time()
#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 1)
#print(time.time() - t)