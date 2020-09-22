# y(t) = y(t-1) +e
import numpy as np
import matplotlib.pyplot as plt
y = 0
T = 500
x =0
for t in range(T):
    e = np.random.randint(-100, 100, 1)
    y = y + e
    x = np.append(x,y)
b = np.array(list(range(0,T+1)))
plt.plot(b,x)
plt.show()