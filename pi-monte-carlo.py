import random as r
import math as m

inside = 0
total = 10000

for i in range(0, total):
    x = r.random() ** 2
    y = r.random() ** 2
    if m.sqrt(x + y) <= 1:
        inside += 1.0

pi = (inside/total) * 4

print(pi)
