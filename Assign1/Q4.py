# Importing required libraries
 
import numpy as np
from mypylib import mat_iter as mi
import matplotlib.pyplot as plt

def heat_eqn(temp, alpha, Nx, Lt, Nt, xn, x0 = 0):

    Nt=int(Nt)
    Lx = xn-x0
    ht = Lt / Nt
    # print("ht:", ht)
    hx = Lx / Nx
    # print("hx:", hx)
    alpha = ht * alpha / (hx**2)
    print("alpha:", alpha)

    # Testing stability
    if alpha > 0.5:
        raise ValueError("Stability condition: D*ht/hx^2 <= 0.5 not met")
    
    # Creating the master array containing function's (u(x,t)) value at all grid points
    res = [[]]
    
    # initializing the position dependent vector at j(=0)^th time
    ini = [[]]
    for i in range(Nx+1):
        ini[len(ini)-1].append(temp(x0 + i*hx))
        if i == Nx: break
        ini.append([])
    
    xcurr=ini
    
    # Defining Identity matrix (of suitable order)
    I = [[]]
    for i in range(Nx):I.append([])
    for i in range(Nx+1):
        for j in range(Nx+1):I[i].append(0)

    for i in range(Nx+1):I[i][i] = 1

    # Defining the B matrix
    B = [[]]
    for i in range(Nx):B.append([])
    for i in range(Nx+1):
        for j in range(Nx+1):B[i].append(0)

    for i in range(Nx+1):
        B[i][i] = 2
        if i==0: B[i][i+1]=-1
        elif i==Nx: B[i][i-1]=-1
        else:
            B[i][i+1]=-1
            B[i][i-1]=-1
    
    P = mi.mat_add(I,mi.scale_mat(B,2*alpha))
    Q = mi.mat_add(I,mi.scale_mat(B,-1*alpha))
    
    #Inverting P = (2*I + alpha*B)
    s = np.linalg.inv(P)
    for j in range(Nx+1):
        for k in range(Nx+1): P[j][k]=s[j][k]
    
    # getting the evolution matrix operator
    P = mi.mat_prod(P,Q)

    # Storing the intital value u(x,t=0) in the result array
    for i in range(Nx+1):
        res[len(res)-1].append(ini_cond(x0 + i*hx))
    
    # Iterative solution for u(x,t)
    for i in range(Nt+1):
        xcurr = mi.mat_prod(P,xcurr)
        res.append([])
        for k in range(Nx+1): res[len(res)-1].append(xcurr[k][0])
    
    return res


def ini_cond(x):
    return 4*x - (x**2)/2

L = 8
T = 1
alpha = 4
Nx = 100
Nt = 2000
A = heat_eqn(ini_cond, alpha, Nx, T, Nt, L)



#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q4 out.txt", "w")
fout.writelines("Solution of heat equation using Crank Nicolson method\n\n" +"\nu_t = 4*u_xx\n\nu(0,t) = u(8,t)=0\nu(x,0) = 4*x - (x**2)/2\n\n"+"Alpha       Result (u(x,t)) at t=1 s\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q4 out.txt", "a")
fout.writelines("\n\n")
fout.writelines(str(float(f'{(4*(1/2000)/((8/100)**2)):.5f}'))+"       "+str(A[len(A)-1])+"\n\n")
fout.close()


# Plot 

# lines = range(1, Nt*10, 1500)
x = np.linspace(0, L, Nx+1)
y0 = A[0]
y1 = A[1]
y10 = A[10]
y100 = A[100]
y1000 = A[1000]

plt.xlabel("x")
plt.ylabel("Temperature")
plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y10)
plt.plot(x, y100)
plt.plot(x, y1000)
plt.grid()
plt.legend(("t ="+str(0*T/Nt),"t ="+str(1*T/Nt),"t ="+str(10*T/Nt),"t ="+str(100*T/Nt),"t ="+str(1000*T/Nt)),loc='lower right')
plt.title("Temperature distribution over time")
plt.savefig("Q4 \u03B1="+str(4*(1/2000)/((8/100)**2))+".png")
plt.close()


alpha = 4
Nx = 100
Nt = 10000
A = heat_eqn(ini_cond, alpha, Nx, T, Nt, L)

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q4 out.txt", "a")
fout.writelines(str(float(f'{(4*(1/10000)/((8/100)**2)):.5f}'))+"       "+str(A[len(A)-1])+"\n\n")
fout.close()

# Plot 

# lines = range(1, Nt*10, 1500)
x = np.linspace(0, L, Nx+1)
y0 = A[0]
y1 = A[1]
y10 = A[10]
y100 = A[100]
y1000 = A[1000]
y5000 = A[5000]

plt.xlabel("x")
plt.ylabel("Temperature")
plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y10)
plt.plot(x, y100)
plt.plot(x, y1000)
plt.plot(x, y5000)
plt.grid()
plt.legend(("t ="+str(0*T/Nt),"t ="+str(1*T/Nt),"t ="+str(10*T/Nt),"t ="+str(100*T/Nt),"t ="+str(1000*T/Nt),"t ="+str(5000*T/Nt)),loc='lower right')
plt.title("Temperature distribution over time")
plt.savefig("Q4 \u03B1="+str(4*(1/10000)/((8/100)**2))+".png")
plt.close()

alpha = 4
Nx = 100
Nt = 20000
A = heat_eqn(ini_cond, alpha, Nx, T, Nt, L)

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q4 out.txt", "a")
fout.writelines(str(float(f'{(4*(1/20000)/((8/100)**2)):.5f}'))+"       "+str(A[len(A)-1])+"\n\nThe effect of alpha is observed in how quickly the diffusion takes place.\nLinalg module (from numpy) has been used for matrix inversion")
fout.close()

# Plot 

# lines = range(1, Nt*10, 1500)
x = np.linspace(0, L, Nx+1)
y0 = A[0]
y1 = A[1]
y10 = A[10]
y100 = A[100]
y1000 = A[1000]
y10000 = A[10000]

plt.xlabel("x")
plt.ylabel("Temperature")
plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y10)
plt.plot(x, y100)
plt.plot(x, y1000)
plt.plot(x, y10000)
plt.grid()
plt.legend(("t ="+str(0*T/Nt),"t ="+str(1*T/Nt),"t ="+str(10*T/Nt),"t ="+str(100*T/Nt),"t ="+str(1000*T/Nt),"t ="+str(10000*T/Nt)),loc='lower right')
plt.title("Temperature distribution over time")
plt.savefig("Q4 \u03B1="+str(4*(1/20000)/((8/100)**2))+".png")