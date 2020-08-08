import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 50)
y = np.exp(np.sin(x))
plt.figure()
plt.plot(x,y)
plt.show()