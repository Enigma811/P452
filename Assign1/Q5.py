import copy
from matplotlib import pyplot as plt
import numpy as np
from inputsfile import*


def poisson_func(x,y,i,j):
    return x[i] * np.exp(y[j])

def boundary_cond(v,x_b,y_b):
    v[:, 0] = x_b                #U(x,0) = x    
    v[:, -1] = x_b * np.exp(1)   #U(x,1) = xe
    v[0, :] = 0                  #U(0,y) = 0
    v[-1, :] = 2 * np.exp(y_b)   #U(2,y) = 2*exp(y)
    return copy.copy(v)
    

def poisson(lx,ly,nx,ny,lx0,ly0,iterations):

    # Creating the grid
    x = np.linspace(0, 2, nx)
    y = np.linspace(0, 1, ny)
    hx = (lx-lx0)/(nx-1)               #lx0,ly0 are the initial boundaries coordinates.
    hy = (ly - ly0)/(ny-1)
    
    
    # Initialize the solution matrix of (nx) x (ny)
    u = np.zeros((nx, ny))

    # Set boundary conditions
    u = boundary_cond(u,x,y)           # Getting the boundary conditions

    # Solve the Poisson's equation using finite difference
    for k in range(iterations):
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u[i, j] = 0.5*((u[i+1, j] + u[i-1, j])*(hy**(2)) + (u[i, j+1] + u[i, j-1])*(hx**(2)) - (hx**(2) * hy**(2))* poisson_func(x,y,i,j))/(hx**(2)+ hy**(2))         

    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q5 out.txt", "w")
    fout.writelines("Solution of Poisson equation using finite difference method\n\n" +"\nu(0,y) = 0\nu(2,y) = 2*exp(y)\n\nu(x,0) = x\nu(x,1) = x*e\n\n")
    fout.close()
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q5 out.txt", "a")
    fout.writelines("\n\n")
    fout.writelines("Solution at grid points:\n")    
    for row in u:
        for value in row:
            fout.writelines(f"{value:.4f}")
        fout.writelines("\n")
        # print()
    fout.close()

    # Display the solution in a 3-D plot
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, u, cmap='viridis')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Solution')
    ax.set_title("Solution to Poisson's Equation")
    plt.savefig("Q5 Solution to Poisson equation.png")
    
    return x,y,u

poisson(2,1,6,6,0,0,1000)
# or can import input variables from inputsfile and use those as arguments


