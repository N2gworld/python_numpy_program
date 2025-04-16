import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.subplot(3,1,1)
plt.plot(x,y)
plt.title('Sine')

plt.subplot(3,1,2)
plt.plot(x,z)
plt.title('cosine')

plt.subplot(3,1,3)
plt.plot(x,z)
plt.title('cosine')

plt.show()