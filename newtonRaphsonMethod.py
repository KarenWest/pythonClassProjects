#Summary - admittedly--had help from internet search here!  Have not learned all these tricks yet.
#    Solve for a zero of function using Newton-Raphson method 

#Usage
#    real = func(real)
#    real = funcd(real)
#    real = newton(func, funcd, real [, TOL=real]) 

#""" Ubiquitous Newton-Raphson algorithm for solving f(x) = 0 where a root is repeatedly estimated by x = x - f(x)/f'(x) 
#until |dx|/(1+|x|) < TOL is achieved. This termination condition is a compromise between |dx| < TOL, 
#if x is small |dx|/|x| < TOL, if x is large """ 

def newton(func, funcd, x, TOL=1e-6): 
# f(x)=func(x), f'(x)=funcd(x) 
    f, fd = func(x), funcd(x)
 
    count = 0 

    while 1: 
        dx = f / float(fd) 
        if abs(dx) < TOL * (1 + abs(x)): 
            return x - dx 
        x = x - dx 
        f, fd = func(x), funcd(x) 
        count = count + 1 
        print "newton(%d): x=%s, f(x)=%s" % (count, x, f)

#Even though it converges quadratically once a root has been "sighted", it does #not guarantee global convergence. 
#So, I use print statement to see intermediate results. 
