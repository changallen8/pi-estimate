import random as r
import math as m
import matplotlib.pyplot as plt

inside = 0
total = 10000

fig, ax = plt.subplots(1)

plt.axis([-1, 1, -1, 1])
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.gca().set_aspect('equal', adjustable='box')
draw_circle = plt.Circle((0, 0), 1, fill=False)
plt.gcf().gca().add_artist(draw_circle)

for i in range(1, total + 1):
    x = r.uniform(-1, 1)
    y = r.uniform(-1, 1)
    if m.sqrt((x ** 2) + (y ** 2)) <= 1:
        inside += 1.0
        plt.scatter(x, y, c='blue')
    else:
        plt.scatter(x, y, c='black')
    pi = (inside/float(i)) * 4
    plt.title("pi " + r'$\approxeq$' + " " + str(pi))
    plt.pause(0.005)

plt.show()

print(pi)
