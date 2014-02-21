#import pylab

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
'''
Test case output--see correct solutions other file (seemed to work for me?!)
 INCORRECT Hide output
Test: plotQuizzes()

Your output:

    Called generateScores...
    Successfully called pylab.hist with 7 bins.
    Successfully called pylab.title with label: Distribution of Scores
    Successfully called pylab.xlabel with label: Final Score
    Successfully called pylab.ylabel with label: Number of Trials
    Traceback (most recent call last):
      File "submission.py", line 54, in plotQuizzes
        labelPlot(numTrials)
      File "submission.py", line 45, in labelPlot
        xmin, xmax = pylab.xlim()
    AttributeError: 'module' object has no attribute 'xlim'

Correct output:

    Called generateScores...
    Successfully called pylab.hist with 7 bins.
    Successfully called pylab.xlabel with label: Final Score
    Successfully called pylab.ylabel with label: Number of Trials
    Successfully called pylab.title with label: Distribution of Scores
    Successfully called pylab.show
    None
'''
    
