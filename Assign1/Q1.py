import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf

g = "math.exp(-x)"

res1 = rf.fixpt(g,0.0001,1)
res2 = rf.fixpt(g,0.0001,0)
res3 = rf.fixpt(g,0.0001,-1)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q1 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-4)\n\n" +"\nexp(-x) - x = 0\n\nFixted point function: exp(-x)\n\n"+"Input       Result     No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q1 out.txt", "a")
fout.writelines("\n\n")
fout.writelines("1           "+str(float(f'{res1[len(res1)-1][0]:.5f}'))+"       "+str(res1[len(res1)-1][1])+"\n")
fout.writelines("\n")
fout.writelines("0           "+str(float(f'{res2[len(res2)-1][0]:.5f}'))+"       "+str(res2[len(res2)-1][1])+"\n")
fout.writelines("\n")
fout.writelines("-1          "+str(float(f'{res3[len(res3)-1][0]:.5f}'))+"       "+str(res3[len(res3)-1][1])+"\n")
fout.writelines("\n")

fout.close()

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
plt.legend(('Initial Val: 1','Initial Val: 0','Initial Val: -1'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn using Fixed point method")
plt.savefig("Q1.png")

