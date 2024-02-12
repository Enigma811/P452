import copy
import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import de as de

# let the n = 3
# function
def gaussian_func(x):
    return (1 + x**4)**(0.5)
def gaussian_quadrature(a,b,x_gauss,w_gauss):
#         for n =3
#     x = [-0.861136,-0.339981,0.339981,0.861136] for n =3
#     w = [0.347855,0.652145,0.652145,0.347855]
    x = copy.copy(x_gauss)
    w = copy.copy(w_gauss)
    
    integral = 0
# Integrating the function by summing at the roots of the legendre function (0 - 1 limit )
    for i in range(len(x)):
        integral = integral + w[i]*gaussian_func((b-a)/2 * (x[i]) + (a+b)/2)
        
    integral =integral*(b-a)/2
    return integral

fn = "math.sqrt(1+x**(4))"
gn = "0"
x_gauss = [-0.861136,-0.339981,0.339981,0.861136] #  for n =3, hard coded the values of weights and roots for n = 3, legendre polynomials
w_gauss = [0.347855,0.652145,0.652145,0.347855]

res1 = gaussian_quadrature(0,1,x_gauss,w_gauss)
res2a = de.simp_integ(fn,gn,0,1,10)
res2b = de.simp_integ(fn,gn,0,1,20)
res2c = de.simp_integ(fn,gn,0,1,30)
res2d = de.simp_integ(fn,gn,0,1,40)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q2 out.txt", "w+")
fout.writelines("Numerical  Integration\n\n"+"Method            Result          N\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q2 out.txt", "a")
fout.writelines("\n\nGauss. quad"+"     "+str(float(f'{res1:.6f}'))+"         "+"3\n\n")
fout.writelines("Simpson"+"         "+str(float(f'{res2a:.6f}'))+"         "+str(10)+"\n\n")
fout.writelines("Simpson"+"         "+str(float(f'{res2b:.6f}'))+"         "+str(20)+"\n\n")
fout.writelines("Simpson"+"         "+str(float(f'{res2c:.6f}'))+"         "+str(30)+"\n\n")
fout.writelines("Simpson"+"         "+str(float(f'{res2d:.6f}'))+"         "+str(40)+"\n\n")
fout.close()

#plotting the convergence (extra)

x = [10,20,30,40]
y = [res2a, res2b, res2c, res2d]
print(y)
leg = ["Simpson"]
fig, ax = plt.subplots()
plt.scatter(x,y)
ax.yaxis.set_major_formatter('{x:.10f}')
plt.grid()
plt.legend(leg,loc='lower right')
plt.xlabel("N")
plt.ylabel("Estimate of Integral")
plt.title("Q2: Numerical Integration - sqroot(1+ x**4) (from 0 to 1)")
# plt.savefig("Q2.png")
plt.show()