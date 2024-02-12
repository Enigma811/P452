import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import de as de

a = "(5*(x**2) - y)/(math.exp(x+y))"

res1 = de.RK4(a,0.0,1.0,0.5,20)
res2 = de.RK4(a,0.0,1.0,0.2,50)
res3 = de.RK4(a,0.0,1.0,0.05,200)
res4 = de.RK4(a,0.0,1.0,0.01,1000)


#plotting

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

for i in range(1, max(len(res1), len(res2), len(res3), len(res4))):
    if i < len(res1):
        x1.append(res1[i][0])
        y1.append(res1[i][1])
    if i < len(res2):
        x2.append(res2[i][0])
        y2.append(res2[i][1])
    if i < len(res3):
        x3.append(res3[i][0])
        y3.append(res3[i][1])
    if i < len(res4):
        x4.append(res4[i][0])
        y4.append(res4[i][1])

fig, ax = plt.subplots()
plt.scatter(x1,y1, c = 'red', marker = '.')
plt.scatter(x2,y2, c = 'blue', marker = '+', s=15)
plt.scatter(x3,y3, c = 'green', marker = 'o', s=1)
plt.scatter(x4,y4, c = 'black', marker = '*', s=3)
# ax.xaxis.set_major_locator(MultipleLocator(1))
# ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Step Size: 0.5','Step Size: 0.2','Step Size: 0.05', 'Step Size: 0.01'),loc='lower right')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Q3: Solving ODE using RK 4")
plt.savefig("Q3 ALL.png")

fig, ax = plt.subplots()
plt.scatter(x1,y1, c = 'red', marker = '.')
# ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Step Size: 0.5'),loc='lower right')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Q3: Solving ODE using RK 4")
plt.savefig("Q3 Step size = 0.5.png")

fig, ax = plt.subplots()
plt.scatter(x2,y2, c = 'blue', marker = '+', s=15)
plt.grid()
plt.legend(('Step Size: 0.2'),loc='lower right')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Q3: Solving ODE using RK 4")
plt.savefig("Q3 Step size = 0.2.png")

fig, ax = plt.subplots()
plt.scatter(x3,y3, c = 'green', marker = 'o', s=1)
plt.grid()
plt.legend(('Step Size: 0.05'),loc='lower right')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Q3: Solving ODE using RK 4")
plt.savefig("Q3 Step size = 0.05.png")

fig, ax = plt.subplots()
plt.scatter(x4,y4, c = 'black', marker = '*', s=3)
plt.grid()
plt.legend(('Step Size: 0.01'),loc='lower right')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Q3: Solving ODE using RK 4")
plt.savefig("Q3 Step size = 0.01.png")

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q3 out.txt", "w")
fout.writelines("Solution of ODE using RK4 method\n\n" +"\ny' = (5x**2 - y)/(exp(x+y))\n\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A1\Q3 out.txt", "a")
fout.writelines("\n\n")
fout.writelines("Step sixe = 0.5\n(x,y)\n")
fout.writelines(str(x1)+str(y1))

fout.writelines("\n\n")
fout.writelines("Step sixe = 0.2\n(x,y)\n")
fout.writelines(str(x2)+str(y2))

fout.writelines("\n\n")
fout.writelines("Step sixe = 0.05\n(x,y)\n")
fout.writelines(str(x3)+str(y3))

fout.writelines("\n\n")
fout.writelines("Step sixe = 0.01\n(x,y)\n")
fout.writelines(str(x4)+str(y4))
fout.close()

