import math
import matplotlib.pyplot as plt

angles = [i for i in range(0, 361)]

x = []
y = []

for i in angles:
  x = x + [i]
  y = y + [math.sin(i * math.pi / 180)]

plt.plot(x, y)
plt.show()
