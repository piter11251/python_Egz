import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, (x**2)+4, color='orange', label='y=x^2+4', linestyle='--')
ax2.plot(x, -(x**2)-6, color='green', label='y=x^2-6', linestyle='-.')
ax1.set_ylabel('oś pionowa po lewej stronie', color='purple')
ax2.set_ylabel('oś pionowa po prawej stronie', color='orange')
ax1.set_xlabel('oś pozioma', color='pink')
plt.title('Wykresy dwóch funkcji liniowych - wzory Latex')
ax1.legend(loc=2)
ax2.legend(loc=1)
ax1.grid()
plt.savefig('zad1fk.jpg')
plt.show()