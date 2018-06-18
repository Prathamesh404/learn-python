#! /usr/bin/env python3

import math
def area(r):
    """Area of a circel with radius r"""
    return math.pi *( r**2)

radii = [3, 6.7, 8, 93, 8.34]

# Method 1(without map)
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

#Method 2 : Use "map" function

areass = list(map(area, radii))
print(areas)
print(areass)

