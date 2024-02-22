# P452 Midsem Exam
# Name: Monu Kumar Choubey
# Roll: 2011090
# Stream: Int. M.Sc.
# Batch: 2020

import math
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator


def one_dPDE(fx0,f0t,flt,ti,tf,nt,xi,xf,nx):
# 'fx0' - function of x at t=0
# 'f0t' - function of x = 0 (bdry condn at x=0)(may be a function of time)
# 'flt' - function of x = l (bdry condn at x=l)(may be a function of time)
# 'ti' - initial time point
# 'tf' - final time point
# 'nt' - number of time slices
# 'li' - initial space point
# 'lf' - final space point
# 'nl' - number of space slices
    if ti >= tf:
        print("Error: initial time is not less than final time")
        print("Error Handling: Input time coordinates with positive time interval")
        return
    ht = (tf - ti)/nt
    hx = (xf - xi)/nx
    al = ht/(hx**2)
    if al >= 0.4:
        if al>=0.5:
            print("Error: Stability condition not satisfied")
            print("Error Handling: Choose the number of time slices and space slices such that (del(t)/(del(x)^2)) < 0.5")
            return
        else: print("System alert: Weak stability for chosen number of time and space slices.")
    fig, ax = plt.subplots()

    arr = []
    x_i = []
    leg = ["t = "+str(ti), "t = "+str(ti + 5*ht), "t = "+str(ti + 10*ht), "t = "+str(ti + 50*ht), "t = "+str(ti + 100*ht), "t = "+str(ti + 200*ht), "t = "+str(ti + 500*ht), "t = "+str(ti + 800*ht), "t = "+str(ti + 1000*ht), "t = "+str(ti + 1500*ht), "t = "+str(tf)]
    for i in range(nx+1):
        x = xi + i*hx
        x_i.append(x)
        arr.append(eval(fx0)) 
    plt.plot(x_i,arr)
    for j in range(1,nt+1):
        # leg.append(ti+ht)
        arr[0] = (1-2*al)*arr[0] + al*arr[1]
        for i in range(1,(len(arr)-1)): arr[i] = al*(arr[i-1] + arr[i+1]) + (1-2*al)*arr[i]
        arr[len(arr)-1] = (1-2*al)*arr[len(arr)-1] + al*arr[len(arr)-2]
        # if (j%5 == 0) & (j<100): plt.plot(x_i,arr)
        # elif (j%50 == 0) & (j<500): plt.plot(x_i,arr)
        if(j == 5): plt.plot(x_i,arr)
        if(j == 10): plt.plot(x_i,arr)
        if(j == 50): plt.plot(x_i,arr)
        if(j == 100): plt.plot(x_i,arr)
        if(j == 200): plt.plot(x_i,arr)
        if(j == 500): plt.plot(x_i,arr)
        if(j == 800): plt.plot(x_i,arr)
        if(j == 1000): plt.plot(x_i,arr)
        if(j == 1500): plt.plot(x_i,arr)
        if(j == 2500): plt.plot(x_i,arr)
        # if(j%500 == 0): plt.plot(x_i,arr)
    plt.legend(leg, loc = 'lower right')
    plt.grid()
    plt.xlabel("Postion(Length) (m)")
    plt.ylabel("Temperature (T (deg C))")
    plt.title("1-D heat equation: Explicit finite difference method")
    del arr
    del x_i
    del leg
    # plt.show()
    plt.savefig("Q3 - T vs x for t in range ["+str(ti)+","+str(tf)+"].png")
    print("")

# may give functions as input from file
f = "300 if x==1 else 0" # function of x at t=0
g = "0"
h = "0"

one_dPDE(f,g,h,0,1,2500,0,2,20)
