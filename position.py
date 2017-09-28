import math

"""
    I position is just a tuple and here are some useful functions
    operating over them
"""

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def direction(p1, p2):
    return math.degrees(math.atan((p1[1]-p2[1])/(p1[0]-p2[0])))

def slope(p1, p2):
    if p1[0]==p2[0]:
        raise RuntimeError()
    return (p1[1]-p2[1])/(p1[0]-p2[0])

def range_x(p1, p2):
    return sorted((p1[0], p2[0]))

def range_y(p1, p2):
    return sorted((p1[1], p2[1]))
