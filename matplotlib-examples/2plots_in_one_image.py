import matplotlib.pyplot as plt
import numpy as np

# row, columns, 1st plot
plt.subplot(3,1,1)

#bell curve
x = np.random.normal(0.0,1.0,10000)
plt.hist(x)

#purely random
plt.subplot(3,1,2)
x = np.random.uniform(-3.0,3.0,10000)
plt.hist(x)

plt.subplot(3,1,3)
x = np.random.uniform(-3.0,3.0,10000)
plt.hist(x)

plt.show()


