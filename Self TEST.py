from geom2d import *

l = []

for i in range(90):
   l.append(Point(i+777, i*(i+356343)))

for el in l:
   print(el)

print(l)