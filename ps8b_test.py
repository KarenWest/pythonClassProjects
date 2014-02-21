# License: Public Domain
# Version: 0.5.4

import sys
import os
import unittest

from ps8b import *


# DONE
#
# Problem 2
# - Don't use random.seed()
# - Make sure that a maxBirthProb of 1.0 and popDensity of 0.0 reproduces
# - Make sure that a popDensity of 1.0 doesn't reproduce
# - Use only random.random()
# - One single call to random.random() in doesClear() and reproduce()
# - Check return type for all methods
# - Make sure the update() method uses both the doesClear() 
#   and reproduce() methods
# - Check density parameter type when used in reproduce()
# - Check type of SimpleVirus __init__() parameters when used in reproduce()
# - Make sure the correct viruses are cleared in update(), no mutation
# - Make sure the correct viruses are reproduced in update(), no mutation
# - Make sure not to add parentheses when catching the exception 
#   on the update() method
#
# Problem 3
# - Check number of Patient objects instantiated
# - Make sure the number of steps being used is 300
# - Make sure pylab functions are called
#   pylab.plot()
#   pylab.title()
#   pylab.xlabel()
#   pylab.ylabel()
#   pylab.legend()
#   pylab.show()
# - Make sure averages are floats
#
# Problem 4
# - Don't use random.seed()
# - Make sure that a maxBirthProb of 1.0 and popDensity of 0.0 reproduces
# - Make sure that a popDensity of 1.0 doesn't reproduce
# - Make sure that a non resistant virus doesn't reproduce
# - Use only random.random()
# - One single call to random.random() in doesClear() and reproduce()
# - Check return type for all methods
# - Make sure the update() method uses both the doesClear() 
#   and reproduce() methods
# - Check density parameter type when used in reproduce()
# - Check type of ResistantVirus __init__() parameters when used in reproduce()
# - Make sure the correct viruses are cleared in update(), no mutation
# - Make sure the correct viruses are reproduced in update(), no mutation
# - Warn if not calling SimpleVirus.__init__() method
# - Warn if not calling Patient.__init__() method
# - Make sure the ResistantVirus is created with a new dictionary and not 
#   just an alias
# - Check if isResistantTo doesn't raise an exception when it receives 
#   an unknown drug
# - Make sure drugs have no repeated values
# - Use getMaxBirthProb() method instead of accessing the variable directly
# - Use getClearProb() method instead of accessing the variable directly
# - Use getMaxPop() method instead of accessing the variable directly
# - Make sure not to add parentheses when catching the exception 
#   on the update() method
#
# Problem 5
#
# - Check number of TreatedPatient objects instantiated
# - Make sure the number of steps being used is 300
# - Make sure pylab functions are called
#   pylab.plot()
#   pylab.title()
#   pylab.xlabel()
#   pylab.ylabel()
#   pylab.legend()
#   pylab.show()
# - Make sure averages are floats


class CommonTests(object):
    @staticmethod
    def test_1(unit, virus, patient):
        '''
        - Check return type for all methods
        '''
        test = isinstance(virus.getMaxBirthProb(), float)
        msg = ('The return value for the getMaxBirthProb() ' + 
               'method must be a float object.')
        unit.assertTrue(test, msg)
        test = isinstance(virus.getClearProb(), float)
        msg = ('The return value for the getClearProb() ' + 
               'method must be a float object.')
        unit.assertTrue(test, msg)
        test = isinstance(virus.doesClear(), bool)
        msg = ('The return value for the doesClear() ' + 
               'method must be a boolean object.')
        unit.assertTrue(test, msg)
        test = isinstance(patient.getViruses(), list)
        msg = ('The return value for the getViruses() ' + 
               'method must be a list object.')
        unit.assertTrue(test, msg)
        
        test = isinstance(patient.getMaxPop(), int)
        msg = ('The return value for the getMaxPop() ' + 
               'method must be an integer object.')
        unit.assertTrue(test, msg)
        test = isinstance(patient.getTotalPop(), int)
        msg = ('The return value for the getTotalPop() ' + 
               'method must be an integer object.')
        unit.assertTrue(test, msg)
        test = isinstance(patient.update(), int)
        msg = ('The return value for the update() ' + 
               'method must be an integer object.')
        unit.assertTrue(test, msg)
        
        if (isinstance(virus, ResistantVirus) and 
            isinstance(patient, TreatedPatient)):
            test = isinstance(virus.isResistantTo('xorox'), bool)
            msg = ('The return value for the isResistantTo() ' + 
                   'method must be a boolean object.')
            unit.assertTrue(test, msg)
            test = patient.addPrescription('xorox') == None
            msg = ('The return value for the addPrescription() ' + 
                   'method must be None.')
            unit.assertTrue(test, msg)
            test = isinstance(patient.getPrescriptions(), list)
            msg = ('The return value for the getPrescriptions() ' + 
                   'method must be a list object.')
            unit.assertTrue(test, msg)
            test = isinstance(patient.getResistPop(['xorox']), int)
            msg = ('The return value for the getResistPop() ' + 
                   'method must be an integer object.')
            unit.assertTrue(test, msg)
            args = [0.0, ['xorox']]
        else:
            args = [0.0]
        
        test = isinstance(virus.reproduce(*args), virus.__class__)
        msg = ('The return value for the reproduce() ' + 
               'method when it reproduces must be a ' + 
               virus.__class__.__name__ + ' object.')
        unit.assertTrue(test, msg)
        try:
            args[0] = 1.0
            virus.reproduce(*args)
            msg = ('The reproduce() method must raise a NoChildException ' + 
                   'exception when it doesn\'t reproduce.')
            unit.assertTrue(False, msg)
        except NoChildException:
            pass
    
    @staticmethod
    def test_2(unit, virus):
        '''
        - One single call to random.random() in doesClear() and reproduce()
        '''
        temp_random = random.random
        unit.count = 0
        def custom_random(*args, **kwargs):
            unit.count += 1
            return temp_random(*args, **kwargs)
        random.random = custom_random
        
        unit.count = 0
        virus.doesClear()
        test = unit.count <= 1
        msg = ('You must call the random.random() method ' + 
               'just once on the doesClear() method.')
        unit.assertTrue(test, msg)
        unit.count = 0
        if isinstance(virus, ResistantVirus):
            virus.reproduce(0.0, ['xorox'])
            # One for the the birth probability and 
            # one for the mutation probability 
            test = unit.count <= 2
        else:
            virus.reproduce(0.0)
            test = unit.count <= 1
        msg = ('You must call the random.random() method ' + 
               'just once on the reproduce() method.')
        unit.assertTrue(test, msg)
        
        random.random = temp_random
    
    @staticmethod
    def test_3(unit, virus, patient):
        '''
        - Make sure random.seed() isn't used.
        - Use only the random.random() method
        - Make sure that a maxBirthProb of 1.0 and 
          popDensity of 0.0 reproduces
        - Make sure that a popDensity of 1.0 doesn't reproduce
        - Make sure that a non resistant virus doesn't reproduce
        '''
        temp_seed = random.seed
        def custom_seed(*args, **kwargs):
            msg = ('The random.seed() method can\'t be used ' + 
                   'in the code you submit to the grader.')
            unit.assertTrue(False, msg)
            return temp_seed(*args, **kwargs)
        random.seed = custom_seed
        
        unit.random_state = random.getstate()
        temp_random = random.random
        def custom_random(*args, **kwargs):
            test_random_state()
            result = temp_random(*args, **kwargs)
            unit.random_state = random.getstate()
            return result
        random.random = custom_random
        
        def test_random_state():
            test = random.getstate() == unit.random_state
            msg = ('Use no other method from the random ' + 
                   'module other than random().')
            unit.assertTrue(test, msg)
        
        virus.getMaxBirthProb()
        virus.getClearProb()
        virus.doesClear()
        if isinstance(virus, ResistantVirus):
            virus.isResistantTo('xorox')
            try:
                for _ in range(1024):
                    virus.reproduce(0.0, ['xorox'])
                msg = ('The reproduce() method must raise a ' + 
                       'NoChildException() exception when the ' + 
                       'virus isn\'t resistant to a drug.')
                unit.assertTrue(False, msg)
            except NoChildException:
                pass
            args = [0.0, []]
        else:
            args = [0.0]
        try:
            for _ in range(1024):
                virus.reproduce(*args)
        except NoChildException:
            msg = ('The reproduce() method should return a ' + 
                   virus.__class__.__name__ + ' object, when ' + 
                   'maxBirthProb is 1.0 and popDensity is 0.0.')
            unit.assertTrue(False, msg)
        try:
            args[0] = 1.0
            for _ in range(1024):
                virus.reproduce(*args)
            msg = ('The reproduce() method must raise a ' + 
                   'NoChildException() exception when ' + 
                   'the popDensity is 1.0.')
            unit.assertTrue(False, msg)
        except NoChildException:
            pass
        patient.getViruses()
        patient.getMaxPop()
        patient.getTotalPop()
        patient.update()
        if isinstance(patient, TreatedPatient):
            patient.addPrescription('xorox')
            patient.getPrescriptions()
            patient.getResistPop(['xorox'])
        test_random_state()
        
        random.seed = temp_seed
        random.random = temp_random
    
    @staticmethod
    def test_3_5(unit, patient):
        '''
        - Make sure not to add parentheses when catching 
          the exception on the update() method 
        '''
        unit.init_count = 0
        temp_init = NoChildException.__init__
        def custom_init(*args, **kwargs):
            unit.init_count += 1
            return temp_init(*args, **kwargs)
        NoChildException.__init__ = custom_init
        
        try:
            patient.update()
        except NoChildException:
            pass
        
        test = unit.init_count <= 1
        msg = ('Make sure not to add parentheses in front of the ' + 
               'exception class, when catching it on the update() method.')
        unit.assertTrue(test, msg)
        
        NoChildException.__init__ = temp_init
    
    @staticmethod
    def test_4(unit, patient):
        '''
        - Make sure the update() method uses both the doesClear() 
          and reproduce() methods
        - Check density parameter type when used in reproduce()
        - Make sure the correct viruses are cleared in update(), no mutation
        - Make sure the correct viruses are reproduced in update(), no mutation
        '''
        if isinstance(patient, TreatedPatient):
            temp_doesClear = ResistantVirus.doesClear
            temp_reproduce = ResistantVirus.reproduce
        else:
            temp_doesClear = SimpleVirus.doesClear
            temp_reproduce = SimpleVirus.reproduce
        
        unit.does_clear_count = []
        def custom_doesClear(*args, **kwargs):
            result = temp_doesClear(*args, **kwargs)
            if result:
                unit.does_clear_count += [args[0]]
            return result
        
        unit.reproduce_count = []
        def custom_reproduce(*args, **kwargs):
            test = isinstance(args[1], float)
            msg = ('On the update() method, the density variable supplied ' + 
                   'to the reproduce() method must be a float.')
            unit.assertTrue(test, msg)
            result = temp_reproduce(*args, **kwargs)
            if result:
                unit.reproduce_count += [result]
            return result
        
        if isinstance(patient, TreatedPatient):
            ResistantVirus.doesClear = custom_doesClear
            ResistantVirus.reproduce = custom_reproduce
        else:
            SimpleVirus.doesClear = custom_doesClear
            SimpleVirus.reproduce = custom_reproduce
        
        patient.update()

        test = unit.does_clear_count > 0 and unit.reproduce_count > 0
        msg = ('The update() method needs to use both ' + 
               'the doesClear() and reproduce() methods.')
        unit.assertTrue(test, msg)
        
        test = all(i not in patient.getViruses() 
                   for i in unit.does_clear_count)
        msg = ('Make sure you\'re clearing the correct viruses ' + 
               'on the update() method. Make sure you\'re not ' + 
               'mutating a list while iterating over it.')
        unit.assertTrue(test, msg)
        
        test = all(i in patient.getViruses() 
                   for i in unit.reproduce_count)
        msg = ('Make sure you\'re reproducing the correct viruses ' + 
               'on the update() method. Make sure you\'re not ' + 
               'mutating a list while iterating over it.')
        unit.assertTrue(test, msg)
        
        if isinstance(patient, TreatedPatient):
            ResistantVirus.doesClear = temp_doesClear
            ResistantVirus.reproduce = temp_reproduce
        else:
            SimpleVirus.doesClear = temp_doesClear
            SimpleVirus.reproduce = temp_reproduce
    
    @staticmethod
    def test_5(unit, virus):
        '''
        - Check type of SimpleVirus/Resistant __init__() 
          parameters when used in reproduce()
        '''
        if isinstance(virus, ResistantVirus):
            temp_init = ResistantVirus.__init__
        else:
            temp_init = SimpleVirus.__init__
        def custom_init(*args, **kwargs):
            test = isinstance(args[1], float) and isinstance(args[2], float)
            msg = ('When creating a ' + virus.__class__.__name__ + 
                   ' object in the reproduce() method both the ' + 
                   'maxBirthProb and clearProb variables must be floats.')
            unit.assertTrue(test, msg)
            return temp_init(*args, **kwargs)
        if isinstance(virus, ResistantVirus):
            ResistantVirus.__init__ = custom_init
            virus.reproduce(0.0, ['xorox'])
            ResistantVirus.__init__ = temp_init
        else:
            SimpleVirus.__init__ = custom_init
            virus.reproduce(0.0)
            SimpleVirus.__init__ = temp_init
    
    @staticmethod
    def test_6(unit, drugs, arguments):
        '''
        - Check number of Patient objects instantiated
        - Make sure the number of steps being used is 300
        '''
        if drugs:
            target_class = TreatedPatient
            func = simulationWithDrug
        else:
            target_class = Patient
            func = simulationWithoutDrug
        temp_update = target_class.update
        unit.count_update = 0
        def custom_update(*args, **kwargs):
            unit.count_update += 1
            return temp_update(*args, **kwargs)
        target_class.update = custom_update
        
        temp_init = target_class.__init__
        unit.count_init = 0
        def custom_init(*args, **kwargs):
            unit.count_init += 1
            return temp_init(*args, **kwargs)
        target_class.__init__ = custom_init
        
        temp_show = pylab.show
        def custom_show(*args, **kwargs):
            pass
        pylab.show = custom_show
        
        unit.trials = arguments[-1]
        func(*arguments)
        test = unit.count_update == 300 * unit.trials
        msg = ('You\'re calling the update() method in total ' + 
               str(unit.count_update) + ' times, when you should be ' + 
               'calling it 300 times for each trial(' + str(unit.trials) + 
               '), in total ' + str(300*unit.trials) + ' times.')
        unit.assertTrue(test, msg)
        test = unit.count_init == unit.trials
        msg = ('You\'re creating ' + str(unit.count_init) + ' Patient ' + 
               'objects, when you should be creating one for each trial, ' + 
               'in total ' + str(unit.trials) + ' Patient objects.')
        unit.assertTrue(test, msg)
        
        target_class.update = temp_update
        target_class.__init__ = temp_init
        pylab.show = temp_show
    
    @staticmethod
    def test_7(unit, drugs, arguments):
        '''
        - Make sure pylab functions are called
          pylab.plot()
          pylab.title()
          pylab.xlabel()
          pylab.ylabel()
          pylab.legend()
          pylab.show()
        - Make sure averages are floats
        '''
        if drugs:
            func = simulationWithDrug
        else:
            func = simulationWithoutDrug
        unit.count = {}
        temp_plot = pylab.plot
        def custom_plot(*args, **kwargs):
            unit.count['plot'] = True
            n_args = len(args)
            if n_args == 1:
                test = all(isinstance(i, float) for i in args[0])
            elif n_args == 2:
                if isinstance(args[1], str):
                    test = all(isinstance(i, float) for i in args[0])
                else:
                    test = all(isinstance(i, float) for i in args[1])
            else:
                test = all(isinstance(i, float) for i in args[1])
            msg = ('The averages you want to plot must be floats.')
            unit.assertTrue(test, msg)
            return temp_plot(*args, **kwargs)
        pylab.plot = custom_plot
        
        temp_title = pylab.title
        def custom_title(*args, **kwargs):
            unit.count['title'] = True
            return temp_title(*args, **kwargs)
        pylab.title = custom_title
        
        temp_xlabel = pylab.xlabel
        def custom_xlabel(*args, **kwargs):
            unit.count['xlabel'] = True
            return temp_xlabel(*args, **kwargs)
        pylab.xlabel = custom_xlabel
        
        temp_ylabel = pylab.ylabel
        def custom_ylabel(*args, **kwargs):
            unit.count['ylabel'] = True
            return temp_ylabel(*args, **kwargs)
        pylab.ylabel = custom_ylabel
        
        temp_legend = pylab.legend
        def custom_legend(*args, **kwargs):
            unit.count['legend'] = True
            return temp_legend(*args, **kwargs)
        pylab.legend = custom_legend
        
        temp_show = pylab.show
        def custom_show(*args, **kwargs):
            unit.count['show'] = True
            #return temp_show(*args, **kwargs)
        pylab.show = custom_show
        
        func(*arguments)
        for s in ['plot', 'title', 'xlabel', 'ylabel', 'legend', 'show']:
            test = s in unit.count
            msg = ('You didn\'t call pylab function ' + s + '().')
            unit.assertTrue(test, msg)
        
        pylab.plot = temp_plot
        pylab.title = temp_title
        pylab.xlabel = temp_xlabel
        pylab.ylabel = temp_ylabel
        pylab.legend = temp_legend
        pylab.show = temp_show


class Problem_2(unittest.TestCase):
    def test_1(self):
        '''
        - Check return type for all methods
        '''
        virus = SimpleVirus(1.0, 0.0)
        patient = Patient([virus], 256)
        CommonTests().test_1(self, virus, patient)
    
    def test_2(self):
        '''
        - One single call to random.random() in doesClear() and reproduce()
        '''
        virus = SimpleVirus(1.0, 0.5)
        CommonTests().test_2(self, virus)
    
    def test_3(self):
        '''
        - Make sure random.seed() isn't used.
        - Use only the random.random() method
        - Make sure that a maxBirthProb of 1.0 and 
          popDensity of 0.0 reproduces
        - Make sure that a popDensity of 1.0 doesn't reproduce
        '''
        virus = SimpleVirus(1.0, 0.0)
        patient = Patient([virus], 256)
        CommonTests.test_3(self, virus, patient)
    
    def test_3_5(self):
        '''
        - Make sure not to add parentheses when catching 
          the exception on the update() method 
        '''
        virus = SimpleVirus(0.0, 0.0)
        patient = Patient([virus], 256)
        CommonTests.test_3_5(self, patient)
    
    def test_4(self):
        '''
        - Make sure the update() method uses both the doesClear() 
          and reproduce() methods
        - Check density parameter type when used in reproduce()
        - Make sure the correct viruses are cleared in update(), no mutation
        - Make sure the correct viruses are reproduced in update(), no mutation
        '''
        viruses = [SimpleVirus(0.5, 0.5) for _ in range(128)]
        patient = Patient(viruses, 256)
        CommonTests.test_4(self, patient)
    
    def test_5(self):
        '''
        - Check type of SimpleVirus __init__() parameters 
          when used in reproduce()
        '''
        virus = SimpleVirus(1.0, 0.0)
        CommonTests.test_5(self, virus)    


class Problem_3(unittest.TestCase):
    def test_1(self):
        '''
        - Check number of Patient objects instantiated
        - Make sure the number of steps being used is 300
        '''
        arguments = [8, 16, 0.1, 0.05, 8]
        CommonTests.test_6(self, False, arguments)
    
    def test_2(self):
        '''
        - Make sure pylab functions are called
          pylab.plot()
          pylab.title()
          pylab.xlabel()
          pylab.ylabel()
          pylab.legend()
          pylab.show()
        - Make sure averages are floats
        '''
        arguments = [8, 16, 0.1, 0.05, 8]
        CommonTests.test_7(self, False, arguments)


class Problem_4(unittest.TestCase):
    def test_1(self):
        '''
        - Check return type for all methods
        '''
        virus = ResistantVirus(1.0, 0.0, {'xorox': True}, 0.0)
        patient = TreatedPatient([virus], 256)
        CommonTests().test_1(self, virus, patient)
    
    def test_2(self):
        '''
        - One single call to random.random() in doesClear() and reproduce()
        '''
        virus = ResistantVirus(1.0, 0.5, {'xorox': True}, 0.0)
        CommonTests().test_2(self, virus)
    
    def test_3(self):
        '''
        - Make sure random.seed() isn't used.
        - Use only the random.random() method
        - Make sure that a maxBirthProb of 1.0 and 
          popDensity of 0.0 reproduces
        - Make sure that a popDensity of 1.0 doesn't reproduce
        - Make sure that a non resistant virus doesn't reproduce
        '''
        virus = ResistantVirus(1.0, 0.0, {'xorox': False}, 0.0)
        patient = TreatedPatient([virus], 256)
        CommonTests.test_3(self, virus, patient)
    
    def test_3_5(self):
        '''
        - Make sure not to add parentheses when catching 
          the exception on the update() method 
        '''
        virus = ResistantVirus(0.0, 0.0, {'xorox': True}, 0.0)
        patient = TreatedPatient([virus], 256)
        CommonTests.test_3_5(self, patient)
    
    def test_4(self):
        '''
        - Make sure the update() method uses both the doesClear() 
          and reproduce() methods
        - Check density parameter type when used in reproduce()
        - Make sure the correct viruses are cleared in update(), no mutation
        - Make sure the correct viruses are reproduced in update(), no mutation
        '''
        viruses = [ResistantVirus(0.5, 0.5, {'xorox': True}, 0.0) 
                   for _ in range(128)]
        patient = TreatedPatient(viruses, 256)
        CommonTests.test_4(self, patient)
    
    def test_5(self):
        '''
        - Check type of ResistantVirus __init__() parameters 
          when used in reproduce()
        '''
        virus = ResistantVirus(1.0, 0.0, {'xorox': True}, 0.0)
        CommonTests.test_5(self, virus)
    
    def test_6(self):
        '''
        - Warn if not calling SimpleVirus.__init__() method
        - Warn if not calling Patient.__init__() method
        '''
        temp_virus_init = SimpleVirus.__init__
        self.virus_init_flag = False
        def custom_virus_init(*args, **kwargs):
            self.virus_init_flag = True
            return temp_virus_init(*args, **kwargs)
        SimpleVirus.__init__ = custom_virus_init
        
        temp_patient_init = Patient.__init__
        self.patient_init_flag = False
        def custom_patient_init(*args, **kwargs):
            self.patient_init_flag = True
            return temp_patient_init(*args, **kwargs)
        Patient.__init__ = custom_patient_init
        
        rv = ResistantVirus(0.0, 0.0, {'xorox': True}, 0.0)
        tp = TreatedPatient([rv], 256) #@UnusedVariable
        
        msg = ('Your ResistantVirus.__init__() method isn\'t calling ' + 
               'the SimpleVirus.__init__() method which would ' + 
               'initialize a good portion of the arguments you receive.')
        self.assertTrue(self.virus_init_flag, msg)
        msg = ('Your TreatedPatient.__init__() method isn\'t calling ' + 
               'the Patient.__init__() method which would initialize ' + 
               'a good portion of the arguments you receive.')
        self.assertTrue(self.patient_init_flag, msg)
    
    def test_7(self):
        '''
        - Make sure the ResistantVirus is created with a new dictionary and not 
          just an alias
        - Check if isResistantTo doesn't raise an exception when it receives 
          an unknown drug
        - Make sure drugs have no repeated values
        '''
        temp_init = ResistantVirus.__init__
        self.copy = None
        def custom_init(*args, **kwargs):
            self.copy = args[3]
            return temp_init(*args, **kwargs)
        
        original = {'xorox': True}
        rv = ResistantVirus(1.0, 0.0, original, 0.0)
        ResistantVirus.__init__ = custom_init
        offspring = rv.reproduce(0.0, original.keys()) #@UnusedVariable
        test = original is not self.copy
        msg = ('The ResistantVirus object you\'re creating with your ' + 
               'reproduce() method is using the same resistances ' + 
               'dictionary as its parent, you need to give the ' + 
               'offspring a new dictionary.')
        self.assertTrue(test, msg)
        
        try:
            rv.isResistantTo('unknown drug')
        except KeyError:
            msg = ('The isResistantTo() method is raising a KeyError ' + 
                   'exception when tested with a drug that doesn\'t exist.')
            self.assertTrue(False, msg)
            
        tp = TreatedPatient([rv], 256)
        tp.addPrescription('xorox')
        tp.addPrescription('xorox')
        test = tp.getPrescriptions() == ['xorox']
        msg = ('Make sure your drugs don\'t have repeated prescriptions.')
        self.assertTrue(test, msg)
        
        ResistantVirus.__init__ = temp_init
    
    def test_8(self):
        '''
        - Use getMaxBirthProb() method, don't access the variable directly
        - Use getClearProb() method, don't access the variable directly
        - Use getMaxPop() method instead of accessing the variable directly
        '''
        temp_birth_prob = SimpleVirus.getMaxBirthProb
        self.flag_birth = False
        def custom_birth_prob(*args, **kwargs):
            self.flag_birth = True
            return temp_birth_prob(*args, **kwargs)
        SimpleVirus.getMaxBirthProb = custom_birth_prob
        
        temp_clear_prob = SimpleVirus.getClearProb
        self.flag_clear = False
        def custom_clear_prob(*args, **kwargs):
            self.flag_clear = True
            return temp_clear_prob(*args, **kwargs)
        SimpleVirus.getClearProb = custom_clear_prob
        
        temp_max_pop = Patient.getMaxPop
        self.flag_max_pop = False
        def custom_max_pop(*args, **kwargs):
            self.flag_max_pop = True
            return temp_max_pop(*args, **kwargs)
        Patient.getMaxPop = custom_max_pop
        
        rv = ResistantVirus(1.0, 0.0, {'xorox': True}, 0.0)
        rv.reproduce(0.0, ['xorox'])
        tp = TreatedPatient([rv], 256)
        tp.update()
        
        msg = ('Use the getMaxBirthProb() method, don\'t ' + 
               'access the variable directly.')
        self.assertTrue(self.flag_birth, msg)
        msg = ('Use the getClearProb() method, don\'t ' + 
               'access the variable directly.')
        self.assertTrue(self.flag_clear, msg)
        msg = ('Use the getMaxPop() method, don\'t ' + 
               'access the variable directly.')
        self.assertTrue(self.flag_max_pop, msg)
        
        SimpleVirus.getMaxBirthProb = temp_birth_prob
        SimpleVirus.getClearProb = temp_clear_prob
        Patient.getMaxPop = temp_max_pop


class Problem_5(unittest.TestCase):
    def test_1(self):
        '''
        - Check number of Patient objects instantiated
        - Make sure the number of steps being used is 300
        '''
        arguments = [8, 16, 0.1, 0.05, {'xorox': True}, 0.005, 8]
        CommonTests.test_6(self, True, arguments)
    
    def test_2(self):
        '''
        - Make sure pylab functions are called
          pylab.plot()
          pylab.title()
          pylab.xlabel()
          pylab.ylabel()
          pylab.legend()
          pylab.show()
        - Make sure averages are floats
        '''
        arguments = [8, 16, 0.1, 0.05, {'xorox': True}, 0.005, 8]
        CommonTests.test_7(self, True, arguments)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_2))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_3))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_4))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_5))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.failfast = True
    runner.run(suite)