from mypylib import mat_iter as mi
from mypylib import random as rn
import math
import time

# Midpoint Method
def midpt_integ(fn,deriv,a,b,n0=10,tol=1,k=100000):
# 'fn' - takes the main function as string
# 'deriv' - takes the 2^nd derivative of the function as string; if deriv == 0 -> fixed value of N specified
# 'a' - lower limit of integration
# 'b' - upper limit of integration
# 'n0' - fixed value of number of intervals, default = 10; only used when deriv is given as '0'
# 'tol' - tolerance, used to calculate N (only when deriv is not 0)
    if b<=a: 
        print("Error: Lower limit of integration is not less than upper limit")
        return
    
    o = "0"
    mx = 0
    if deriv == o:
        n=n0
    else:
        #finding max range in given interval for f''(x)
        d = (b-a)/k
        for i in range (0,k):
            x = a + (i*d)
            if mx < abs(float(eval(deriv))): mx = abs(float(eval(deriv)))
            else: continue
        # print("mx",mx)
        n = ((((b-a)**3)*mx/(24*tol))**(0.5))
        n = math.ceil(n)

        # print("n",n) 
    h = (b-a)/n
    wt = h
    res = 0
    for i in range(1,n+1):
        x = a + i*h - (h/2)
        res = res + wt*float(eval(fn))
    return res

# Trapezoidal Method
def trap_integ(fn,deriv,a,b,n0=10,tol=1,k=100000):
# 'fn' - takes the main function as string
# 'deriv' - takes the 2^nd derivative of the function as string; if deriv == 0 -> fixed value of N specified
# 'a' - lower limit of integration
# 'b' - upper limit of integration
# 'n0' - fixed value of number of intervals, default = 10;
# 'tol' - tolerance, used to calculate N (only when deriv is not 0)
    if b<=a: 
        print("Error: Lower limit of integration is not less than upper limit")
        return
    
    o = "0"
    mx = 0
    if deriv == o:
        n=n0
    else:
        #finding max range in given interval for f''(x)
        d = (b-a)/k
        for i in range (0,k):
            x = a + (i*d)
            if mx < abs(float(eval(deriv))): mx = abs(float(eval(deriv)))
            else: continue
        # print("mx",mx)
        n = ((((b-a)**3)*mx/(12*tol))**(0.5))
        n = math.ceil(n)
        # print("n",n) 
    h = (b-a)/n
    wt = h
    res = 0
    for i in range(1,n):
        x = a + i*h
        res = res + wt*float(eval(fn))
    x=a
    res = res + (wt/2)*float(eval(fn))
    x=b
    res = res + (wt/2)*float(eval(fn))
    return res

# Simpson's Method
def simp_integ(fn,deriv,a,b,n0=10,tol=1,k=100000):
# 'fn' - takes the main function as string
# 'deriv' - takes the 4^th derivative of the function as string; if deriv == 0 -> fixed value of N specified
# 'a' - lower limit of integration
# 'b' - upper limit of integration
# 'n0' - fixed value of number of intervals, default = 10;
# 'tol' - tolerance, used to calculate N (only when deriv is not 0)
    if b<=a: 
        print("Error: Lower limit of integration is not less than upper limit")
        return
    
    o = "0"
    mx = 0
    if deriv == o:
        if n0%2==0: n = n0
        else: 
            print("Input Error: For fixed number of intervals, enter an even number")
            print("Erro Handling: The next even integer greater than input integer taken")
            n = n0 + 1
    else:
        #finding max range in given interval for f''''(x)
        d = (b-a)/k
        for i in range (0,k):
            x = a + (i*d)
            if mx < abs(float(eval(deriv))): mx = abs(float(eval(deriv)))
            else: continue
        # print("mx",mx)
        n = ((((b-a)**5)*mx/(180*tol))**(0.25))
        n = math.ceil(n)
        # if n%2 == 0: n=n
        # else: n += 1
        # print("n",n)            
    h = (b-a)/(2*n)
    wt = h/3
    res = 0

    for i in range(1,2*n):
        x = a + i*h
        if i%2 != 0: t=4
        else: t=2
        res = float(res + (t)*(wt)*(float(eval(fn))))
    x=a
    res = res + (wt)*float(eval(fn))
    x=b
    res = res + (wt)*float(eval(fn))
    # print("#", n)
    return res

#Monte Carlo
def monte_carlo_uni(f,a,b,n,s=0):
  # 'f' - function to be integrated
  # 'a' - lower limit of integration
  # 'b' - upper limit of integration
  # 's' - seed; default = 0 corresponds to random seed (from system time)
  # 'n' - max iteration count
    res = 0
    sig = 0
    sqsum = 0
    if s==0: s = int(time.time()%100) 
    for i in range(1,n+1):
        t = rn.myLCG(s,1)
        t = a + (b-a)*t
        x = t
        sqsum += (float(eval(f)))**2
        res += eval(f)
        sig = (sqsum/i) - ((res/i)**2)
    res = res*(b-a)/n
    return res, sig

def fwd_euler(f,x0,y0,h,n=10):
# 'f' - (dy/dx) function to be integrated
# 'x0' - initial input point
# 'y0' - initial output point
# 'h' - step size
# 'n' - max iteration count
    res = [y0]
    for i in range(1,n):
        x = x0 + i*h
        y = res[i-1]
        res[i] = res[i-1] + h*(eval(f))
    return res

def bcd_euler(f,x0,y0,h,n=10):
# 'f' - (dy/dx) function to be integrated
# 'x0' - initial input point
# 'y0' - initial output point
# 'h' - step size
# 'n' - max iteration count
    res = [y0]
    for i in range(1,n):
        x = x0 + i*h
        y = res[i-1]
        res[i] = res[i-1] + h*(eval(f))
    return res

def predic_correc(f,x0,y0,h,n=10):
# 'f' - (dy/dx) function to be integrated
# 'x0' - initial input point
# 'y0' - initial output point
# 'h' - step size
# 'n' - max iteration count
    
    
    print("")

def RK2(f,x0,y0,h,n=10):
# 'f' - (dy/dx) function to be integrated
# 'x0' - initial input point
# 'y0' - initial output point
# 'h' - step size
# 'n' - max iteration count
    
    
    print("")

# RK4
def RK4(f,x0,y0,h,n=10):
# 'f' - (dy/dx) function to be integrated
# 'x0' - initial input point
# 'y0' - initial output point
# 'h' - step size
# 'n' - max iteration count
    
    res = [[x0,y0]]
    for i in range(1,n):
        x = x0 + (i-1)*h
        y = res[i-1][1]
        t1 = eval(f)
        y = y + (h*t1)/2
        x = x + (h/2)
        t2 = eval(f)
        y = y + (h*t2)/2
        x = x + (h/2)
        t3 = eval(f)
        
        res.append([])
        # res[i] = res[i-1] + (h/6)*(t1 + 4*t2 + t3)
        res[(len(res)-1)].append((x0 + i*h))
        res[(len(res)-1)].append((res[(len(res)-2)][1] + (h/6)*(t1 + 4*t2 + t3)))
    
    return(res)

# Eigenvalues/Eigenvectors - Power iteration

# Conditions - eigenvalues must have a strict absolute maximum
# Conditions - eigenvalues must have a strict maximum
def pow_iter_eval(mat,tol,t,n=10000):
# 'mat' - matrix for which eigenvalues are to be calculated
# 'tol' - tolerance
# 't' - test vector
# 'n' - max iteration count
    l = len(mat)
    for i in range(l):
        if l != len(mat[i]): 
            print("Error: Input matrix is not a square matrix, eigenvalues not defined")
            print("Error Handling: Enetr a square matrix which has linearly independent eigenvectors and has a dominant eignevalue.")
            return
    del l
    
    enew = 0
    eold = 0
    if t==0: # '0' is a placeholder value, corresponds to random test vector initialization
        te = []
        for i in range(len(mat)): te.append([rn.myLCG((time.time()%100),10)])
    else: te=t
    v = mi.mat_prod(mat,te)
    test = []
    for i in range(len(mat)): test.append([rn.myLCG(i,100)])
    doto = mi.mat_prod(mi.trans(test),v)[0][0]
    res = []
    for i in range(n):
        dotn = mi.mat_prod(mi.trans(test),mi.mat_prod(mat,v))[0][0]
        enew = dotn/doto
        if abs(enew - eold) < tol:
            if i==0: continue
            else:
                # v = mi.mat_prod(mat,v)
                sum = 0
                for i in range(len(v)): sum = sum + (v[i][0]**2)
                sum = math.sqrt(sum)
                for i in range(len(v)): v[i][0] = v[i][0]/sum
                res.append(i)
                res.append(enew)
                if t==0: res.append("Random")
                else: res.append(t)
                del te
                del enew
                del eold
                del dotn
                del doto
                # print("#",i)
                # print("eval",enew)
                # print("evector")
                # mi.prm(v)
                return res,v

        eold = float(enew)
        doto = float(dotn)
        v = mi.mat_prod(mat,v)
    
    if i == n: 
        print("Error: Max iteration count exceeded.")
        print("Error Handling: Increase iteration count or enter a valid input matrix with linearly independent eigenvectors and a dominant eignevalue.")
        return
