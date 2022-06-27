import numpy as np
import math 
import matplotlib.pyplot as plt

prices = []
d_prices = []
km = []
d_km = []
iteration = 1000

Lr = 0.1
def read_data():
  outfile = open("data.csv","r")
  data = outfile.readlines()
  # File parsing arranged int two arrays
  for line in data:
    if 'km' not in line:
        words = line.split(",")
        words[1] =words[1][:-1]
        km.append(float(words[0]))
        prices.append(float(words[1]))
  outfile.close()
  return (km, prices)

def scale_down(km):
  a_max = max(km)
  i = 0
  d_km = []
  while i < len(km):
    d_km.append(km[i] / a_max)
    print("d_km = " + str(d_km[i]) + "    km = " + str(km[i]) )
    i += 1
  return (d_km, a_max)

def training(km, prices, iteration):
  LR_m = Lr/len(km)
  teta0 = 0
  teta1 = 0

  j = 0
  while j < iteration:
    sum0 = 0
    sum1 = 0

    i = 0
    while i < len(km):
      sum0 += (teta0 + teta1 * km[i]) - prices[i]
      sum1 += ((teta0 + teta1 * km[i]) - prices[i]) * km[i]
      i += 1

    tmpteta0 = LR_m * sum0
    tmpteta1 = LR_m * sum1

    teta0 -= tmpteta0
    teta1 -= tmpteta1

    j += 1
  return (teta0, teta1)

[km, prices] = read_data()

a_max = 0
[d_km, a_max] = scale_down(km)

# [teta0, teta1] = training(d_km, d_prices, iteration)
[teta0, teta1] = training(d_km, prices, iteration)

def mean_calc(km):
  i = 0
  sum = 0
  while (i < len(km)):
    sum += km[i]
    i += 1
  mean = sum / i
  return (mean)

def std_calc(mean, km):
  i = 0
  std = 0
  while (i < len(km)):
    std += pow((km[i] - mean), 2)
    i += 1
  std = std / i
  std = math.sqrt(std)
  return (std)

ukm = mean_calc(km)

std = std_calc(ukm, km)

# teta0 = teta0 - (ukm/std) * teta1
# teta1 = teta1 / std

# teta1 = teta1 / std



print("teta0 = " + str(teta0) + "       teta1 = " + str(teta1))
# teta0 *= max(prices)
# teta1 *= max(km)
# print("teta0 = " + str(teta0) + "       teta1 = " + str(teta1))

x = np.linspace(0, 2, 2)
y = teta0 + teta1 * x
plt.plot(x, y, '-r', label='price = teta0 + teta1 * km')

plt.plot(d_km, prices, 'ro')
plt.ylabel('price')
plt.xlabel('km')
plt.show()
