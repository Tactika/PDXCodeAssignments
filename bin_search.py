""" def search(xs, target):
    if not xs:
        return - 1
    
    low = 0
    high = len(xs)

    return recurse(xs, target, low, high)
     """
def search(xs, target):
    return -1 if not xs else recurse(xs, target, 0, len(xs) - 1)

def average(a,b):
    return (a + b) // 2 

def recurse(xs, target,low,high):
    midpoint = average(low, high)

    if xs[midpoint] == target:
        return midpoint
    if low == high:
        return -1

    if xs[midpoint] < target: # Less Than
        return recurse(xs, target, midpoint+1, high)
    if xs[midpoint] > target: # Greater Than
        return recurse(xs, target,low, midpoint-1)