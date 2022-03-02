from geom2d import *


l1 = [Point(5, 1), Point(4, 5), Point(2, 2)]

l2 = sorted(l1, cmp=lambda p1, p2: cmp(p1.y, p2.y))

print(l2)


