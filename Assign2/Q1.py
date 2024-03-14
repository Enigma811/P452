import re
from mypylib import random as rn
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

#breaking the augmented matrix
if len(in_mat)+1 == len(in_mat[0]):
    #extracting A & B
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = in_mat[i][(len(in_mat[0])-1)]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]
    
    #Cholesky
    
    a = mi.is_posdef(A)
    b = mi.is_sym(A)
    if a == True & b == True: #check for symmetric and pos def matrix
        A = mi.cholesky_deco(A)
        #forward substitution
        for i in range(0, len(A)):
            sum = 0
            for j in range(0,i): sum = sum + (A[i][j]*B[j])
            B[i] = (B[i] - sum)/A[i][i]
        #backward substitution
        A = mi.trans(A)
        for i in range(len(A)-1,-1,-1):
            sum2 = 0
            for j in range(i+1, len(A)): sum2 += A[i][j]*B[j]
            B[i] = (B[i] - sum2)/A[i][i]
        #file print module
        fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "w")
        fout.writelines("\nSolution by Cholesky decomposition\n" +"Solution: "+str(B)+"\n")
        fout.close()

    elif a==False:
        #file print module
        fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "w")
        fout.writelines("\nSolution by Cholesky decomposition\n" +"\nError: A is not positive definite in given input A|B, where AX=B\n")
        fout.close() 
    elif b==False:
        #file print module 
        fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "w")
        fout.writelines("\nSolution by Cholesky decomposition\n" +"\nError: A is not symmetric in given input A|B, where AX=B\n")
        fout.close()
    elif a==False & b==False:
        #file print module 
        fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "w")
        fout.writelines("\nSolution by Cholesky decomposition\n" +"\nError: A is not positive definite and symmetric in given input A|B, where AX=B\n")
        fout.close()
    

    #Gauss-Seidel
    res = mi.gsd(in_mat,0.000001,50,1)
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "a")
    fout.writelines("\nSolution by Gauss Seidel (Precision: 10^-6)\n"+"Number of iterations: " + str(res[len(res)-1])+"\nSolution: ")
    res.remove(res[len(res)-1])
    fout.writelines(str(res))

else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\A2\Q1 out.txt", "w")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()

