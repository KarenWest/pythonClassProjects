#for web solution below first solution
#from scipy import linspace, polyval, polyfit, sqrt, stats, randn
#from pylab import plot, title, show , legend
#for first attempt below
import pylab

a = 3.0
b = 2.0
c = 1.0
accuracy = 1.0e-1
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = pylab.array(yVals)
xVals = 2*pylab.array(xVals)
try:
    (ar,residuals, rank, singular_values, rcond) = pylab.polyfit(xVals, yVals, 3, accuracy, True)
    print('Linear regression using polyfit')
    print('parameters: a=%.2f b=%.2f c=%.2f\nregression: a=%.2f' % (a,b,c, ar))    
    print "residuals"
    print residuals
    print "rank"
    print rank
    print "singular values"
    print singular_values
    print "rcond"
    print rcond
except:
    print 'unable to fit'

'''
Test cases posted after due date of final (see correct solutions in other file):

 INCORRECT Hide output
Test 1

p = [-200.0] xVals = range(-50,50) yVals = numpy.polyval(p, xVals)

Your output:

    array([  2.72142191e-13,   7.60350526e-10,   1.57475896e-09,
             1.06429798e-06,   4.67636002e-06,  -6.18826811e-03,
            -9.81896194e-03,  -1.97848839e+02])

Correct output:

    array([-200.])

Test 2

yVals = [] xVals = range(-20, 20) for x in xVals: yVals.append(3*x**2 - 2*x + 1 + 0.1 * rand.random()) yVals = numpy.array(yVals) xVals = numpy.array(xVals)

Your output:

    array([  3.42340379e-08,   5.81071483e-06,   1.51513246e-05,
             2.77590380e-03,   4.09188190e-03,   1.28049110e+00,
            -4.02475745e+00,   9.05607312e+01])

Correct output:

    array([ 2.99991648, -2.00077149,  1.06476382])

Test 3

p = [3.0, -4.0, 2.0, -10.0] xVals = range(-50,50) yVals = numpy.polyval(p, xVals)

Your output:

    array([  1.37238376e-07,  -3.84767147e-07,   3.67376901e-04,
            -4.94517477e-04,   9.17637261e-01,   3.91903570e-01,
             1.43226277e+03,  -1.87920236e+03])

Correct output:

    array([ 3., -4.,  2., -10.])

Test 4

p = [3.0, 0.0, 0.0, 0.0, 0.0, 0.0] xVals = range(-50,50) yVals = numpy.polyval(p, xVals)

Your output:

    array([  4.44502083e-04,  -9.59231187e-04,   1.11052292e+00,
            -3.73099664e-01,   2.29937184e+03,   5.98374550e+03,
            -7.06546377e+05,  -2.30677582e+06])

Correct output:

    array([  3.00000000e+00,   1.01283193e-13,   8.97646763e-12,
            -1.56913735e-10,   7.44083713e-10,  -7.65872954e-08])
'''

'''
solution found on web

#Linear regression example
# This is a very simple example of using two scipy tools
# for linear regression, polyfit and stats.linregress
 
#Sample data creation
#number of points
accuracy = 1.0e-1
n=50
t=linspace(-5,5,n)
#parameters
a=0.8; b=-4
x=polyval([a,b],t)
#add some noise
xn=x+randn(n)
 
#Linear regressison -polyfit - polyfit can be used other orders polys
(ar,br)=polyfit(t,xn,1)
#(ar,br,residuals, rank, singular_values, rcond)=polyfit(t,xn,1,accuracy,True)
xr=polyval([ar,br],t)
#compute the mean square error
err=sqrt(sum((xr-xn)**2)/n)
 
print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a,b,ar,br,err))
 
#matplotlib ploting
title('Linear Regression Example')
plot(t,x,'g.--')
plot(t,xn,'k.')
plot(t,xr,'r.-')
legend(['original','plus noise', 'regression'])
 
show()
 
#Linear regression using stats.linregress
(a_s,b_s,r,tt,stderr)=stats.linregress(t,xn)
print('Linear regression using stats.linregress')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a,b,a_s,b_s,stderr))

print "residuals"
print residuals
print "rank"
print rank
print "singular values"
print singular_values
print "rcond"
print rcond
'''
