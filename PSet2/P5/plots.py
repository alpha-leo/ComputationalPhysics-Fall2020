#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


lengths = np.array([10, 50, 100, 150, 200, 250])
t_s = np.array([32, 3072, 16384, 49152, 131072, 1048276])
w_s = np.array([0.6, 1.1, 1.678, 2.725, 2.789, 3.558])

def full_log_plot(x, y, name):
    """
    plot x vs. y as full log
    """
    plt.plot(x, y, 'go--')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(name + ".jpg", bbox_inches='tight')
    plt.close()


def full_log_optimize(x, y):
    """
    return fitted plot vals with sdtev as error
    """
    x = np.log10(x)
    y = np.log10(y)
    popt, pcov = np.polyfit(x, y, 1, full=False, cov=True)
    return popt, np.sqrt(np.diag(pcov))


print("width vs. time")
full_log_plot(t_s, w_s, "beta")
popt, pcov = full_log_optimize(t_s, w_s)
print("beta is: %.2f" % popt[0], " (+/-) %.2f" % pcov[0])
beta = popt[0]

print("width vs. time")
full_log_plot(lengths, t_s, "z")
popt, pcov = full_log_optimize(lengths, t_s)
print("z is: %.2f" % popt[0], " (+/-) %.2f" % pcov[0])
z = popt[0]
print("Means that alpha is: ", z / beta)
