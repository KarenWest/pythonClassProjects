# 6.00 Problem Set 9

import random
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from ps8b import *

'''
From My mid term 2 solution for the quiz score histogram:
def labelPlot(numTrials):
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    
def plotQuizzes():
    # Your code here
    quizScores = []
    numTrials = 10000
    quizScores = generateScores(numTrials)
    pylab.hist(quizScores, bins=7)
    labelPlot(numTrials)
    pylab.show()


From SubPlot web page:
http://scipy-lectures.github.com/intro/matplotlib/matplotlib.html#subplots

With subplot you can arrange plots in a regular grid. You need to specify the number of rows
and columns and the number of the plot. Note that the gridspec command is a more powerful
alternative.

From: http://matplotlib.org/examples/pylab_examples/subplots_demo.html
Examples illustrating the use of plt.subplots().

This function creates a figure and a grid of subplots with a single call, while
providing reasonable control over how the individual plots are created.  For
very refined tuning of subplot creation, you can still use add_subplot()
directly on a new figure.


import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
#NOTE: np.linspace() used for non-integer ranges
#np.arange(start, stop, step) used for integer ranges
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

plt.close('all')

# Two subplots, the axes array is 1-d
f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(x, y)
axarr[0].set_title('Sharing X axis')
axarr[1].scatter(x, y)

From StackOverflow question:
I am having a hard time with putting in the parameters for the python subplot function.

What I want is to plot 4 graphs on a same image file with the following criteria

answer:
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,4)
ax3 = fig.add_subplot(4,2,5)
ax4 = fig.add_subplot(4,2,8)

fig.subplots_adjust(hspace=1)

plt.show()

With addtional information from another StackOverflow web page:
The formatting is done via the argument passed to 'add_subplot'. Notice it is (211) for the first plot and (212)
for the second. These mean: "two rows; one column, plot number one," and "two rows, one column, plot number two."

So for instance, if instead you wanted four plots on a page, in a 2x2 matrix configuration, you would call the
add_subplot method four times, passing in: (221), (222), (223), and (224), to create four plots on a page at
10, 2, 8, and 4 o'clock, respectively and in this order.

Another answer to this question:
Matplotlib provides several ways deal with the deliberate placement of plots on a single page; i think the best is gridspec, which i believe first appeared in the 1.0 release. The other two, by the way, are (i) directly indexing subplot and (ii) the new ImageGrid toolkit).

GridSpec works like grid-based packers in GUI toolkits used to placed widgets in a parent frame, so for that reason at least, it seems the easiest to use and the most configurable of the three placement techniques.

import numpy as NP
import matplotlib.pyplot as PLT
import matplotlib.gridspec as gridspec
import matplotlib.cm as CM

V = 10 * NP.random.rand(10, 10)  # some data to plot

fig = PLT.figure(1, (5., 5.))  # create the top-level container

gs = gridspec.GridSpec(4, 4)   # create a GridSpec object

# for the arguments to subplot that are identical across all four subplots,
# to avoid keying them in four times, put them in a dict 
# and let subplot unpack them
kx = dict(frameon = False, xticks = [], yticks = [])

ax1 = PLT.subplot(gs[0, 0], **kx)
ax3 = PLT.subplot(gs[2, 0], **kx)
ax2 = PLT.subplot(gs[1, 1], **kx)
ax4 = PLT.subplot(gs[3, 1], **kx)

for itm in [ax1, ax2, ax3, ax4] :
    itm.imshow(V, cmap=CM.jet, interpolation='nearest')

PLT.show()

Beyond just arranging the four plots in a 'checkerboard' configuration (per your Question), I have not tried to tune this configuration, but that's easy to do. E.g.,

# to change the space between the cells that hold the plots:
gs1.update(left=.1, right=,1, wspace=.1, hspace=.1)

# to create a grid comprised of varying cell sizes:
gs = gridspec.GridSpec(4, 4, width_ratios=[1, 2], height_ratios=[4, 1])
'''
#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    timeSteps = [300, 150, 75, 0]
    #timeSteps = [300]
    afterDrugSteps = 150
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonal':False}
    mutProb = 0.005
    xAxis = []
    yAxis = []
    binsForHistogram = 0
    
    #fig = plt.figure()
    fig = plt.figure("Simulation With Drugs")
    f,axarr = plt.subplots(4, sharex=True)
    #plt.legend(loc='upper left')
    # Four subplots, one for each num of steps where drug first introduced, before
    # continuing the next 150 steps, the axes array is 1-dimensional

    numStepsInList = len(timeSteps)
    stepNumIndex = 0
    #xmin = 0
    #ymin = 0
    
    for steps in timeSteps:
        totalSteps = steps + afterDrugSteps
        virusPopEachStepList = []
        virusPopEachStepList = simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, totalSteps, afterDrugSteps)
        #for virusPopulation in virusPopEachStepList:
            #print virusPopulation
        #pl.figure()
        xmax = int(max(virusPopEachStepList))
        xmin = int(min(virusPopEachStepList))
        #print "xmax " + str(xmax) + " xmin " + str(xmin)
        #determine bin numbers for histogram by ranges according to numTrials
        #if just one trial, that is the y axis, which must total 1,
        #then all the different virus populations must total 1 trial,
        #so y axis are percentages, perhaps in tenths.
        #Must divide bins to total on y axis the number of trials.
        #If you have 10 trials, the bins could be 10, so you have to
        #arrange the ranges of the virus populations to fit into 10 bins
        #etc - for 100 trials, that is too many bins for your histogram,
        #so want to perhaps divide virus populations into ranges that fit
        #into 10 bins, etc.

        #try something else (not the above way)
        binsForHistogram = 7
        virusPopInBins = [0] * binsForHistogram
        #now fit data into these 7 bins
        rangeIncrement = xmax / binsForHistogram
        #print "range increment " + str(rangeIncrement)
        #try ex: from mid term 2: low grade = 50 high grade = 95
        #range of x axis = 95-50 = 45
        #range increment for each bin = 95 / 7 = 13, plus 1 extra bin
        # if there is a remainder, so 14 would be range increment for ex.
        #0-14 - bin 1, 15-29 - bin 2, 30-44 - bin 3, 45-59 - bin 4,
        #60-74 - bin 5, 75-89 - bin 6, 90-95 - bin 7, so 7 bins fits the range
        binStepCounts =  [0] * binsForHistogram
        for avgVirusPop in virusPopEachStepList:
            #print "avgVirusPop " + str(avgVirusPop)
            if (avgVirusPop > 0) and (avgVirusPop <= (0 + rangeIncrement)):
                virusPopInBins[0] += avgVirusPop
                binStepCounts[0] += 1
            elif (avgVirusPop > rangeIncrement) and (avgVirusPop <= (rangeIncrement * 2)):
                virusPopInBins[1] += avgVirusPop
                binStepCounts[1] += 1
            elif (avgVirusPop > (rangeIncrement * 2)) and (avgVirusPop <= (rangeIncrement * 3)):
                virusPopInBins[2] += avgVirusPop
                binStepCounts[2] += 1
            elif (avgVirusPop > (rangeIncrement * 3)) and (avgVirusPop <= (rangeIncrement * 4)):
                virusPopInBins[3] += avgVirusPop
                binStepCounts[3] += 1
            elif (avgVirusPop > (rangeIncrement * 4)) and (avgVirusPop <= (rangeIncrement * 5)):
                virusPopInBins[4] += avgVirusPop
                binStepCounts[4] += 1
            elif (avgVirusPop > (rangeIncrement * 5)) and (avgVirusPop <= (rangeIncrement * 6)):
                virusPopInBins[5] += avgVirusPop
                binStepCounts[5] += 1
            else:
                virusPopInBins[6] += avgVirusPop
                binStepCounts[6] += 1
        #for i in binStepCounts:
            #print i
        #for avgVirusPop in virusPopInBins:
            #print avgVirusPop
        #get average virus population for this range over total steps
        for avgVirusPop in virusPopInBins:
            #print "avg virus pop in bins " + str(avgVirusPop)
            if (avgVirusPop > 0) and (avgVirusPop <= (0 + rangeIncrement)):
                if (binStepCounts[0] > 0):
                    #print "virus pop bin0 before div by steps " + str(virusPopInBins[0])
                    #print "num steps for bin 0 " + str(binStepCounts[0])
                    virusPopInBins[0] /= binStepCounts[0]
                    #print "virus pop after div by steps " + str(binStepCounts[0])
            elif (avgVirusPop > rangeIncrement) and (avgVirusPop <= (rangeIncrement * 2)):
                if (binStepCounts[1] > 0):
                    #print "virus pop bin1 before div by steps " + str(virusPopInBins[1])
                    #print "num steps for bin 1 " + str(binStepCounts[1])
                    virusPopInBins[1] /= binStepCounts[1]
                    #print "virus pop after div by steps " + str(binStepCounts[1])
            elif (avgVirusPop > (rangeIncrement * 2)) and (avgVirusPop <= (rangeIncrement * 3)):
                if (binStepCounts[2] > 0):
                    #print "virus pop bin2 before div by steps " + str(virusPopInBins[2])
                    #print "num steps for bin 2 " + str(binStepCounts[2])
                    virusPopInBins[2] /= binStepCounts[2]
                    #print "virus pop after div by steps " + str(binStepCounts[2])
            elif (avgVirusPop > (rangeIncrement * 3)) and (avgVirusPop <= (rangeIncrement * 4)):
                if (binStepCounts[3] > 0):
                    #print "virus pop bin3 before div by steps " + str(virusPopInBins[3])
                    #print "num steps for bin 3 " + str(binStepCounts[3])
                    virusPopInBins[3] /= binStepCounts[3]
                    #print "virus pop after div by steps " + str(binStepCounts[3])
            elif (avgVirusPop > (rangeIncrement * 4)) and (avgVirusPop <= (rangeIncrement * 5)):
                if (binStepCounts[4] > 0):
                    #print "virus pop bin4 before div by steps " + str(virusPopInBins[4])
                    #print "num steps for bin 4 " + str(binStepCounts[4])
                    virusPopInBins[4] /= binStepCounts[4]
                    #print "virus pop after div by steps " + str(binStepCounts[4])
            elif (avgVirusPop > (rangeIncrement * 5)) and (avgVirusPop <= (rangeIncrement * 6)):
                if (binStepCounts[5] > 0):
                    #print "virus pop bin5 before div by steps " + str(virusPopInBins[5])
                    #print "num steps for bin 5 " + str(binStepCounts[5])
                    virusPopInBins[5] /= binStepCounts[5]
                    #print "virus pop after div by steps " + str(binStepCounts[5])
            else:
                if (binStepCounts[6] > 0):
                    #print "virus pop bin6 before div by steps " + str(virusPopInBins[6])
                    #print "num steps for bin 6 " + str(binStepCounts[6])
                    virusPopInBins[6] /= binStepCounts[6]
                    #print "virus pop after div by steps " + str(binStepCounts[6])
                                                  
        #yAxisArr = np.arange(0, numTrials, 0.2)        
        #lenx = xmax - xmin
        #ymax = 0
        #for trial in range(numTrials):
            #if virusPopEachStepList[trial] == xmax:
                #ymax += 1
        #print "numTrials " + str(numTrials)
        #leny = ymax - ymin

        #axarr[stepNumIndex] = pl.hist(virusPopEachStepList, bins = lenx/10)
        #NOTE: np.linspace() used for non-integer ranges
        #np.arange(start, stop, step) used for integer ranges
        #xAxis = range(int(lenx))
        #yAxis = range(leny)
        #plt.plot(xAxis, yAxis, color='blue')
        if (stepNumIndex == 0):
            axarr[0] = fig.add_subplot(2,2,1)
            axarr[0].set_title('Drug at Time Step 300')
            #print "plotting time step 300 plot"
        elif (stepNumIndex == 1):
            axarr[1] = fig.add_subplot(2,2,2)
            axarr[1].set_title('Drug at Time Step 150')
            #print "plotting time step 150 plot"
        elif (stepNumIndex == 2):
            axarr[2] = fig.add_subplot(2,2,3)
            axarr[2].set_title('Drug at Time Step 75')
            #print "plotting time step 75 plot"
        elif (stepNumIndex == 3):
            axarr[3] = fig.add_subplot(2,2,4)
            axarr[3].set_title('Drug at Time Step 0')
            #print "plotting time step 0 plot"
        fig.subplots_adjust(hspace=1)
        ax = axarr[stepNumIndex]
        ax.set_xlabel('Final Virus Populations')
        ax.set_ylabel('Number of Trials')
        #ax.bar(xAxis, yAxis)
        
        ax.hist(virusPopInBins, bins = binsForHistogram)
        xmin, xmax = pl.xlim(0, xmax)
        ymin, ymax = pl.ylim(0,numTrials)
        #xmin, xmax = pl.xlim()
        #ymin, ymax = pl.ylim()

        #for x, y in zip(xAxis, yAxis):
            #ax.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        #ax.set_xticks(max(virusPopEachStepList))
        #ax.set_yticks(numTrials)
        #pl.legend()
        stepNumIndex += 1
    #print "calling plt.show()"
    plt.show()
        
#test
simulationDelayedTreatment(100)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    beforeDrug1Steps = 150
    afterDrug1Steps = [300, 150, 75, 0]
    #timeSteps = [300]
    afterBothDrugSteps = 150
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonal':False}
    mutProb = 0.005
    xAxis = []
    yAxis = []
    binsForHistogram = 0
    
    #fig = plt.figure()
    fig = plt.figure("Simulation With 2 Drugs")
    f,axarr = plt.subplots(4, sharex=True)
    #plt.legend(loc='upper left')
    # Four subplots, one for each num of steps where drug first introduced, before
    # continuing the next 150 steps, the axes array is 1-dimensional

    numStepsInList = len(afterDrug1Steps)
    stepNumIndex = 0
    #xmin = 0
    #ymin = 0
    
    for steps in afterDrug1Steps:
        totalSteps = beforeDrug1Steps + steps + afterBothDrugSteps
        virusPopEachStepList = []
        virusPopEachStepList = simulationWith2Drugs(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, totalSteps, beforeDrug1Steps, steps)
        #for virusPopulation in virusPopEachStepList:
            #print virusPopulation
        #pl.figure()
        xmax = int(max(virusPopEachStepList))
        xmin = int(min(virusPopEachStepList))
        #print "xmax " + str(xmax) + " xmin " + str(xmin)
        #determine bin numbers for histogram by ranges according to numTrials
        #if just one trial, that is the y axis, which must total 1,
        #then all the different virus populations must total 1 trial,
        #so y axis are percentages, perhaps in tenths.
        #Must divide bins to total on y axis the number of trials.
        #If you have 10 trials, the bins could be 10, so you have to
        #arrange the ranges of the virus populations to fit into 10 bins
        #etc - for 100 trials, that is too many bins for your histogram,
        #so want to perhaps divide virus populations into ranges that fit
        #into 10 bins, etc.

        #try something else (not the above way)
        binsForHistogram = 7
        virusPopInBins = [0] * binsForHistogram
        #now fit data into these 7 bins
        rangeIncrement = xmax / binsForHistogram
        #print "range increment " + str(rangeIncrement)
        #try ex: from mid term 2: low grade = 50 high grade = 95
        #range of x axis = 95-50 = 45
        #range increment for each bin = 95 / 7 = 13, plus 1 extra bin
        # if there is a remainder, so 14 would be range increment for ex.
        #0-14 - bin 1, 15-29 - bin 2, 30-44 - bin 3, 45-59 - bin 4,
        #60-74 - bin 5, 75-89 - bin 6, 90-95 - bin 7, so 7 bins fits the range
        binStepCounts =  [0] * binsForHistogram
        for avgVirusPop in virusPopEachStepList:
            #print "avgVirusPop " + str(avgVirusPop)
            if (avgVirusPop > 0) and (avgVirusPop <= (0 + rangeIncrement)):
                virusPopInBins[0] += avgVirusPop
                binStepCounts[0] += 1
            elif (avgVirusPop > rangeIncrement) and (avgVirusPop <= (rangeIncrement * 2)):
                virusPopInBins[1] += avgVirusPop
                binStepCounts[1] += 1
            elif (avgVirusPop > (rangeIncrement * 2)) and (avgVirusPop <= (rangeIncrement * 3)):
                virusPopInBins[2] += avgVirusPop
                binStepCounts[2] += 1
            elif (avgVirusPop > (rangeIncrement * 3)) and (avgVirusPop <= (rangeIncrement * 4)):
                virusPopInBins[3] += avgVirusPop
                binStepCounts[3] += 1
            elif (avgVirusPop > (rangeIncrement * 4)) and (avgVirusPop <= (rangeIncrement * 5)):
                virusPopInBins[4] += avgVirusPop
                binStepCounts[4] += 1
            elif (avgVirusPop > (rangeIncrement * 5)) and (avgVirusPop <= (rangeIncrement * 6)):
                virusPopInBins[5] += avgVirusPop
                binStepCounts[5] += 1
            else:
                virusPopInBins[6] += avgVirusPop
                binStepCounts[6] += 1
        #for i in binStepCounts:
            #print i
        #for avgVirusPop in virusPopInBins:
            #print avgVirusPop
        #get average virus population for this range over total steps
        for avgVirusPop in virusPopInBins:
            #print "avg virus pop in bins " + str(avgVirusPop)
            if (avgVirusPop > 0) and (avgVirusPop <= (0 + rangeIncrement)):
                if (binStepCounts[0] > 0):
                    #print "virus pop bin0 before div by steps " + str(virusPopInBins[0])
                    #print "num steps for bin 0 " + str(binStepCounts[0])
                    virusPopInBins[0] /= binStepCounts[0]
                    #print "virus pop after div by steps " + str(binStepCounts[0])
            elif (avgVirusPop > rangeIncrement) and (avgVirusPop <= (rangeIncrement * 2)):
                if (binStepCounts[1] > 0):
                    #print "virus pop bin1 before div by steps " + str(virusPopInBins[1])
                    #print "num steps for bin 1 " + str(binStepCounts[1])
                    virusPopInBins[1] /= binStepCounts[1]
                    #print "virus pop after div by steps " + str(binStepCounts[1])
            elif (avgVirusPop > (rangeIncrement * 2)) and (avgVirusPop <= (rangeIncrement * 3)):
                if (binStepCounts[2] > 0):
                    #print "virus pop bin2 before div by steps " + str(virusPopInBins[2])
                    #print "num steps for bin 2 " + str(binStepCounts[2])
                    virusPopInBins[2] /= binStepCounts[2]
                    #print "virus pop after div by steps " + str(binStepCounts[2])
            elif (avgVirusPop > (rangeIncrement * 3)) and (avgVirusPop <= (rangeIncrement * 4)):
                if (binStepCounts[3] > 0):
                    #print "virus pop bin3 before div by steps " + str(virusPopInBins[3])
                    #print "num steps for bin 3 " + str(binStepCounts[3])
                    virusPopInBins[3] /= binStepCounts[3]
                    #print "virus pop after div by steps " + str(binStepCounts[3])
            elif (avgVirusPop > (rangeIncrement * 4)) and (avgVirusPop <= (rangeIncrement * 5)):
                if (binStepCounts[4] > 0):
                    #print "virus pop bin4 before div by steps " + str(virusPopInBins[4])
                    #print "num steps for bin 4 " + str(binStepCounts[4])
                    virusPopInBins[4] /= binStepCounts[4]
                    #print "virus pop after div by steps " + str(binStepCounts[4])
            elif (avgVirusPop > (rangeIncrement * 5)) and (avgVirusPop <= (rangeIncrement * 6)):
                if (binStepCounts[5] > 0):
                    #print "virus pop bin5 before div by steps " + str(virusPopInBins[5])
                    #print "num steps for bin 5 " + str(binStepCounts[5])
                    virusPopInBins[5] /= binStepCounts[5]
                    #print "virus pop after div by steps " + str(binStepCounts[5])
            else:
                if (binStepCounts[6] > 0):
                    #print "virus pop bin6 before div by steps " + str(virusPopInBins[6])
                    #print "num steps for bin 6 " + str(binStepCounts[6])
                    virusPopInBins[6] /= binStepCounts[6]
                    #print "virus pop after div by steps " + str(binStepCounts[6])
                                                  
        #yAxisArr = np.arange(0, numTrials, 0.2)        
        #lenx = xmax - xmin
        #ymax = 0
        #for trial in range(numTrials):
            #if virusPopEachStepList[trial] == xmax:
                #ymax += 1
        #print "numTrials " + str(numTrials)
        #leny = ymax - ymin

        #axarr[stepNumIndex] = pl.hist(virusPopEachStepList, bins = lenx/10)
        #NOTE: np.linspace() used for non-integer ranges
        #np.arange(start, stop, step) used for integer ranges
        #xAxis = range(int(lenx))
        #yAxis = range(leny)
        #plt.plot(xAxis, yAxis, color='blue')
        if (stepNumIndex == 0):
            axarr[0] = fig.add_subplot(2,2,1)
            axarr[0].set_title('Drug2 at Time Step 300')
            #print "plotting time step 300 plot"
        elif (stepNumIndex == 1):
            axarr[1] = fig.add_subplot(2,2,2)
            axarr[1].set_title('Drug2 at Time Step 150')
            #print "plotting time step 150 plot"
        elif (stepNumIndex == 2):
            axarr[2] = fig.add_subplot(2,2,3)
            axarr[2].set_title('Drug2 at Time Step 75')
            #print "plotting time step 75 plot"
        elif (stepNumIndex == 3):
            axarr[3] = fig.add_subplot(2,2,4)
            axarr[3].set_title('Drug2 at Time Step 0')
            #print "plotting time step 0 plot"
        fig.subplots_adjust(hspace=1)
        ax = axarr[stepNumIndex]
        ax.set_xlabel('Final Virus Populations')
        ax.set_ylabel('Number of Trials')
        #ax.bar(xAxis, yAxis)
        
        ax.hist(virusPopInBins, bins = binsForHistogram)
        xmin, xmax = pl.xlim(0, xmax)
        ymin, ymax = pl.ylim(0,numTrials)
        #xmin, xmax = pl.xlim()
        #ymin, ymax = pl.ylim()

        #for x, y in zip(xAxis, yAxis):
            #ax.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        #ax.set_xticks(max(virusPopEachStepList))
        #ax.set_yticks(numTrials)
        #pl.legend()
        stepNumIndex += 1
    #print "calling plt.show()"
    plt.show()
        
#test
simulationTwoDrugsDelayedTreatment(10)

