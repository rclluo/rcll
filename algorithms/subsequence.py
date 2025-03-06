"""
Subsequence related things
"""

def lis(seq,comp=lambda a,b:a>b):
    """
    Longest Increasing Subsequence
    """
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

def lcs(a: list, b: list):
    """
    Longest Common Subsequence
    """
    m=len(a)
    n=len(b)
    l = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    index = l[m][n]

    dp = [""] * (index+1)
    dp[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if a[i-1] == b[j-1]:
            dp[index-1] = a[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif l[i-1][j] > l[i][j-1]:
            i -= 1
        else:
            j -= 1
    return dp