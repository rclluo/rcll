from math import sqrt

"""
Some statistics related functions.
"""

def avg(ls: list):
    return sum(ls)/len(ls)

def var(ls: list):
    mean=avg(ls)
    return sum(pow(x-mean,2) for x in ls)/len(ls)

def dev(ls: list):
    return sqrt(var(ls))

def med(ls: list):
    n=len(ls)
    s=sorted(ls)
    return (s[n//2-1]/2.0+s[n//2]/2.0,s[n//2])[n%2]
