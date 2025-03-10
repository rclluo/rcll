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
