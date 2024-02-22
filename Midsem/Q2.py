# P452 Midsem Exam
# Name: Monu Kumar Choubey
# Roll: 2011090
# Stream: Int. M.Sc.
# Batch: 2020

import math
import time
from mypylib import random as rn

from matplotlib import pyplot as plt

def bdODE(f1,f2,x0,y10,y11,y20,tol,con=0,h=0.1,n=100):
# 'f1' - (dy1/dx) 
# 'f2' - (dy2/dx) or (d^2y1/dx^2)
# 'x0' - independent variable - initial value
# 'y10' - y1 - initial value
# 'y11' - y1 - final value
# 'y20' - y2 or dy1/dx - initial value; "a" is placeholder - random initial guess in range 0,100
# 'tol' - tolerance
# 'con' - check to plot convergence; default - 0 = False, 1 = True
# 'h' - step size of independent variable
# 'n' - max iteration count
    
    # print(tol)
    x = x0 #initalizing independent variable
    xn = x0 #updating varible x
    y1 = y10 #initalizing dependent variable y1
    y1n = y1 #updating varible y1
    if y20 == "a": y2 = rn.myLCG(int(time.time())%100,100) #initalizing dependent variable y2 = dy1/dx
    else: y2 = y20
    y2n = y2 #updating varible y2
    ck_h=0 # tells whether high(overestimating) initial guess for y2 has been found; 0 - false, 1 - true
    ck_l=0 # tells whether low(underestimating) initial guess for y2 has been found; 0 - false, 1 - true
    ogl = 0 # low(underestimating) initial guess for y2
    ogh = 0 # high(overestimating) initial guess for y2
    y11l = 0 # corresponding low boundary value of y1
    y11h = 0 # corresponding high boundary value of y1
    CG = []

    for j in range(n):
        x = x0
        xn = x0
        y1 = y10
        y1n = y1

        res = [[x0,y10]]
        if j==0: cg = y2
        y2n = cg
        CG.append(cg)

        for i in range(1,n):
            x = x0 + (i-1)*h
            k1y1 = h*eval(f1)
            k1y2 = h*eval(f2)
            x = x + h/2
            y1 = y1n + (k1y1/2)
            y2 = y2n + (k1y2/2)
            k2y1 = h*eval(f1)
            k2y2 = h*eval(f2)
            y1 = y1n + (k2y1/2)
            y2 = y2n + (k2y2/2)
            k3y1 = h*eval(f1)
            k3y2 = h*eval(f2)
            y1 = y1n + (k2y1/2)
            y2 = y2n + (k2y2/2)
            x = x + h/2
            k4y1 = h*eval(f1)
            k4y2 = h*eval(f2)
            y1n = y1n + (k1y1 + 2*k2y1 + 2*k3y1 + k4y1)/6
            y2n = y2n + (k1y2 + 2*k2y2 + 2*k3y2 + k4y2)/6
        
            res.append([])
            # res[i] = res[i-1] + (h/6)*(t1 + 4*t2 + t3)
            res[(len(res)-1)].append(x0 + i*h)
            res[(len(res)-1)].append(y1n)
        
        s=20
        p = []
        q = []
        for i in range(len(res)):
            p.append(res[i][0])
            q.append(res[i][1])

        plt.scatter(p,q, marker='.', s=s)
        plt.grid()
        plt.legend(CG,loc='lower right')
        plt.xlabel("Position (x) (m)")
        plt.ylabel("Temperature (T(x) (deg C))")
        plt.title("Revision of estimated sol with intital guess for dT/dx")

        if (abs(res[len(res)-1][1] - y11) > tol) & (res[len(res)-1][1] < y11):
            if (ck_l == 1) & (res[len(res)-1][1]>y11l): 
                ogl=cg
                if ck_h==1:
                    # print("ogh + better ogl")
                    y11l = res[len(res)-1][1]
                    # print(ogl)
                    cg = ogl + ((ogh-ogl)*(y11-y11l))/(y11h - y11l)
                    y2 = cg
                else:
                    # print("no ogh, better ogl")
                    y11l = res[len(res)-1][1] 
                    cg += 0.1
                    y2=cg
            elif ck_l==0:
                # print("ogl ini") 
                ck_l=1
                ogl=cg
                y11l = res[len(res)-1][1]
                cg += 0.1
                y2=cg
            else:
                # print("worse ogl")
                cg = (ogl + ogh)/2
                y2=cg
            
        elif (abs(res[len(res)-1][1] - y11) > tol) & (res[len(res)-1][1] > y11):

            if (ck_h == 1) and (res[len(res)-1][1] < y11h): 
                ogh = cg
                if ck_l==1:
                    # print("ogl + better ogh")
                    y11h = res[len(res)-1][1]
                    # print(ogh)
                    cg = ogh + ((ogl-ogh)*(y11-y11h))/(y11h - y11l)
                    y2 = cg
                else:
                    # print("no ogl, better ogh") 
                    y11h = res[len(res)-1][1]
                    cg += 0.1
                    y2=cg
            elif ck_h==0:
                # print("ogh ini")
                ck_h=1
                ogh=cg
                y11h = res[len(res)-1][1] 
                cg += 0.1
                y2=cg
            else:
                # print("worse ogh")
                cg = (ogl + ogh)/2
                y2=cg
            
        elif abs(res[len(res)-1][1] - y11) < tol:
            if con == 1: plt.savefig("Q2 Convergence.png")
            del p
            del q
            del CG
            if y20 == "a": b="Random"
            else: b = y20
            return res,j,b
        # print(abs(res[len(res)-1][1] - y11))
    if j == n-1: 
        print("Error: Max Iteration count exceeded")
        print("Error Handling: Increase Max Iteration count or imput another inital guess for dy/dx")
        del p
        del q
        del CG
        return

# may give functions as input from file
fn = "y2"
gn = "0.01*(y1 - 20)"
s=20

pr,iter,ini = bdODE(fn,gn,0,40,200,"a",0.0001)

#plotting
p = []
q = []
y = []
for i in range(len(pr)):
            p.append(pr[i][0])
            q.append(pr[i][1])
            y.append(100)

fig, ax = plt.subplots()
plt.scatter(p,q, marker='.', s=s)
plt.plot(p,y,'k--',color='r')
plt.grid()
plt.legend(('Estimated sol','T = 100 deg C'),loc='lower right')
plt.xlabel("Position (x) (m)")
plt.ylabel("Temperature (T(x) (deg C))")
plt.title("1-D Heat conduction (d\N{SUPERSCRIPT TWO}T/dx\N{SUPERSCRIPT TWO} + \u03B1*(T\u2090 - T) = 0): Shooting Method (RK4)")
plt.savefig("Q2 \u03B1=0.02, T\u2090=20.png")
# plt.show()

del p
del q
del y

#finding the required position using Lagrange interpolation
dif = abs(pr[0][1]-100)
for i in range(len(pr)):
    if abs(pr[i][1]-100)<dif:
        dif = abs(pr[i][1]-100)
        pos = pr[i][0] + ((pr[i-1][0]-pr[i][0])*(100-pr[i][1]))/(pr[i][1]-pr[i-1][1])

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q2 out.txt", "w+")
fout.writelines("1-D Heat conduction (d^2T/dx^2 + alpha*(T_a - T) = 0): Shooting Method (RK4)\n\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q2 out.txt", "a")
fout.writelines("Precision: 10^-4\n\n")
fout.writelines("Boundary Values:\n")
fout.writelines("T(0) = 40, T(10) = 200\n\n")
fout.writelines("Assume that the left end of the rod is kept at origin.\n")
fout.writelines("Length of rod = 10m\n\n")
fout.writelines("Initial guess for dT/dx: "+str(ini)+"\n\n")
fout.writelines("Number of revisions to achieve given precision: "+str(iter)+"\n\n")
fout.writelines("Estimated position at which T(x) = 100: "+str(float(f'{pos:.5f}'))+" m\n")

