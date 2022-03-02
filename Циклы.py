from geom2d import *

#l = [Point(i, i*i) for i in range (-5, 6)]

l = map(lambda i: Point(i, i*i), range (-5, 6))

l2 = filter(lambda p: p.x % 2 == 0, l)

for el in l2:
    print(el)
