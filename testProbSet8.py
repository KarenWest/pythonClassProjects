# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics 
import math
import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):
    maxBirthProb = 0.0
    clearProb = 0.0

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb #virus max. birth rate under optimal conditions
        self.clearProb = clearProb #virus max. clearance probability under optimal conditions
        #random.seed(0)
        
    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if (self.getClearProb() == 1.0):
            return True
        elif (self.getClearProb() == 0.0):
            return False
        #random.seed(0)
        num = random.random()
        if (num <= self.getClearProb()):
            #print "clear virus particle - random # " + str(num) + " <= clear Prob " + str(self.getClearProb())
            return True
        else:
            #print "DO NOT clear virus particle - random # " + str(num) + " > clear Prob " + str(self.getClearProb())
            return False
        
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.getMaxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.
        --should be calculated in the update method of the Patient class
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # reproduce method in simpleVirus should produce an offspring by returning a new instance
        # of SimpleVirus with probability: self.maxBirthRate * (1 - popDensity).
        #random.seed(0)
        num = random.random()
        #print "pop density " + str(popDensity)
        
        if (num <= (self.getMaxBirthProb() * (1 - popDensity))):
            # should reproduce - so create and return instance of offspring SimpleVirus, which has
            # the same maxBirthProb and clearProb values as its parent.
            #print "reproducing " + "random num = " + str(num) + " ?? <= (maxBirthProb * (1-popDensity)) ?? " + str((self.getMaxBirthProb() * (1 - popDensity))) 
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            #print "random num = " + str(num) + " ?? <= (maxBirthProb * (1-popDensity)) ?? " + str((self.getMaxBirthProb() * (1 - popDensity)))
            return False
            #raise NoChildException("NoChildException - no simple virus reproduced")

class Patient(object):
    viruses = []
    maxPop = 0
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        # (??) assume that the current total virus population is the length of the SimpleVirus list,
        # so each SimpleVirus instance, represents one of the total virus population
        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        numViruses = self.getTotalPop()
        virusList = self.getViruses()
        virusesToRemove = []
        virusListCopy = virusList[:]
        maxVirusPop = self.getMaxPop()
        removeViruses = False
        #calculate the population density
        popDensity = float(numViruses) / float(maxVirusPop)
        #print "update: popDensity = " + str(popDensity) + " len viruses = " + str(len(virusList))
        if (popDensity < 1.0) and (len(virusList) > 0):
            for virus in virusListCopy:
                #print "should virus.getMaxBirthProb() be cleared? " + str(virus.getMaxBirthProb())
                #print "should virus.getClearProb() be cleared? " + str(virus.getClearProb())
                removeViruses = False
                if (virus.doesClear() == True):
                    virusesToRemove.append(virus)
                    removeViruses = True
            if (removeViruses == True):
                for virus in virusesToRemove:
                    #print "removing virus.getMaxBirthProb() " + str(virus.getMaxBirthProb())
                    #print "removing virus.getClearProb() " + str(virus.getClearProb())
                    self.viruses.remove(virus)
            virusList = self.getViruses()
            if (len(virusList) > 0):
                numViruses = self.getTotalPop()
                popDensity = float(numViruses / maxVirusPop)
                virusListCopy = virusList[:]
                for virus in virusListCopy:
                    offSpringVirus = virus.reproduce(popDensity)
                    #if (isInstance(offSpringVirus, SimpleVirus)):
                    #if it gets this far, then append, since no exception occurred
                    if (offSpringVirus != False):
                        self.viruses.append(offSpringVirus)
        return self.getTotalPop()
'''
Test results
CORRECT 
Test: Initialization 1

Initialize a SimpleVirus

Output:

    Passed test

Test: Initialization 2

Initialize a Patient

Output:

    Passed test

Test: SimpleVirus 1

Initialize a SimpleVirus that is never cleared and always reproduces

Output:

    v1 = SimpleVirus(1.0, 0.0)
    Testing doesClear and reproduce methods
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    Test completed.

Test: SimpleVirus 2

Initialize a SimpleVirus that is never cleared and never reproduces

Output:

    v1 = SimpleVirus(0.0, 0.0)
    Testing doesClear and reproduce methods
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    v1.doesClear(): False
    Test completed.

Test: SimpleVirus 3

Initialize a SimpleVirus that is always cleared and always reproduces

Output:

    v1 = SimpleVirus(1.0, 1.0)
    Testing doesClear and reproduce methods
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    Test completed.

Test: SimpleVirus 4

Initialize a SimpleVirus that is always cleared and never reproduces

Output:

    v1 = SimpleVirus(0.0, 1.0)
    Testing doesClear and reproduce methods
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    v1.doesClear(): True
    Test completed.

Test: SimpleVirus 5

Initialize a SimpleVirus with randomized probabilities

Output:

    v1 = SimpleVirus(0.97, 0.03)
    Testing reproduce. Be sure your implementation is making EXACTLY ONE call to random.random(), and no other random module calls.
    popDensity = 0.03
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Reproduced successfully
    Test completed.

Test: class Patient 1

Initialize a Patient with randomized viruses

Output:

    viruses = [ SimpleVirus(0.97, 0.87) SimpleVirus(0.66, 0.37) SimpleVirus(0.81, 0.65) SimpleVirus(0.08, 0.77) ]
    P1 = Patient(viruses, 6)
    P1.getTotalPop() = 4

Test: class Patient 2

Create a Patient with virus that is never cleared and always reproduces

Output:

    virus = SimpleVirus(1.0, 0.0)
    patient = Patient([virus], 100)
    Updating the patient for 100 trials...
    patient.getTotalPop() expected to be >= 100
    Test successfully completed

Test: class Patient 3

Create a Patient with virus that is always cleared and always reproduces

Output:

    virus = SimpleVirus(1.0, 1.0)
    patient = Patient([virus], 100)
    Updating the patient for 100 trials...
    patient.getTotalPop() expected to = 0
    Test successfully completed

Test: class Patient 4

Initialize a Patient with randomized viruses

Output:

    viruses = [ SimpleVirus(0.0, 0.98) SimpleVirus(0.49, 0.94) SimpleVirus(0.78, 0.87) SimpleVirus(0.11, 0.95) ]
    P1 = Patient(viruses, 8)
    P1.getTotalPop() = 4
    Updating patient 25 times... all exceptions should be handled...
    Test Completed
'''
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
    totalVirusPopulationList = [0]
    steps = 300
    #stepList = pylab.arange(0,100)
    for i in range(numTrials):
        virusList = []
        for i in range(numViruses):
            virus = SimpleVirus(maxBirthProb, clearProb)
            virusList.append(virus)

        #print "trial num = " + str(i)
        a_patient = Patient(virusList, maxPop)
        for timeStep in range(steps):
            #print "time step " + str(timeStep)
            a_patient.update()
        avgVirusPopulationPerStep = float((a_patient.getTotalPop())/numTrials)
        print "this trial gave avg virus population per Trial: " + str(avgVirusPopulationPerStep)
        totalVirusPopulationList.append(avgVirusPopulationPerStep)
    pylab.plot(totalVirusPopulationList, 'b', label="SimpleVirus Simulation")      
    #pylab.plot(stepList, totalVirusPopulationList, 'b')      
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Average Size of Virus Population in Patient')
    pylab.legend()
    pylab.title('Clearance of SimpleVirus Particles in Patient')
    #pylab.semilogx()
    #pylab.semilogy()
    #pylab.saveFig('simNoDrug.png')
    pylab.show()
'''
test simulationWithoutDrug() with:
numViruses = 100
maxPop (maximum sustainable virus population) = 1000
maxBirthProb (maximum reproduction probability for a virus particle) = 0.1
clearProb (maximum clearance probability for a virus particle) = 0.05
numTrials = up to 100
'''
simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)
'''
Test results
INCORRECT 
Test: simulation 1

Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module. Additionally, be sure you call pylab.show() last. The order of other lines do not matter.

Your output:

    Test: simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
    Plotting...
    Plotting values: [0, 11]
    Successfully called pylab.xlabel with label: Number of Steps
    Successfully called pylab.ylabel with label: Average Size of Virus Population in Patient
    Successfully called pylab.legend
    Successfully called pylab.title with label: Clearance of Virus Particles in Patient
    Successfully called pylab.show

Correct output:

    Test: simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
    Plotting...
    Plotting values: [2.0, 3.0, 5.0, 7.0, 8.0, 9.0, 9.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0]
    Successfully called pylab.title with label: SimpleVirus simulation
    Successfully called pylab.xlabel with label: Time Steps
    Successfully called pylab.ylabel with label: Average Virus Population
    Successfully called pylab.legend
    Successfully called pylab.show

Test: simulation 2

Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module. Additionally, be sure you call pylab.show() last. The order of other lines do not matter.

Your output:

    Test: simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
    Plotting...
    Plotting values: [0, 0]
    Successfully called pylab.xlabel with label: Number of Steps
    Successfully called pylab.ylabel with label: Average Size of Virus Population in Patient
    Successfully called pylab.legend
    Successfully called pylab.title with label: Clearance of Virus Particles in Patient
    Successfully called pylab.show

Correct output:

    Test: simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
    Plotting...
    Plotting values: [91.0, 54.0, 37.0, 22.0, 10.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    Successfully called pylab.title with label: SimpleVirus simulation
    Successfully called pylab.xlabel with label: Time Steps
    Successfully called pylab.ylabel with label: Average Virus Population
    Successfully called pylab.legend
    Successfully called pylab.show

Test: simulation 3

Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module. Additionally, be sure you call pylab.show() last. The order of other lines do not matter.

Your output:

    Test: simulationWithoutDrug(1, 90, 0.8, 0.1, 1)
    Plotting...
    Plotting values: [0, 0]
    Successfully called pylab.xlabel with label: Number of Steps
    Successfully called pylab.ylabel with label: Average Size of Virus Population in Patient
    Successfully called pylab.legend
    Successfully called pylab.title with label: Clearance of Virus Particles in Patient
    Successfully called pylab.show

Correct output:

    Test: simulationWithoutDrug(1, 90, 0.8, 0.1, 1)
    Plotting...
    Plotting values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    Successfully called pylab.title with label: SimpleVirus simulation
    Successfully called pylab.xlabel with label: Time Steps
    Successfully called pylab.ylabel with label: Average Virus Population
    Successfully called pylab.legend
    Successfully called pylab.show

A good question to consider as you look at your plot is: about how long does
it take before the population stops growing?

--About 50 time-steps
--About 100 time-steps
--About 150 time-steps
--About 200 time-steps
--About 250 time-steps
'''
#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    resistances = {}
    mutProb = 0.0
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        #dictionary look-up: drug strings as keys map to state of virus particle's resistance (T/F) to each drug
        #(??) do you really need to copy dictionary for just a look-up?
        resistancesCopy = {}
        resistancesCopy = self.resistances.copy() #don't clobber resistance dictionary
        if resistancesCopy[drug] == True:
            return True
        else
            return False


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.getMaxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        #Stochastically determines whether this virus particle reproduces at a
        #time step. Called by the update() method in the TreatedPatient class.
        #stochastic = previous state plus random state makes the next state
        #random.seed(0)
        num = random.random()
        reproduceTheVirus = False
        #A virus particle will only reproduce if it is resistant to ALL the drugs
        #in the activeDrugs list. For example, if there are 2 drugs in the
        #activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        #then it will NOT reproduce.
        for drug in activeDrugs:
            if (reproduceTheVirus == False) and (isResistantTo(drug) == False):
                reproduceTheVirus = True
        '''        
        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.getMaxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.
        '''
        
        if (reproduceTheVirus == True) and (num <= (self.getMaxBirthProb() * (1 - popDensity))):
            # should reproduce - so create and return instance of offspring ResistantVirus, which has
            # the same maxBirthProb and clearProb and mutProb values as its parent.
            #print "reproducing " + "random num = " + str(num) + " ?? <= (maxBirthProb * (1-popDensity)) ?? " + str((self.getMaxBirthProb() * (1 - popDensity))) 
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), self.getMutProb())
        else:
            #print "random num = " + str(num) + " ?? <= (maxBirthProb * (1-popDensity)) ?? " + str((self.getMaxBirthProb() * (1 - popDensity)))
            return False
            #raise NoChildException("NoChildException - no simple virus reproduced")
        '''
        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.
        ----no code needed to deal with this part--just an explanation of inheritance and resistance to virus traits
        '''    

class TreatedPatient(Patient):
    drugsAdministered = []
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        self.drugsAdministered = []
        #the viruses have an attribute that tells what drugs patient is resistant to, along with their mutation probability

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.getPrescriptions(): #if newDrug NOT already prescribed to patient
            self.drugsAdministered.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugsAdministered


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        lenDrugResist = len(drugResist)
        virusListResistantToAllDrugs = []
        totalPopulationViruses = self.getTotalPop()
        countVirusesResistantToAllDrugs = 0
        for virus in totalPopulationViruses:
            countDrugsResistantTo = 0
                for drug in drugResist:
                    if (virus.isResistantTo(drug) == False):
                        break
                    else:
                        countDrugsResistantTo += 1
            if (countDrugsResistantTo == lenDrugList): #then this virus is resistant to all drugs in list
                virusListResistantToAllDrugs.append(virus)
        countVirusesResistantToAllDrugs = len(virusListResistantToAllDrugs)
        return (countVirusesResistantToAllDrugs)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        numViruses = self.getTotalPop()
        virusList = self.getViruses()
        virusesToRemove = []
        virusListCopy = virusList[:]
        maxVirusPop = self.getMaxPop()
        removeViruses = False
        #calculate the population density
        popDensity = float(numViruses) / float(maxVirusPop)

        virusListThatWillNotReproduceButNotClear = []
        for virus in virusListCopy:
            for drug in self.getPrescriptions():
                if not virus.isResistantTo(drug) and virus not in virusListThatWillNotReproduceButNotClear:
                    virusListThatWillNotReproduceButNotClear.append(virus)
        virusesThatCanReproduce = []
        for virus in virusListCopy:
            if virus not in virusListThatWillNotReproduceButNotClear:
                virusesThatCanReproduce.append(virus)
        #unlike the Simple virus that can be cleared, the Resistant Virus cannot be cleared, but if not
        #resistant to a drug, it will not reproduce
        
        for virus in virusesThatCanReproduce:
            if (len(virusesThatCanReproduce) > 0):
                numViruses = self.getTotalPop()
                popDensity = float(numViruses / maxVirusPop)
                offSpringVirus = virus.reproduce(popDensity, self.getPrescriptions())
                    #if (isInstance(offSpringVirus, SimpleVirus)):
                    #if it gets this far, then append, since no exception occurred
                    if (offSpringVirus != False):
                        self.viruses.append(offSpringVirus)
        return self.getTotalPop()

#seems that we cannot call getResistPop() since we do not have a list of drugs to which       
#have been already administered to the patient, and do not know which ones it is resistant to,
#so just call reproduce() with the list of prescriptions, only on those viruses that can reproduce,
#those that are resistant to the drugs are viruses that can reproduce

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

    

