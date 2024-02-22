# P452 Midsem Exam
# Name: Monu Kumar Choubey
# Roll: 2011090
# Stream: Int. M.Sc.
# Batch: 2020

import re
from mypylib import random as rn
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q5 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

if len(in_mat)+1 == len(in_mat[0]):
    #extracting A & B
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = in_mat[i][(len(in_mat[0])-1)]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]


    # doolittle LU Decomposition
    t = mi.doolittle_lu(A)

    l = [0]*len(t)
    u = [0]*len(t)
    for j in range(0, len(t)): #creating l and u
        l[j] = [0]*len(t)
        u[j] = [0]*len(t)
    for i in range(0, len(t)):
        for j in range(0, len(t)):
            if i==j:
                l[i][i] = 1
                u[i][i] = t[i][i]
            elif i>j: l[i][j] = t[i][j]
            else: u[i][j] = t[i][j]

    #forward substitution
    for i in range(0, len(l)):
        sum = 0
        for j in range(0,i): sum = sum + (l[i][j]*B[j])
        B[i] = (B[i] - sum)/l[i][i]
    
    #backward substitution
    for i in range(len(u)-1,-1,-1):
        sum2 = 0
        for j in range(i+1, len(u)): sum2 += u[i][j]*B[j]
        B[i] = (B[i] - sum2)/u[i][i]
    
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q5 out.txt", "w+")
    fout.writelines("\nSolution by doolittle_LU decomposition\n\n" +"Solution [a1 a2 a3 a4 a5 a6]: \n"+str(B)+"\n")
    fout.close()
    
else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q5 out.txt", "w")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()