import math
import time
from matplotlib import pyplot as plt

import numpy as np
from mypylib import random as rn
from mypylib import mat_iter as mi

## Roots of non-linear functions

# Bisection method
def bisec(s, eps, de, lb = -1, ub = 1, ck = 0, n = 10000):
# 's' - input function as string
# 'eps' - tolerance for output of function
# 'de' - tolerance for input of function
# 'lb' - initial guess for lower bound of test interval, default = -1
# 'ub' - initial guess for upper bound of test interval, default = 1
# 'ck' - check variable; 1 - output is list of estimates for root after each iteration and the corresponding iteration
# 'ck' - check variable; 0 (default) - outputs are the root and the correspoding iteration count
# 'n' - max iteration count    
    
    lnew = lb
    unew = ub
    ctnew = 0
    anew = 0
    bnew = 0
    res = [[]]

    if lnew >= unew:
        print("Error: Lower bound of interval not less than upper bound")
        return
    for k in range(n):
      x = lnew
      anew = eval(s) #ouput of function at lnew
      x = unew
      bnew = eval(s) #ouput of function at unew

      #if either of the ouputs are within tolerance
      if abs(anew) < eps: 
        if ck == 1: 
          if len(res[len(res)-1]) == 0:
            res[len(res)-1].append(lnew)
            res[len(res)-1].append(k) 
          else:
            res[len(res)-1][0] = lnew
            res[len(res)-1][1] = k
          return res
        else: return lnew, k
      elif abs(bnew) < eps: 
        if ck == 1: 
          # res.append([])
          if len(res[len(res)-1]) == 0:
            res[len(res)-1].append(unew)
            res[len(res)-1].append(k) 
          else:
            res[len(res)-1][0] = unew
            res[len(res)-1][1] = k
          return res
        else: return unew, k
      
      #if both ouputs have same sign and f(lnew) < f(unew)
      elif (anew*bnew > 0) & (anew < bnew):
        #checking for root in between lnew and unew
        t = (lnew + unew)/2
        x = t
        ft = eval(s)
        #case: change of sign of function between lnew and unew
        if ft*anew < 0:
            unew = t
            if ck == 1: 
              res.append([])
              res[len(res)-1].append(((lnew + unew)/2))
              res[len(res)-1].append((k+1))
            del t
            del ft
        #case: function has root at midpoint of chosen interval
        elif abs(ft) < eps: 
          if ck == 1: 
            res.append([])
            res[len(res)-1].append(t)
            res[len(res)-1].append((k+1))
            return res
          else: return t, (k+1)
        #case: function's value between lnew & unew greater than at endpoints of interval    
        elif (ft > anew) & (ft > bnew):
            d = unew - lnew
            if anew < 0: #shift towards right needed
                lnew = unew
                unew = lnew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
            else: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
            del d
        #case: no root detected in the interval, new interval needed
        else:
          #case: function decreasing towards lower bound of interval; shift new interval to the left
            #subcase: fast variation in function over the interval, smaller shift needed 
            if anew < (0.5*bnew):
              d = unew - lnew
              if anew < 0: #shift towards right needed
                lnew = unew
                unew = lnew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
            #subcase: slow variation in function over the interval, larger shift needed
            else:
              d = unew - lnew
              if anew < 0: #shift towards right needed
                lnew = unew + d
                unew = lnew + 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards left needed
                unew = lnew - d
                lnew = lnew - 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
      
      #if both ouputs have same sign and f(lnew) > f(unew)
      elif (anew*bnew > 0) & (anew > bnew):
        #checking for root in between lnew and unew
        t = (lnew + unew)/2
        x = t
        ft = eval(s)
        #case: change of sign of function between lnew and unew
        if ft*anew < 0:
            lnew = t
            if ck == 1: 
              res.append([])
              res[len(res)-1].append(((lnew + unew)/2))
              res[len(res)-1].append((k+1))
            del t
            del ft
        #case: function has root at midpoint of chosen interval
        elif abs(ft) < eps: 
          if ck == 1: 
            res.append([])
            res[len(res)-1].append(t)
            res[len(res)-1].append((k+1))
            return res
          else: return t, (k+1)
        #case: function's value between lnew & unew greater than at endpoints of interval
        elif (ft > anew) & (ft > bnew):
            d = unew - lnew
            if anew < 0: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
            
            else: #shift towards right needed
                lnew = unew
                unew = unew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
            del d
        #case: no root detected in the interval, new interval needed
        else:
          #case: function decreasing towards lower bound of interval; shift new interval to the left 
            #subcase: fast variation in function over the interval, smaller shift needed
            if bnew < (0.5*anew):
              d = unew - lnew
              if anew < 0: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              
              else: #shift towards right needed
                lnew = unew
                unew = unew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
            #subcase: slow variation in function over the interval, larger shift needed
            else:
              d = unew - lnew
              if anew < 0: #shift towards left needed
                unew = lnew - d
                lnew = lnew - 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              
              else: #shift towards right needed
                lnew = unew + d
                unew = unew + 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
      
      #if both ouputs have same sign and f(lnew) = f(unew)
      elif (anew*bnew > 0) & (anew == bnew): 
        unew = (lnew + unew)/2
        if ck == 1: 
          res.append([])
          res[len(res)-1].append(((lnew + unew)/2))
          res[len(res)-1].append((k+1))

      #if the ouputs have opposite sign  
      else: 
        ctnew = (lnew + unew)/2
        x = ctnew
        c = eval(s)
        if (anew*c < 0) & (bnew*c > 0):
            unew = ctnew
            if ck == 1: 
                res.append([])
                res[len(res)-1].append(((lnew + unew)/2))
                res[len(res)-1].append((k+1))
            if abs(lnew - unew) < de: 
              if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(ctnew)
                  res[len(res)-1].append((k+1))
                  return res
              else: return ctnew, (k+1)

        elif (bnew*c < 0) & (anew*c > 0):
            lnew = ctnew
            if ck == 1: 
                res.append([])
                res[len(res)-1].append(((lnew + unew)/2))
                res[len(res)-1].append((k+1))
            if abs(lnew - unew) < de: 
              if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(ctnew)
                  res[len(res)-1].append((k+1))
                  return res
              else: return ctnew, (k+1)
  
    if k == (n-1):
      print("No convergent solution found after",n,"iterations")
      return
    
    return(res)

# Bisection method(recursive)
def bisec_rec(s, eps, de, lb = -1, ub = 1):
# 's' - input function as string
# 'eps' - tolerance for output of function
# 'de' - tolerance for input of function
# 'lb' - initial guess for lower bound of test interval, default = -1
# 'ub' - initial guess for upper bound of test interval, default = 1

  x = lb
  a = eval(s)
  # print(a)
  x = ub
  b = eval(s)
  # print(b)

  #case: right bracket found, need to shorten it
  if a*b < 0: 
    if (abs(ub - lb) < de) & (abs(b - a) < eps):
      res = (lb + ub)/2
      return(res)
    else: 
      d = (lb + ub)/2
      x = d
      c = eval(s)
      if c*a < 0: #going with the left half
        return(bisec_rec(s, eps, de, lb, d))
      elif c*a == 0: #going with the right half
        return d
      else: return(bisec_rec(s, eps, de, d, ub))
  
  #case: need to go right
  elif (a*b > 0) & (abs(a) > abs(b)):
    y = lb 
    lb = ub
    ub = ub + (ub - y)
    del y
    return(bisec_rec(s, eps, de, lb, ub))

  #case: need to go left
  elif (a*b > 0) & (abs(b) > abs(a)):
    y = ub 
    ub = lb
    lb = lb - (y - lb)
    del y
    return(bisec_rec(s, eps, de, lb, ub))

  #case: equal values at both points
  elif (a*b > 0) & (abs(b) == abs(a)): 
    z = ub - lb
    ck = 0 #check variable, tells which is the correct bracket - prod is -ve
    #trying to bracket towards the left
    for k in range(1,300):
      np = lb - k*z 
      x = np
      out = eval(s)
      if out*b < 0:
        ck = 1
        break
    #if ck is 1, then bracket is shifted there
    if ck == 1:
      lb = np
      ub = lb + z
      return(bisec_rec(s, eps, de, lb, ub))
    else: #trying to bracket towards the right
      for k in range(1,300):
        np = ub + k*z 
        x = np
        out = eval(s)
        if out*b < 0:
          ck = 1
          break
      #if ck is 1, then bracket is shifted there
      if ck == 1:
        ub = np
        lb = ub - z
        return(bisec_rec(s, eps, de, lb, ub))
      #if both sides don't work out, going to the extreme right to start anew
      else:
        lb = lb + 1000*z
        ub = lb + z
        return(bisec_rec(s, eps, de, lb, ub))
  
  #case: one side of the bracket is the soln
  else: 
    if a == 0: return lb
    else: return ub

# Regula falsi
def regfal(s, eps, de, lb = -1, ub = 1, ck = 0, n = 10000):
# 's' - input function as string
# 'eps' - tolerance for output of function
# 'de' - tolerance for input of function
# 'lb' - initial guess for lower bound of test interval, default = -1
# 'ub' - initial guess for upper bound of test interval, default = 1
# 'ck' - check variable; 1 - output is list of estimates for root after each iteration and the corresponding iteration
# 'ck' - check variable; 0 - outputs are the root and the correspoding iteration count
# 'n' - max iteration count
    
    lnew = lb
    unew = ub
    ctnew = 0
    ctold = 0
    anew = 0
    bnew = 0
    res = [[]]

    if lnew >= unew:
        print("Error: Lower bound of interval not less than upper bound")
        return
    for k in range(n):

      ctold = ctnew
      x = lnew
      anew = eval(s) #ouput of function at lnew
      x = unew
      bnew = eval(s) #ouput of function at unew

      #if either of the ouputs are within tolerance
      if abs(anew) < eps: 
        if ck == 1:
              if len(res[len(res)-1]) == 0:
                res[len(res)-1].append(lnew)
                res[len(res)-1].append(k) 
              else:
                res[len(res)-1][0] = lnew
                res[len(res)-1][1] = k
              return res
        else: return lnew, k
      elif abs(bnew) < eps: 
        if ck == 1: 
              if len(res[len(res)-1]) == 0:
                res[len(res)-1].append(unew)
                res[len(res)-1].append(k) 
              else:
                res[len(res)-1][0] = unew
                res[len(res)-1][1] = k
              return res
        else: return unew, k
      
      #if both ouputs have same sign and f(lnew) < f(unew)
      elif (anew*bnew > 0) & (anew < bnew):
        #checking for root in between lnew and unew
        t = (lnew + unew)/2
        x = t
        ft = eval(s)
        #case: change of sign of function between lnew and unew
        if ft*anew < 0:
            unew = t
            if ck == 1: 
              res.append([])
              res[len(res)-1].append(((lnew + unew)/2))
              res[len(res)-1].append((k+1))
            del t
            del ft
        #case: function has root at midpoint of chosen interval
        elif abs(ft) < eps: 
          if ck == 1: 
              res.append([])
              res[len(res)-1].append(t)
              res[len(res)-1].append((k+1))
              return res
          else: return t, (k+1)
        #case: function's value between lnew & unew greater than at endpoints of interval
        elif (ft > anew) & (ft > bnew):
            unew = t
            if ck == 1: 
              res.append([])
              res[len(res)-1].append(((lnew + unew)/2))
              res[len(res)-1].append((k+1))
            del t
            del ft
        #case: no root detected in the interval, new interval needed
        else:
          #case: function decreasing towards lower bound of interval; shift new interval to the left 
            #subcase: fast variation in function over the interval, smaller shift needed 
            if anew < (0.5*bnew):
              d = unew - lnew
              if anew < 0: #shift towards right needed
                lnew = unew
                unew = lnew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
            #subcase: slow variation in function over the interval, larger shift needed
            else:
              d = unew - lnew
              if anew < 0: #shift towards right needed
                lnew = unew + d
                unew = lnew + 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards left needed
                unew = lnew - d
                lnew = lnew - 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
      
      #if both ouputs have same sign and f(lnew) > f(unew)
      elif (anew*bnew > 0) & (anew > bnew):
        #checking for root in between lnew and unew
        t = (lnew + unew)/2
        x = t
        ft = eval(s)
        #case: change of sign of function between lnew and unew
        if ft*anew < 0:
            lnew = t
            if ck == 1: 
                res.append([])
                res[len(res)-1].append(((lnew + unew)/2))
                res[len(res)-1].append((k+1))
            del t
            del ft
        #case: function has root at midpoint of chosen interval
        elif abs(ft) < eps: 
          if ck == 1: 
              res.append([])
              res[len(res)-1].append(t)
              res[len(res)-1].append((k+1))
              return res
          else: return t, (k+1)
        #case: function's value between lnew & unew greater than at endpoints of interval
        elif (ft > anew) & (ft > bnew):
            lnew = t
            if ck == 1: 
                res.append([])
                res[len(res)-1].append(((lnew + unew)/2))
                res[len(res)-1].append((k+1))
            del t
            del ft
        #case: no root detected in the interval, new interval needed
        else:
          #case: function decreasing towards lower bound of interval; shift new interval to the left 
            #subcase: fast variation in function over the interval, smaller shift needed 
            if bnew < (0.5*anew):
              d = unew - lnew
              if anew < 0: #shift towards left needed
                unew = lnew
                lnew = lnew - d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards right needed
                lnew = unew
                unew = unew + d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
            #subcase: slow variation in function over the interval, larger shift needed
            else:
              d = unew - lnew
              if anew < 0: #shift towards left needed
                unew = lnew - d
                lnew = lnew - 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              else: #shift towards right needed
                lnew = unew + d
                unew = unew + 3*d
                if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
              del d
      
      #if both ouputs have same sign and f(lnew) = f(unew)
      elif (anew*bnew > 0) & (anew == bnew): 
        unew = (lnew + unew)/2
        if ck == 1: 
            res.append([])
            res[len(res)-1].append(((lnew + unew)/2))
            res[len(res)-1].append((k+1))

      #if the ouputs have opposite sign  
      else: 
        ctnew = unew - ((unew-lnew)*bnew/(bnew - anew))
        x = ctnew
        c = eval(s)
        if (anew*c < 0) & (bnew*c > 0):
            if abs(ctnew - ctold) < de: 
              if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((ctnew + ctold)/2))
                  res[len(res)-1].append((k+1))
                  return res
              else: return ctnew, (k+1)
            unew = ctnew
            if ck == 1: 
              res.append([])
              res[len(res)-1].append(((lnew + unew)/2))
              res[len(res)-1].append((k+1))
            
        elif (bnew*c < 0) & (anew*c > 0):
            if abs(ctnew - ctold) < de: 
              if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((ctnew + ctold)/2))
                  res[len(res)-1].append((k+1))
                  return res
              else: return ctnew, (k+1)
            lnew = ctnew
            if ck == 1: 
                  res.append([])
                  res[len(res)-1].append(((lnew + unew)/2))
                  res[len(res)-1].append((k+1))
             
    if k == (n-1):
      print("No convergent solution found after",n,"iterations")
      return
    
    return(res)

# Newton-Raphson (taking function and its derivative as an input via string)
def newraph(f, df, eps, de, ini = 0, ck = 0, n = 10000):
  #'f' - main input function
  #'df' - derivative of input function
  #'eps' - tolerance for function's output value
  # 'ck' - check variable; 1 - output is list of estimates for root after each iteration and the corresponding iteration
  # 'ck' - check variable; 0 (default) - outputs are the root and the correspoding iteration count
  #'n' - max iteration count; default = 10000

  xnew = ini
  xold = xnew
  res = [[]]
  for k in range(n):
    x = xnew
    a = eval(f)
    b = eval(df)
    if abs(a) <= eps: 
      if ck == 1:
          if len(res[len(res)-1]) == 0:
            res[len(res)-1].append(xnew)
            res[len(res)-1].append(k) 
          else:
            res[len(res)-1][0] = xnew
            res[len(res)-1][1] = k
          return res
      # print("Iteration Count: ", k+1)
      else: return xnew, k
    if abs(b) < (eps**2): #if the function is varying too slowly(relative to eps),
      xnew = 3*xnew + 2 #large change in new test point
      if ck == 1:
          res.append([])
          res[len(res)-1].append(xnew)
          res[len(res)-1].append((k+1))
      continue
    else: 
      xold = xnew
      xnew = xnew - a/b
      if ck == 1: 
          res.append([])
          res[(len(res)-1)].append(xnew)
          res[(len(res)-1)].append((k+1))

    
    if abs(xnew - xold) < de: 
      # print("Iteration Count: ", k+1)
      if ck == 1: 
          res[len(res)-1][0] = (xnew + xold)/2
          res[len(res)-1][1] = k
          return res
      else:
        root = (xnew + xold)/2
        return root, k
  
  if k == (n-1):
    print("No convergent solution found after",n,"iterations")
    return

#differentiating polynomial as array of coefficients
def deriv_poly(l):
  n = len(l)
  if n == 1: 
    res = [0]
    return(res)
  res = [0]*(n-1)
  for j in range(n-1): res[j] = (j+1)*l[j+1]
  return(res)

#printing polynomial as string from array of coefficients
def pr_poly(lit):
  n = len(lit)
  f = str(lit[0])
  for k in range(1, n):
    if lit[k] == 0:continue
    elif lit[k] == 1: f = f + " + " + "(x**"+str(k)+")"
    elif lit[k] < 0: f = f + " - " + str(abs(lit[k]))+"*(x**"+str(k)+")"
    else: f = f + " + " + str(lit[k])+"*(x**"+str(k)+")"
  return f

# 
def findroot_poly(ls, eps, de, ini = 1, maxiter = 30):

  curr = ini
  x = curr
  ans = [0]*2

  for i in range(maxiter):
    f_o = eval(pr_poly(ls))
    df_o = eval(pr_poly(deriv_poly(ls)))
    d2f_o = eval(pr_poly(deriv_poly(deriv_poly(ls))))

    if abs(f_o) < (eps**2): 
      ans[0] = curr
      ans[1] = i
      return(ans)
    
    G = (df_o)/(f_o)
    H = (G**2) - ((d2f_o)/(f_o))
    deg = len(ls) - 1

    if G >= 0: a = deg/(G + (((deg - 1)*(deg*H - (G**2)))**0.5))
    else: a = deg/(G - (((deg - 1)*(deg*H - (G**2)))**0.5))
     
    prev = curr 
    curr = curr - a
    x = curr

    if (abs(curr - prev) < de) & (abs(f_o) < eps): 
      ans[0] = curr
      ans[1] = i
      return(ans) #returns root and corresponding iteration count
    else: continue
  
  if i == (maxiter - 1): 
    print("No root found for: ")
    print(pr_poly(ls))

#Synthetic division - reduction of polynomial deg by 1
def deflate(lt, d, tol = 0.0001):
  arr = [0]*len(lt)
  for i in range(len(lt)): arr[i] = lt[(len(lt)-1-i)]
  for t in range(1,len(lt)): arr[t] = arr[t] + d*(arr[t-1])
  if abs(arr[(len(lt)-1)]) > tol: print("Non-zero remainder")
  else: 
    t_arr = [0]*len(lt)
    for i in range(len(lt)): 
      t_arr[i] = arr[(len(lt)-1-i)]

    arr = [0]*(len(lt) - 1)
    for i in range(len(arr)): arr[i] = t_arr[i+1]
    del t_arr
    return(arr)

# Laguerre's Method
def lagu(lst, ep, delta, fp = 1, iter = 30):
  n = len(lst) - 1
  if n >= 1:
    roots = [0]*n
    for u in range(n): roots[u] = [0]*2
    c_arr = lst
    for s in range(n):
      roots[s] = findroot_poly(c_arr, ep, delta, fp, iter)
      c_arr = deflate(c_arr, roots[s][0])
    return(roots)
  else:
    print("Enter a polynomial of degree >= 1")
    return


## Interpolation 

def poly_sum(p1, p2):
  if len(p1) > len(p2): t_arr = [0]*len(p1)
  else: t_arr = [0]*len(p2)
  for i in range(len(t_arr)):
    if i >= len(p1): t_arr[i] = p2[i]
    elif i >= len(p2): t_arr[i] = p1[i]
    else: t_arr[i] = p1[i] + p2[i]
  return(t_arr)

def poly_prod(l1, l2):

  arr = [0]*(len(l1) + len(l2) - 1)
  for i in range(len(l1)):
    for j in range(len(l2)): 
      k = i + j
      if i==j: arr[k] = l1[i]*l2[i]
      else: 
        if i >= len(l2): arr[k] = (l1[i]*l2[j])
        elif j >= len(l1): arr[k] = (l1[i]*l2[j])
        else: arr[k] = (l1[i]*l2[j]) + (l1[j]*l2[i])
  return(arr)

# Lagrange's Method (INCOMPLETE)
def Lag_interpol(xls, yls):
  n = len(xls)
  for i in range(n):
    prod = 0
    for k in range(n):
      if k == i:continue

#Linear Regression
def lsqfit_linear1d(val):
  # 'val' - input nested list; each row cotains (x_i, y_i, err_i)
  # err_i corresponds to std deviation in y_i; by default, the associated weight with y_i = 1
   
    if len(val[0]) == 2:
        for i in range(len(val)): val[i].append(1)
    elif len(val[0]) == 3:
        print("")
    else:
        print("Error: Invalid Input, enter 2D list with each element as (x_i,y_i)")
        return

    Sx = 0
    Sy = 0
    Sxx = 0
    Syy = 0
    Sxy = 0
    Si = 0
    De = 0
    for i in range(len(val)):
        Sx = Sx + ((val[i][0])/((val[i][2])**2))
        Sy = Sy + ((val[i][1])/((val[i][2])**2))
        Sxx = Sxx + (((val[i][0])**2)/((val[i][2])**2))
        Syy = Syy + (((val[i][1])**2)/((val[i][2])**2))
        Si = Si + (1/((val[i][2])**2))
        Sxy = Sxy + (((val[i][0])*(val[i][1]))/((val[i][2])**2))
    De = Si*Sxx - (Sx**2)

    a1 = ((Sxx*Sy) - (Sx*Sxy))/De
    a2 = ((Sxy*Si) - (Sx*Sy))/De
    err_a1 = Sxx/De
    err_a2 = Si/De

    res = [0]*2
    for i in range(2): res[i] = [0]*2
    res[0][0] = a1
    res[0][1] = err_a1
    res[1][0] = a2
    res[1][1] = err_a2

    # pears_r = (abs(Sxy)/math.sqrt(Sxx*Syy))
    # ONLY for \sigma_i = 1 for all i, use the following
    pears_r = abs((len(val)*Sxy) - (Sx*Sy))/abs((math.sqrt((Sxx*len(val)) - (Sx**2)))*(math.sqrt((Syy*len(val)) - (Sy**2))))
    pears_r = (pears_r**2)

    del Sx
    del Sy
    del Sxx
    del Sxy
    del Syy
    del Si
    del De
    del a1
    del a2
    del err_a1
    del err_a2

    return res, pears_r

#Polynomial Regression
def lsqfit_poly1d(val, deg):
# val - takes 2d matrix containing (x,y)
# deg - takes degree of polynomial(to be fit)
    
    if len(val[0]) == 2:
        deg = deg
    else:
        print("Error: Invalid Input, enter 2D list with each element as (x_i,y_i)")
        return

    n = deg
    test = [0]*(n+1)
    for i in range(0, n+1): test[i] = [0]*(n+2)
    test[0][0] = len(val)
    for i in range(0, n+1):
        for j in range(0, n+1):
            if i!=0 or j!=0:
                sum = 0
                for p in range(0, len(val)): sum = sum + ((val[p][0])**(i+j))
                test[i][j] = sum
        
        sum = 0
        for p in range(0, len(val)): sum = sum + (((val[p][0])**i)*(val[p][1]))
        test[i][n+1] = sum
    

    mi.gj_ele(test)
    sol = [0]*(n+1)
    for i in range(0, n+1): sol[i] = test[i][n+1]

    return(sol)

#Plotting best l_sq polynomial fit
def plot_polyfit(dt,deg):

    val = lsqfit_poly1d(dt,deg)

    #plotting data
    x_i = [dt[0][0]]
    y_i = [dt[0][1]]
    for i in range(1, len(dt)): x_i.append(dt[i][0])
    for i in range(1, len(dt)): y_i.append(dt[i][1])

    plt.scatter(x_i,y_i, color= 'black',marker='.')

    #plotting model function
    min = 0
    max = 0
    for i in range(len(x_i)):
        if min > x_i[i]: min = x_i[i]
        if max < x_i[i]: max = x_i[i]
    
    min = min - min*0.5
    max = max + max*0.5

    x = np.arange(min, max, 0.001)
    y = 0
    for i in range(len(val)): y += val[i]*(x**i) 
    plt.plot(x,y)
    
    for i in range(len(val)): val[i] = float(f'{val[i]:.2f}')
    leg = [[str(pr_poly(val))], ["Data"]]
    
    plt.grid(which='major')
    plt.legend(leg[0])
    return(plt.savefig("a.png"))

# Fixed point method
def fixpt(s, eps, ini = 0, n = 100):
# 's' - input fixed point function as string
# 'eps' - tolerance for output of function
# 'ini' - initial guess for the root
# 'n' - max iteration count; default = 1000    
    
    out = 0
    x = ini
    res = [[]]
    for i in range(n):
        out = eval(s)
        if abs(out-x) < eps: 
            # print(i)
            res[len(res)-1].append(x)
            res[len(res)-1].append(i)            
            return res
        x = out
        res[len(res)-1].append(x)
        res[len(res)-1].append(i)
        res.append([])
        if i == n-1: 
            print("No convergent solution found after",n,"iterations with given fixed point function.")
            return
        
