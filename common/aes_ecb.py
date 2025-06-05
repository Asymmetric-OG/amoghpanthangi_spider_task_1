import random

k=3
a0=9818440203 # secret = first term of the polynomial
n=10
sum=0
shares=[]
minset=[]

'''for k shares to unlock the secret,
polynomial should be of k-1 degree, k-1 equations and k-1 variables'''

coeffs=[a0]
for i in range(1,k):
    coeffs = coeffs + [random.randint(1,1000)] #a1 to ak-1

def fun(x):
    poly=0
    for i in range(k):
        poly = poly + coeffs[i]*pow(x,i) # a0+a1x+a2x2.......+ak-1xk-1
    return poly

for i in range(n):
    pt=random.randint(1,1000)
    shares = shares + [(pt, fun(pt))] # n total shares where each share is a tuple

i=1
while i<=k:
    pick = random.choice(shares)
    if pick not in minset:
        minset = minset + [pick]
        i+=1

#A random combination of UNIQUE k out of n shares should be enough to unlock the secret
#minset is that random combination

'''Lagrange Interpolation formula to find f(0) using k shares'''

for i in range(0,k):
    pi=1
    for j in range(0,k):
        if j!=i:
            pi = pi * ((0 - minset[j][0]) / (minset[i][0] - minset[j][0]))
    sum = sum+(pi*minset[i][1])

#print(shares)
#print(minset)
#print(a0)
print(round(sum))


