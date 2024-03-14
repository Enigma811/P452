import re
from mypylib import random as rn
from mypylib import mat_iter as mi
import time

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q3 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

print(in_mat)

if len(in_mat)+1 == len(in_mat[0]):
    print("yes")
    #extracting A & B
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = [in_mat[i][(len(in_mat[0])-1)]]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]

    # Conjugate Gradient      
    tr = [0]*len(A)
    for i in range(0,len(A)): tr[i] = [0]
    # can set tr = 0 for random initial guess

    sol, arr = mi.conju_grad(A, B, tr, 0.0001)
    
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q3 out.txt", "w")
    fout.writelines("\nSolution by Conjugate Gradient Method\n" +"Solution: "+str(sol)+"\n")
    fout.close()
    # print(sol)
    # print("")
    # print(len(arr)) C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2

else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q3 out.txt", "w")
    fout.writelines("\nError: Invalid input\n\n")
    fout.close()