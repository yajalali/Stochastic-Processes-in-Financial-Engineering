# -*- coding: utf-8 -*-
"""jalali-task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YAeQcJzxnIaY_RegrNXcvk5rkfeoINFB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parameters
n_steps = 10
n_paths = 10
start_position = 100

# simple random walk (srw)
simple_random_walk = np.zeros((n_steps+1,n_paths))
simple_random_walk[0,:] = start_position
for i in range(1,n_steps+1):
  step = np.random.choice([-1,1],n_paths) #choose step of -1 or 1 randomly
  simple_random_walk[i] = simple_random_walk[i - 1,:] + step
pd.DataFrame(simple_random_walk)