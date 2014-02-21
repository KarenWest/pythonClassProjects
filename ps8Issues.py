class ResistantVirus(SimpleVirus):
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
        SimpleVirus.__init__(self,maxBirthProb, clearProb)
        self.resistances=resistances
        self.mutProb=mutProb
        # TODO


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
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
        
        # TODO
        return drug in self.resistances and self.resistances[drug]
    
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
        res=True
        for a in activeDrugs:
            res=res and self.getResistances()[a]
        if res:   
            if random.random()<(self.getMaxBirthProb() * (1 - popDensity)) :
                newDrugRes = self.getResistances().copy()
                for drug in self.resistances:
                    if random.random() > (1-self.getMutProb()):
                        newDrugRes[drug]=not newDrugRes[drug]
                    
                return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(),newDrugRes, self.getMutProb())
            else:
                raise NoChildException()
        else:
            raise NoChildException()
        # TODO
        
        
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self,viruses,maxPop)
        self.drugList=[]
        
        # TODO


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if not (newDrug in self.drugList):
            self.drugList.append(newDrug)
        return
        # TODO


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugList
        # TODO


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        pop=0
        for b in self.getViruses():
            
            for a in drugResist:
            
                if b.isResistantTo(a):
                    pop+=1
                    break
        return pop


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
        
        tempVirList=self.getViruses()[:]
        for vir in tempVirList:
            if vir.doesClear():
                
                self.viruses.remove(vir)
        
        tempVirList=self.getViruses()[:]
        popDen=self.getTotalPop()/float(self.maxPop)
        for vir in tempVirList:
            
            try:
                self.viruses.append(vir.reproduce(popDen,self.drugList))
            except NoChildException:
                pass
        # TODO
        return self.getTotalPop()



#
# PROBLEM 5

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
    time =300
    virusPop=[]
    for i in range(time):
        
        virusPop.append(0)
    resVirusPop=[]
    for i in range(time):
        
        resVirusPop.append(0)
    viruses=[]
    for a in range(100):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    
    for trials in range(numTrials):
        temp = viruses[:]
        
        someGuy = TreatedPatient(temp,maxPop)
        for timeStep in range(time):
            if timeStep == (time/2):
                someGuy.addPrescription('guttagonol')
            someGuy.update()
            virusPop[timeStep]=someGuy.getTotalPop()+virusPop[timeStep]
            resVirusPop[timeStep]=someGuy.getResistPop(['guttagonol'])+resVirusPop[timeStep]
            
    avgVirusPop=[]        
    for h in virusPop:
        avgVirusPop.append(h/float(numTrials))
    avgResVirusPop=[]        
    for h in resVirusPop:
        avgResVirusPop.append(h/float(numTrials))
    pylab.figure()
    pylab.plot(range(time),avgResVirusPop, label = 'resistive')
    pylab.plot(range(time),avgVirusPop,label='total')
    pylab.title('virus populations')
    pylab.xlabel('time')
    pylab.ylabel('Num of Viruses')
    pylab.legend()
    
    pylab.show()