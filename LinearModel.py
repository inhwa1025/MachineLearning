'''in Pytorch'''
import torch
import numpy as np
import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4]
y_data = [200000, 270000, 340000, 410000]

w = 100000

def forward(x):
  return x * w

def loss(x, y):
  y_pred = forward(x)
  return (y_pred - y) * (y_pred - y)

w_list = []
mse_list = []

for w in np.arange(0.0, 410000, 10000):
  l_sum = 0

  for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    l = loss(x_val, y_val)
    l_sum += l

  w_list.append(w)
  mse_list.append(l_sum / 3)

plt.plot(w_list, mse_list)
plt.ylabel('Cost')
plt.xlabel('w')
plt.show()
