# P452 Midsem Exam
# Name: Monu Kumar Choubey
# Roll: 2011090
# Stream: Int. M.Sc.
# Batch: 2020

from mypylib import de as de

f = "x**2"   #([linear mass density])
g = "x**3"   #(x*[linear mass density])
df = "2"
dg = "6*x"

# COM = (integration of (x*[linear mass density]))/(integration of [linear mass density]) over relevant limits

# Assume that the left end of the rod is kept at origin.
# Length of rod = 2m
# Integration limits = 0 to 2

# Integration of (x*[linear mass density])
res1 = de.midpt_integ(g,dg,0,2,1,0.0001)

# Integration of [linear mass density]
res2 = de.midpt_integ(f,df,0,2,1,0.0001)

res = res1/res2

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q4 out.txt", "w+")
fout.writelines("Solution by Midpoint Integration (Precision - 10^(-4))\n\n"+"Given, Length of rod = 2 m\n"+"Linear mass density = x^2\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\P452 Midsem 24\Q4 out.txt", "a")
fout.writelines("Assume that the left end of rod is kept at the origin.\n\n")
fout.writelines("Center of Mass = "+str(float(f'{res:.5f}'))+" m")
fout.close()