import math
import time

from mypylib import random as rn

#printing matrix
def prm(x):
  for i in range(0, len(x)):
    print(x[i])
    print()

#row swap
def rswap(x,r1,r2):
  for i in range(0,len(x[0])):
    y = x[r1][i]
    x[r1][i] = x[r2][i]
    x[r2][i] = y

#choose the pivot element and make it the leading element
def pivot(o,m,n):
  gr = m
  for i in range(m,len(o)):
    if abs(o[i][n]) > abs(o[gr][n]): gr = i
    else: continue
  if gr != m: 
    rswap(o,m,gr)
    return True

#making the leading element 1 and rest 0 - takes the object, row and column of lead element     
def col_rref(x,y,z,l=0,u=0):
# l=0 corresponds to reduction of elements below the diagonal
# l=1 corresponds to no reduction of elements below the diagonal
# u=0 corresponds to reduction of elements above the diagonal
# u=1 corresponds to no reduction of elements above the diagonal  
  if x[y][z]==0:
    print("Error - Leading element at ",y,",",z,"is 0")
    print("Error: Pre-augmented matrix is not invertible")
    return
  elif l==1 & u==1: 
    print("Error - Input values for 'l' and 'u' correspond to no reduction at all. Atleast one must be 0")
    return
  else:
  
      #for converting column to rref form
      if u == 0: 
        for i in range(0,y):
          f = x[i][z]
          for j in range(0,len(x[0])): x[i][j] = x[i][j] - ((x[y][j])*f)

      if l == 0:
        for i in range(y+1,len(x)):
          f = x[i][z]
          for j in range(0,len(x[0])): x[i][j] = x[i][j] - ((x[y][j])*f)

#transpose of a matrix
def trans(x):
  y = [0] * len(x[0])
  for k in range(0,len(x[0])): y[k] = [0] * len(x)
  for i in range(0, len(x[0])):
    for j in range(0, len(x)):
      y[i][j] = x[j][i]
  return(y)

# matrix addition
def mat_add(M,N):
       if (len(M)==len(N)) & (len(M[0])==len(N[0])):
              for i in range(len(M)):
                     for j in range(len(M[0])): M[i][j]=M[i][j]+N[i][j]
              return M             

#multiplying matrix with a scalar              
def scale_mat(M,k):
        for i in range(len(M)):
            for j in range(len(M[0])): M[i][j]=k*M[i][j]
        return M 

#matrix prod
def mat_prod(x,y): #for XY
  if len(x[0]) != len(y):
    print("Product not defined: Incorrect matrix order")
  else:
    #dynamic creation of blank product matrix 
    val = [0] * len(x) 
    for n in range (len(x)): val[n] = [0] * len(y[0])

    #evaluating the elements of product matrix
    for i in range(0, len(val)):        
      for j in range (0, len(val[0])):
        sum = 0
        for k in range(0, len(y)):
          # print(x[i][r])
          # p = x[i]
          sum = sum + (x[i][k])*(y[k][j])
        val[i][j] = sum

    return(val)

#determinant
def det(y):
  x = [0]*len(y)
  for i in range(len(y)): x[i]=[0]*len(y[0])
  if len(x)!=len(x[0]):
    print("Input is not a square matrix, determinant not defined")
    return
  for i in range(len(y)):
    for j in range(len(y)): x[i][j]=y[i][j]
  res = 1
  for d in range(0, len(x)):
    a = pivot(x, d, d)
    if a==True: res = res*(-1)
    if x[d][d]==0:
      res = 0 
      return res
    else:
      #for converting column to rref form
      col_rref(x,d,d,0,1)
    d = d + 1
  for i in range(0, len(x)): res = res*x[i][i]
  if len(x)%2 != 0: return(res*(-1))
  else: return res

def mat_inv(x):
  #takes square matrix as input
    if len(x) != len(x[0]):
        print("Error: input is not a square matrix")
        return
    elif det(x) == 0:
        print("Error: input is not invertible")
        return
    else:
        #creating appropriate augmented input matrix
        for i in range(0, len(x)):
            for j in range(0, len(x)): x[i].append(0)
        for i in range(0, len(x)): x[i][(len(x)+i)] = 1
        # inversion using gauss jordan elimination(full rref)
        gj_ele(x)
        return(x)

#check symmetry
def is_sym(val):
  if len(val) != len(val[0]):
    print("Invalid Input: Enter a square matrix")
  else:
    for i in range(len(val)):
      for j in range(len(val)):
        if val[i][j] != val[j][i]: return False
        else: continue
    return True

#check positive definite
def is_posdef(val, m=10000):
  
  #creating blank test vector in R^n
  test = [0] * len(val)
  for i in range(len(val)): test[i] = [0]

  #generating random seed
  t = time.localtime()
  ct = time.strftime("%H%M%S", t)
  ct = int(ct)
  
  #intializing the test vector with random values
  r_arr = rn.myLCG_arr(ct, len(val), 200, -1)
  for i in range(len(val)): 
    test[i][0] = r_arr[i]

  # m - loop for testing with random vectors
  for k in range(m):
    p = mat_prod(val, test)
    p = mat_prod(trans(test), p)

    if p[0][0] > 0: 
      t = time.localtime()
      ct = time.strftime("%H%M%S", t)
      ct = (int(ct) + k)*int(ct)
      r_arr = rn.myLCG_arr(ct, len(val), -100, -1)
      for i in range(len(val)): test[i][0] = r_arr[i]
    else: 
      #print("Input matrix is not positive definite")
      print("Counter example test vector: ", test)
      return False
  
  if k==(m-1):
    return True

#absolute sum of all elements in row except chosen one
def row_absum(x,m,n):
    # for n^th element of m^th row
    sum = 0
    for k in range(len(x)):
        if k==n: continue
        else: sum += abs(x[m][k])
    return sum

#diagonally dominant
def diag_dom(x):
    for i in range(0,len(x)):
        ck = abs(x[i][i])
        if ck < row_absum(x,i,i):
            for j in range(i+1, len(x)): # looking for best candidate for diagonal element x[i][i]
                if abs(x[j][i])>=row_absum(x,j,i): rswap(x,j,i)
    
    #check if the matrix after swapping is diagonally dominant
    dom = 1
    for i in range(0,len(x)):
      if abs(x[i][i]) <= row_absum(x,i,i): dom = 0

    if dom == 1: return x
    else:
      print("Error: Diagonally dominant form for Input matrix not found")
      return     

#Gauss-Jordan Elimination
def gj_ele(x, ck=1, l=0, u=0):
  # takes augmented matrix as input
  # ck=0 corresponds to no scaling of the lead element, diagonals are not 1
  # ck=1 (default) corresponds to scaling of the lead element, diagonals are 1
  # 'l' & 'u' takes corresponding inputs for col_rref
  if len(x) == (len(x[0])):
    print("Error: Pre-augmented matrix is not a square matrix")
    return
  
  for d in range(0, len(x)):
    pivot(x, d, d)
    if ck==1: 
      lead = float(x[d][d])
      #for scaling the pivot element to 1
      for i in range(0,len(x[0])): x[d][i] = float((x[d][i])/lead)
    col_rref(x, d, d, l, u)
    d = d + 1

#Forward substitution
def fwd_sub(A,B):
  #'A' - input square matrix as 2-D list for AX=B
  #'B' - input column vector matrix as 1-D list  for AX=B
    if len(A)!=len(A[0]):
        print("Error: Input A is not a square matrix in AX=B")
        return
    elif len(A) != len(B):
        print("Length of A is not equal to that of B; LHS/RHS not appropriately defined as in AX=B")
        print("# of variables != # of equations")
        return
    
    for i in range(0, len(A)):
        sum = 0
        for j in range(0,i): sum = sum + (A[i][j]*B[j])
        B[i] = (B[i] - sum)/A[i][i]

#Backward substitution
def bc_sub(A,B):
  #'A' - input square matrix as 2-D list for AX=B
  #'B' - input column vector matrix as 1-D list  for AX=B
    if len(A)!=len(A[0]):
        print("Error: Input A is not a square matrix in AX=B")
        return
    elif len(A) != len(B):
        print("Length of A is not equal to that of B; LHS/RHS not appropriately defined as in AX=B")
        print("# of variables != # of equations")
        return  
    
    for i in range(len(A)-1,-1,-1):
        sum2 = 0
        for j in range(i+1, len(A)): sum2 += A[i][j]*B[j]
        B[i] = (B[i] - sum2)/A[i][i]

#LU Decomposition
def doolittle_lu(x, n=1):
  # takes pre-augmented(square) matrix as input
    if len(x) != len(x[0]):
        print("Error: A is not a square matrix in AX=B")
        print("# of variables != # of equations")
        return 
    elif (n==1) & (det(x) == 0):
        print("Error: A is not invertible in AX=B, No solutions exist")
        return
    else:
        for j in range(0, len(x)):
            for i in range(1, j+1):
              sum1 = 0
              for k in range(0,i): sum1 = sum1 + ((x[i][k])*(x[k][j]))
              x[i][j] = x[i][j] - sum1
            for i in range(j+1, len(x)):
              sum2 = 0
              for k in range(0,j): sum2 = sum2 + ((x[i][k])*(x[k][j]))
              x[i][j] = (x[i][j] - sum2) / (x[j][j])
                    
        del sum1
        del sum2
        return x

#Cholesky Decomposition
def cholesky_deco(x):
  # x takes input matrix; pre-augmented(square)
    if len(x)!=len(x[0]):
      print("Error: Input is not a square matrix")
      return
    
    if det(x) == 0:
        print("Error: A is not invertible in AX=B, No solutions exist")
        return

    for i in range(0, len(x)):
        for j in range(0, i+1):
            sum1 = 0
            sum2 = 0
            for k in range(0,i): sum1 += (x[i][k])**(2) 
            if i==j: x[i][j] = (x[i][i] - sum1)**(0.5)
            elif i>j:
                for k in range(0,j): sum2 += x[i][k]*x[j][k]
                x[i][j] = (x[i][j]-sum2)/x[j][j]
    del sum1
    del sum2
    for i in range(0, len(x)): #ouput is a lower triangular matrix
        for j in range(i+1, len(x)): x[i][j] = 0
    
    return(x)

#Gauss - jacobi
def gji(val, tol, max = 25, ini=0):
  # takes augmented matrix as input
  #tol corresponds to precision/tolerance
  #max corresponds  to the maximum number of iterations
  #ini=0 corresponds to random initial guess
  #ini=1 corresponds to initial guess 0

  if len(val) != (len(val[0])-1):
    print("Error: Pre-augmented matrix is not a square matrix")
    return

  #storing 'b'
  b = [0] * len(val)
  for i in range(len(val)): b[i] = val[i][(len(val[0])-1)]
  
  x_old = [0] * len(val)
  x_new = [0] * len(val)

  if ini==0:
    #initializing x_old
    t = time.localtime()
    ct = time.strftime("%H%M%S", t)
    ct = int(ct)

    ran = rn.myLCG_arr(ct, len(val), 10, -1)
    for i in range(len(val)):
      x_old[i] = ran[i]
    print("Initial guess: ", x_old)
  
  
  for k in range(max+1):
    ck = 1
    for i in range(0, len(val)):
      sum = 0
      for j in range(0, len(val)):
        if i!=j: sum = sum + (val[i][j] * x_new[j])
      x_new[i] = (b[i] - sum)/val[i][i]

    
    for p in range(0, len(val)):
      if abs(x_new[p] - x_old[p]) > tol:
        ck = 0
      else: continue
    
    if ck == 1: 
      # print(k)
      x_new.append(k)
      return(x_new)
    else: 
      for t in range(len(val)): x_old[t] = x_new[t]
      continue

  
  if k == max: 
    print("No. of iterations exceeded max input, no convergent solution found")
    print("No . of iterations tested: ", k)

#Gauss - Seidel
def gsd(val, tol, max = 50, ini = 0):
  # takes augmented matrix as input
  #tol corresponds to precision/tolerance
  #max corresponds  to the maximum number of iterations
  #ini=0 corresponds to random initial guess
  #ini=0 corresponds to initial guess 0
  
  if len(val) != (len(val[0])-1):
    print("Error: Pre-augmented matrix is not a square matrix")
    return

  #storing 'b'
  b = [0] * len(val)
  for i in range(len(val)): b[i] = val[i][(len(val[0])-1)]
  
  x_old = [0] * len(val)
  x_new = [0] * len(val)
  
  if ini==0:
    #initializing x_old
    t = time.localtime()
    ct = time.strftime("%H%M%S", t)
    ct = int(ct)

    ran = rn.myLCG_arr(ct, len(val), 10, -1)
    for i in range(len(val)):
      x_old[i] = ran[i]
      x_new[i] = x_old[i]
    
    print("Initial guess: ", x_old)  

  for k in range(max+1):
    ck = 1
    for i in range(len(val)):
      sum1 = 0
      sum2 = 0
      for j in range(i):
        sum1 += (val[i][j] * x_new[j])
      for j in range(i+1, len(val)):
        sum2 += (val[i][j] * x_new[j])
    
      x_new[i] = (b[i] - sum1 - sum2)/(val[i][i])
  
    for p in range(len(val)):
      if abs(x_new[p] - x_old[p]) >= tol:
        ck = 0
      else: continue
    
    for p in range(len(val)):
      if math.isnan(x_new[p]):
        print("Divergent solution")
        print("Storage limit exceeded at iteration :",k)
        return

    if ck == 1: 
      # print(k)
      x_new.append(k)
      return(x_new)
    else: 
      for t in range(len(val)): x_old[t] = x_new[t]
      continue
  
  if k == max: 
    print("No. of iterations exceeded max input, no convergent solution found")
    print("Last iteration :", x_new)

