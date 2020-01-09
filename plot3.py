import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2)
y1 = x-1
y2 = -x+1
plt.gca().spines['bottom'].set_position('zero')
plt.plot(x, y1, 'y', label='light beam')
plt.plot(x, y2, 'y')
plt.xlim([0,2])
plt.ylim([-2,2])
plt.xticks([0, 1], [r'   0', r'3x$10^8$ m'])
plt.yticks([-1, 0, 1], [r'-1 sec', r'0 sec', r'1 sec'])
plt.xlabel("$x'$")
plt.ylabel("$t'$")
plt.legend(loc='upper center')
plt.savefig("plot3.png", bbox_inches = 'tight', dpi=96)