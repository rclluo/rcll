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