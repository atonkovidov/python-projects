import numpy as np
import matplotlib.pyplot as plt

x = np.arange(4)
y1 = x*2
y2 = (x-1)*2
y3 = (x-2)*2
plt.plot(x, y1, 'xkcd:light blue', label="$t'$")
plt.plot(x, y2, 'b', y3, 'b')
plt.axhline(y=1, color='b', linestyle='--')
plt.axhline(y=2, color='b', linestyle='--')
plt.axhline(y=3, color='b', linestyle='--')
plt.xlim([0,3])
plt.ylim([0,3])
plt.xticks([0, 1, 2, 3], [r'0', r'3x$10^8$ m', r'6x$10^8$ m', r'9x$10^8$ m'])
plt.yticks([1, 2, 3], [r'1 sec', r'2 sec', r'3 sec'])
plt.grid(True)
plt.xlabel("$x$/$x'$")
plt.ylabel('$t$')
plt.legend(loc='upper left')
plt.savefig("plot1.png", dpi=96)
