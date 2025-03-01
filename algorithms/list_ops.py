"""
Prefix Sums
Please note that these functions take padded input and give padded output.
"""

def prefix_1d(arr: list) -> list:
    pref=[0 for i in range(len(arr))]
    for i in range(1, len(arr)):
        pref[i]=arr[i]+pref[i-1]
    return pref

def prefix_2d(arr: list[list]) -> list[list]:
    pref=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            pref[i][j]=arr[i][j]+pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]
    return pref

def prefix_3d(arr: list[list[list]]) -> list[list[list]]:
    pref=[[[0 for i in range(len(arr[0][0]))] for j in range(len(arr[0]))] for k in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            for k in range(1, len(arr[0][0])):
                pref[i][j]=arr[i][j]+pref[i-1][j][k]+pref[i][j-1][k]+pref[i][j][k-1]-pref[i-1][j-1][k]-pref[i][j-1][k-1]-pref[i-1][j][k-1]+pref[i-1][j-1][k-1]
    return pref

"""
Matrix Transformations
"""

def rotate(arr: list[list], rotations: int):
    """
    Rotate clockwise 90 degrees `rotations` times
    """
    for _ in range(rotations%4):
        arr=list(zip(*arr[::-1]))
    return arr

def flip_horizontal(arr: list[list]):
    return [i[::-1] for i in arr]

def flip_vertical(arr: list[list]):
    return arr[::-1]

"""
Subsequence related things
"""

def lis(seq,comp=lambda a,b:a>b):
    if not seq:
        return seq
    m=[None]*len(seq)
    p=[None]*len(seq)
    l=1
    m[0]=0
    for i in range(1, len(seq)):
        lower=0
        upper=l
        if comp(seq[i],seq[m[upper-1]]):
            j=upper
        else:
            while upper-lower>1:
                mid=(upper+lower)//2
                if comp(seq[i],seq[m[mid-1]]):
                    lower=mid
                else:
                    upper=mid
            j=lower
        p[i]=m[j-1]
        if j==l or comp(seq[i],seq[m[j]]):
            m[j]=i
            l=max(l, j+1)
    result=[]
    pos=m[l-1]
    for _ in range(l):
        result.append(seq[pos])
        pos=p[pos]
    return result[::-1]