import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


def draw_normal(mean, std=1, **kwargs):
    x = np.linspace(mean - 5 * std, mean + 5 * std, 100)
    y = scipy.stats.norm.pdf(x, mean, std)

    plt.plot(x, y, marker='o', **kwargs)


draw_normal(-5, 2, color='red', label='task-1')
draw_normal(5, 2, color='green', label='task-2')
plt.arrow(0, 0.01, -2, 0.1, color='red', width=0.003, head_length=1)
plt.arrow(0, 0.01, 2, 0.1, color='green', width=0.003, head_length=1)

plt.arrow(-1.5, 0.2, -2, 0, color='red', width=0.001, head_length=1)
plt.arrow(1.5, 0.2, 2, 0, color='green', width=0.001, head_length=1)

plt.text(0.5,
         0.3,
         "MAML",
         fontsize='12',
         horizontalalignment='center',
         verticalalignment='center',
         transform=plt.gca().transAxes)

plt.text(0.5,
         0.8,
         "pretrain ?",
         fontsize='12',
         horizontalalignment='center',
         verticalalignment='center',
         transform=plt.gca().transAxes)

plt.xlim(-10, 10)
plt.ylim(0, 0.25)
plt.legend()

# plt.show()
plt.savefig("img/nutshell.png")
