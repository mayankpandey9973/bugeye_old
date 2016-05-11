import matplotlib.pyplot as plt
import numpy as np
from time import sleep


def setup_backend(backend='TkAgg'):
    import sys
    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl
    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt
    return plt

def animate():
    # http://www.scipy.org/Cookbook/Matplotlib/Animations
    mu, sigma = 100, 15
    N = 4
    x = mu + sigma * np.random.randn(N)
    print x
    testLabels = ['a','b','c','d']
    #http://matplotlib.org/api/pyplot_api.html
    #http://matplotlib.org/examples/pylab_examples/barchart_demo2.html
    #atplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
    #rects = plt.bar(range(N), x, bottom = ['a','b','c','d'], align='center')
    rects = plt.bar(range(N), x, align='center',tick_label=testLabels)
    
    for i in range(50):
        x = mu + sigma * np.random.randn(N)
        print x
        for rect, h in zip(rects, x):
            sleep(0.05)
            rect.set_height(h)

        fig.canvas.draw()

plt = setup_backend()
fig = plt.figure()
win = fig.canvas.manager.window
win.after(10, animate)
plt.show()
