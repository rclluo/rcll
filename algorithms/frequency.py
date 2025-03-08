"""
Frequency Array
"""

def freq(ls: list, key=lambda a:a):
    ret={}
    for i in ls:
        k=key(i)
        if k in ret:
            ret[k]+=1
        else:
            ret[k]=1
    return ret