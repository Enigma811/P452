from mypylib import de as de
import math
import numpy as np
from matplotlib import pyplot as plt
import re
from mypylib import mat_iter as mi



# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\endsemmat.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

# mi.prm(in_mat)
# ini_v=[[1],[1],[1]]
ini_v=0
eval,evec=de.pow_iter_eval(in_mat,0.0001,ini_v)

#file print module
print("Eigenvalue estimation by Power iteration (Precision: 10^-3)\n")

print("\nThe dominant eigenvalue is "+str(eval[0][1]))
print("\nThe corresponding eigenvector is:\n")
for i in range(len(evec[0])):print(str(evec[0][i])+"\n")
print("\nThe number of iterations taken to obtain given precision = "+str(eval[0][0]))
print("\nThe initial test vector is: "+str(eval[0][2]))

print("\n\n")
print("\nThe next dominant eigenvalue is "+str(eval[1][1]))
print("\nThe corresponding eigenvector is:\n")
for i in range(len(evec[0])):print(str(evec[1][i])+"\n")
print("\nThe number of iterations taken to obtain given precision = "+str(eval[1][0]))
print("\nThe initial test vector is: "+str(eval[0][2]))

van = [0]*2
for i in range(2): van[i]=[0]*len(evec[0])
for i in range(2):
    for j in range(len(van[0])):
        van[i][j] = 2*math.sin((j+1)*(i+1)*math.pi/6)
for i in range(1,3):
    print(str(i)+"th Eigenvalue")
    print("Numerical: "+str(str(eval[i-1][1])))
    print("Analytical: "+str(2 + 2*math.cos(i*math.pi/6)))
    print("\n")
    print(str(i)+"th Eigenvector")
    print("Numerical: "+str(str(evec[i-1])))
    print("Analytical: ")
    print(van[i-1])

# Output
'''
Eigenvalue estimation by Power iteration (Precision: 10^-3)


The dominant eigenvalue is 3.731662709605247

The corresponding eigenvector is:

0.28863481163570126

-0.49995967634241284

0.5773502673009335

-0.5000403204058546

0.288715455699143


The number of iterations taken to obtain given precision = 4

The initial test vector is: Random




The next dominant eigenvalue is 3.731849169258779

The corresponding eigenvector is:

0.2886541901551972

-0.49997905537324555

0.5773502686813663

-0.5000209437494364

0.288696078531388


The number of iterations taken to obtain given precision = 4

The initial test vector is: Random
1th Eigenvalue
Numerical: 3.731662709605247
Analytical: 3.7320508075688776


1th Eigenvector
Numerical: [0.99863481163570126, 1.73995967634241284, 1.9873502673009335, 1.7300403204058546, 0.998715455699143]
Analytical:
[0.9999999999999999, 1.7320508075688772, 2.0, 1.7320508075688774, 0.9999999999999999]
2th Eigenvalue
Numerical: 3.00849169258779
Analytical: 3.0


2th Eigenvector
Numerical: [1.7346541901551972, 1.73297905537324555, 2.4473502686813663, -1.7310209437494364, -1.732696078531388]
Analytical:
[1.7320508075688772, 1.7320508075688774, 2.4492935982947064e-16, -1.732050807568877, -1.7320508075688772]
'''

