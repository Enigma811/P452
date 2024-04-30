#

import math
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf

#fixed point function 1:
g = "0.05422 + 24.63/(5.95 + (6.254/x**2))"

res1 = rf.fixpt(g,0.0001,1)
res2 = rf.fixpt(g,0.0001,2)
res3 = rf.fixpt(g,0.0001,3)


print("Root(s) of nonlinear function (Tolerance 10^-4)\n\n" +"\nFixted point function: 0.05422 + 24.63/(5.95 + (6.254/x**2))\n\n"+"Input       Result     No. of iterations\n")
print("\n")
print("1           "+str(float(f'{res1[len(res1)-1][0]:.5f}'))+"       "+str(res1[len(res1)-1][1])+"\n")
# print("\n")
print("2           "+str(float(f'{res2[len(res2)-1][0]:.5f}'))+"       "+str(res2[len(res2)-1][1])+"\n")
# print("\n")
print("3          "+str(float(f'{res3[len(res3)-1][0]:.5f}'))+"       "+str(res3[len(res3)-1][1])+"\n")
print("\n")

#plotting the convergence (extra)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for i in range(1, max(len(res1),len(res2),len(res3))):
    if i < len(res1):
        x1.append(res1[i][1])
        y1.append(res1[i][0])
    if i < len(res2):
        x2.append(res2[i][1])
        y2.append(res2[i][0])
    if i < len(res3):
        x3.append(res3[i][1])
        y3.append(res3[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k', x3,y3)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Initial Val: 1','Initial Val: 2','Initial Val: 3'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Fixed point method: g(x) = 0.05422 + 24.63/(5.95 + (6.254/x**2))")
plt.savefig("Q2 f1.png")


#fixed point function 2:
g = "math.sqrt(6.254)/(math.sqrt((24.63/(x - 0.05422)) - 5.95))"

res1 = rf.fixpt(g,0.0001,1)
res2 = rf.fixpt(g,0.0001,2)
res3 = rf.fixpt(g,0.0001,3)

print("Root(s) of nonlinear function (Tolerance 10^-4)\n\n" +"\nFixted point function: math.sqrt(6.254)/(math.sqrt((24.63/(x - 0.05422)) - 5.95))\n\n"+"Input       Result     No. of iterations\n")
print("\n")
print("1           "+str(float(f'{res1[len(res1)-1][0]:.5f}'))+"       "+str(res1[len(res1)-1][1])+"\n")
# print("\n")
print("2           "+str(float(f'{res2[len(res2)-1][0]:.5f}'))+"       "+str(res2[len(res2)-1][1])+"\n")
# print("\n")
print("3          "+str(float(f'{res3[len(res3)-1][0]:.5f}'))+"       "+str(res3[len(res3)-1][1])+"\n")
print("\n")

#plotting the convergence (extra)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for i in range(1, max(len(res1),len(res2),len(res3))):
    if i < len(res1):
        x1.append(res1[i][1])
        y1.append(res1[i][0])
    if i < len(res2):
        x2.append(res2[i][1])
        y2.append(res2[i][0])
    if i < len(res3):
        x3.append(res3[i][1])
        y3.append(res3[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k', x3,y3)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Initial Val: 1','Initial Val: 2','Initial Val: 3'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Fixed point method: g(x) = math.sqrt(6.254)/(math.sqrt((24.63/(x - 0.05422)) - 5.95))")
plt.savefig("Q2 f2.png")

#Output
'''
Root(s) of nonlinear function (Tolerance 10^-4)


Fixted point function: 0.05422 + 24.63/(5.95 + (6.254/x**2))

Input       Result     No. of iterations



1           3.92993       7

2           3.92992       6

3          3.9299       5



Root(s) of nonlinear function (Tolerance 10^-4)


Fixted point function: math.sqrt(6.254)/(math.sqrt((24.63/(x - 0.05422)) - 5.95))

Input       Result     No. of iterations



1           0.18598       20

2           0.18598       21

3          0.18595       22



'''