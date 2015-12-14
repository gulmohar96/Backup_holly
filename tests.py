# import random
# walker_path = []
# tot_rooms = 10
# for i in range(0,tot_rooms):
#     print('YAY')
#     path = random.randint(0,tot_rooms)
#     walker_path.append(path)
#     # walker_path += 1
# print(walker_path)


##_____________HAS SOME MAGIC SHIT GOING ON__________##
# %matplotlib inline
# from IPython.core.pylabtools import figsize
# import numpy as np
# from matplotlib import pyplot as plt
# figsize(11, 9)
#
# import scipy.stats as stats
#
# dist = stats.beta
# n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
# data = stats.bernoulli.rvs(0.5, size=n_trials[-1])
# x = np.linspace(0, 1, 100)
#
# # For the already prepared, I'm using Binomial's conj. prior.
# for k, N in enumerate(n_trials):
#     sx = plt.subplot(len(n_trials) / 2, 2, k + 1)
#     plt.xlabel("$p$, probability of heads") \
#         if k in [0, len(n_trials) - 1] else None
#     plt.setp(sx.get_yticklabels(), visible=False)
#     heads = data[:N].sum()
#     y = dist.pdf(x, 1 + heads, 1 + N - heads)
#     plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
#     plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
#     plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)
#
#     leg = plt.legend()
#     leg.get_frame().set_alpha(0.4)
#     plt.autoscale(tight=True)
#
#
# plt.suptitle("Bayesian updating of posterior probabilities",
#              y=1.02,
#              fontsize=14)
#
# plt.tight_layout()

##______________MATPLOTLIB TEST 1_____________##
#from pylab import *
#plot([1,2,3])
#show()


##______________MATPLOTLIB TEST 1_____________##
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   interval=50, blit=True)
#line_ani.save('lines.mp4')

fig2 = plt.figure()

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(15):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
                                   blit=True)
#im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()