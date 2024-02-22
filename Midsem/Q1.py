# P452 Midsem Exam
# Name: Monu Kumar Choubey
# Roll: 2011090
# Stream: Int. M.Sc.
# Batch: 2020

from cProfile import label
import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf

g = "math.log(x/2) - math.sin(2.5*x)"
h = "1/x - (2.5*math.cos(2.5*x))"

res1 = rf.regfal(g,0.000001, 0.000001,1.5,2.5,1)

res2 = rf.newraph(g,h,0.000001,0.000001,1,1)
res3 = rf.newraph(g,h,0.000001,0.000001,1.5,1)
res4 = rf.newraph(g,h,0.000001,0.000001,2.5,1)


#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q1 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-6)\n\n" +"\nf(x) = log(x/2) - sin(5x/2)\n\n"+"Method         Result     No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q1 out.txt", "a")
fout.writelines("\nIntial Bracket: (1.5,2.5)\n\n")
for i in range(1, len(res1)): fout.writelines("Bisection :     "+str(float(f'{res1[i][0]:.7f}'))+"   "+str(float(f'{res1[i][1]:.6f}'))+"\n")
fout.writelines("\n\n")
fout.writelines("\n\nIntial Guess: 1\n\n")
for i in range(1, len(res2)): fout.writelines("Newton Raphson :     "+str(float(f'{res2[i][0]:.7f}'))+"   "+str(float(f'{res2[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Guess: 1.5\n\n")
for i in range(1, len(res3)): fout.writelines("Newton Raphson :     "+str(float(f'{res3[i][0]:.7f}'))+"   "+str(float(f'{res3[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Guess: 2.5\n\n")
for i in range(1, len(res4)): fout.writelines("Newton Raphson :     "+str(float(f'{res4[i][0]:.7f}'))+"   "+str(float(f'{res4[i][1]:.6f}'))+"\n")
fout.writelines("\nThe function has multiple roots.")
fout.writelines("\nAs observed, Newton Raphson converges to a root very quickly.\nAlso, different initial guesses for Newton Raphson may lead to different roots.")
fout.close()

#plotting the convergence (extra)


x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

for i in range(1, max(len(res1),len(res2),len(res3),len(res4))):
    if i < len(res2):
        x2.append(res2[i][1])
        y2.append(res2[i][0])
    if i < len(res3):
        x3.append(res3[i][1])
        y3.append(res3[i][0])
    if i < len(res4):
        x4.append(res4[i][1])
        y4.append(res4[i][0])
    if i < len(res1):
        x1.append(res1[i][1])
        y1.append(res1[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k', x3,y3, 'k*', x4,y4, 'k:')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Regula fal (1.5,2.5)','NewRaph: 1','NewRaph: 1.5','NewRaph: 2.5'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn")
plt.savefig("Q1 all.png")

fig, ax = plt.subplots()
plt.plot(x2,y2, 'k:', x3,y3, 'k', x4,y4, 'k--')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('NewRaph: 1','NewRaph: 1.5','NewRaph: 2.5'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn - Newton Raphson")
plt.savefig("Q1 Newraph.png")