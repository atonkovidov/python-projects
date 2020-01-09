import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,4)
y1 = x*2
y2 = (x-1)*2
y3 = (x-2)*2
l1 = x
l2 = 1.5*x

x1 = np.arange(-0.25,0.75,0.25)
t1 = x1 - 0.25
x2 = np.arange(0.25,0.75,0.25)
t2 = -x2 + 0.75
t3 = 0.5*x

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#plt.gca().spines['bottom'].set_position('zero')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y1, 'xkcd:light blue', label="$t'$")
plt.plot(0.25, 0.5, 'ro')
plt.plot(-0.25, -0.5, 'ro')
plt.plot(x1, t1, 'y', label="light beam")
plt.plot(x2, t2, 'g')
plt.plot(x, t3, 'xkcd:dark blue', label="new $x'$ axis")
#plt.plot(x, y2, 'b', y3, 'b')
#plt.plot(x, l1, 'y', label='light from M')
#plt.plot(l2, x, 'orange', label='light from N')
plt.tick_params(
    axis='both',          
    which='both',      
    bottom=False,      
    top=False,
    right=False,
    left=False,
    labelleft=False,    
    labelbottom=False)

plt.xlim([-1,1])
plt.ylim([-1,1])
#plt.xticks([0, 1, 2, 3], [r'0', r'3x$10^8$ m', r'6x$10^8$ m', r'9x$10^8$ m'])
#plt.yticks([1, 2, 3], [r'1 sec', r'2 sec', r'3 sec'])
plt.xlabel("     $x$")
plt.ylabel('     $t$')
plt.legend(loc='upper left')
plt.savefig("plot6.png", dpi=96)
#plt.show()