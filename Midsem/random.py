global gseed, curr
gseed = 0
curr = 0
def myLCG(seed, scale = 32768, sgn = 1): # takes seed, the number of random numbers to be generated (n), the +-range (scale) in which the numbers are to be generated and 'sgn'.
# By default, scale = RANDMAX
# 'sgn' decides whether negative random numbers will be generated.
  global gseed
  global curr
  if seed == gseed:
    # print("")
    seed = seed
  else: 
    gseed = seed
    p = float(seed)
    curr = float(seed)

  a = 1103515245 # multiplier
  c = 12345 # increment
  m = 32768 # modulus: RANDMAX
  
  # b: base - decides whether negative random numbers will be generated, based on input 'sgn'
  # By default 'sgn' = 1; the function generates only positive random numbers within specified range
  # If 'sgn' is negative, negative numbers are generated
  if sgn >= 0: b = 0
  else: b = 1

  curr = (a*curr + c)%m
  curr = ((-1)**(b*(int(curr))))*curr
  rez = (curr*scale)/m
  del(a)
  del(c)
  del(m)
  del(b)
  return(rez)

def myLCG_arr(seed, n, scale = 32768, sgn = 1): # takes seed, the number of random numbers to be generated (n), the +-range (scale) in which the numbers are to be generated and 'sgn'.
# By default, scale = RANDMAX
# 'sgn' decides whether negative random numbers will be generated.
  random = [0] * n # blank array to store 'n' random numbers
  r = seed # the next random number
  a = 1103515245 # multiplier
  c = 12345 # increment
  m = 32768 # modulus: RANDMAX
  
  # b: base - decides whether negative random numbers will be generated, based on input 'sgn'
  # By default 'sgn' = 1; the function generates only positive random numbers within specified range
  # If 'sgn' is negative, negative numbers are generated
  if sgn >= 0: b = 0
  else: b = 1

  for i in range(n):
    r = (a*r + c)%m
    r = ((-1)**(b*(int(r))))*r
    r = (r*scale)/m
    random[i] = r
  del(r)
  del(a)
  del(c)
  del(m)
  del(b)
  return(random)


def gen_ranwalk(n, origin = [0,0], ls = 0):
# Input: number of steps (n)
# Input: origin of random walk (origin); Default - (0,0)
# Input: max length of step (ls); Default - 0 > the max length of step is fixed, as 2*sqrt(2)

  import time
  t = time.localtime()
  ct = time.strftime("%H%M%S", t)
  ct = int(ct)

  if ct > n: 
    seed1 = ct%n
    seed2 = n - (ct%n)
  elif ct == n: 
    seed1 = int(n/3)
    seed2 = int(n/2)
  else: 
    seed1 = 0
    seed2 = (n%ct)

  if ls == 0: t = 1
  else: t = ct%5

  x = myLCG_arr(seed1, n, 2*t, -1)
  y = myLCG_arr(x[seed1], n, 2*t, -1)
  ran_arr = [0] * int(n+1)

  for l in range(n+1): ran_arr[l] = [0] * 2
  ran_arr[0][0] = origin[0]
  ran_arr[0][1] = origin[1]

  for i in range(1,n):
    ran_arr[i][0] = x[i]
    ran_arr[i][1] = y[i]
  del(x)
  del(y)
  return(ran_arr)

def plot_ranwalk(n, origin = [0,0], ls = 0):
# takes the same inputs as random_walk()

  val = gen_ranwalk(n, origin, ls)
  X = [0] * (n+1)
  Y = [0] * (n+1)

  for i in range(1, (n+1)):
    X[i] = val[i][0] + ((X[i-1]))
    Y[i] = val[i][1] + ((Y[i-1]))
  
  del(val)

  import matplotlib.pyplot as plt

  plt.plot(X,Y)
  plt.xlabel("")
  plt.ylabel("")
  a = "Random walk: " + str(n) + " steps"
  plt.title(a)
  A = 0, round(X[n],3)
  B = 0, round(Y[n],3)
  for xy in zip(A, B):                                       # <--
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--
  plt.grid()
  del a
  plt.show()

  
def ranwalkdist(n, origin = [0,0], ls = 0):
# takes the same inputs as random_walk()

  val = gen_ranwalk(n, origin, ls)
  X = [0] * (n+1)
  Y = [0] * (n+1)

  for i in range(1, (n+1)):
    X[i] = val[i][0] + ((X[i-1]))
    Y[i] = val[i][1] + ((Y[i-1]))
  
  del(val)
  
  x = [0] * n
  y = [0] * n

  dist = 0
  sum = 0
  for i in range(n):
    dist = dist + ((((X[i+1] - X[i])**2)+((Y[i+1] - Y[i])**2))**(0.5))
    sum = sum + (((X[i+1] - X[i])**2)+((Y[i+1] - Y[i])**2))
    x[i] = int(i+1)
    y[i] = (sum/())**(0.5)

  rms = (sum/n)**(0.5)
  disp = ((((X[n])**2)+((Y[n])**2))**(0.5))

  del sum
  del dist
  del X
  del Y

  print("The rms distance covered for", n, "steps:", rms)
  print("The displacement after", n, "steps:", disp)

  import matplotlib.pyplot as plt

  plt.plot(x,y)
  plt.xlabel("Number of steps 'n'")
  plt.ylabel("Distance covered in n steps")
  plt.title("Distance covered in random walk vs no. of steps")
  plt.show()