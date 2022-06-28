from hashlib import new
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

def scale_down_2(km):
  i = 0
  d_km = []
  while (i < len(km)):
    d_km.append((float(km[i]) - float(min(km))) / (float(max(km)) - float(min(km))))
    i += 1
  return (d_km, 1)

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
[d_km, a_max] = scale_down_2(km)

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

# range = max(km) - min(km)
# teta1 = teta1 * range

normd =  (float(22899) - float(min(km))) / (float(max(km)) - float(min(km)))
test = teta0 + teta1 * normd
print("test = " + str(test))

def get_coef_equation(km, teta0, teta1):
  # On calcule deux points de la droite
  km0 =  (float(min(km)) - float(min(km))) / (float(max(km)) - float(min(km)))
  p0 = teta0 + teta1 * km0
  print("min km = " + str(min(km)) + "    price = " + str(p0))
  km1 =  (float(max(km)) - float(min(km))) / (float(max(km)) - float(min(km)))
  p1 = teta0 + teta1 * km1
  print("max km price = " + str(p1))
  new_teta1 = (p1 - p0) / (max(km) - min(km))
  new_teta0 = (float(0) - float(min(km))) / (float(max(km)) - float(min(km)))
  new_teta0 = teta0 + teta1 * new_teta0
  print("res = " + str(new_teta1))
  return (new_teta0, new_teta1)

print("teta0 = " + str(teta0) + "       teta1 = " + str(teta1))
# teta0 *= max(prices)
# teta1 *= max(km)
# print("teta0 = " + str(teta0) + "       teta1 = " + str(teta1))

[new_teta0, new_teta1] = get_coef_equation(km, teta0, teta1)
print("teta1 = " + str(teta1))
print("new_teta1 = " + str(new_teta1))

x = np.linspace(0, 200000, 200000)
y = new_teta0 + new_teta1 * x
# y = teta0 + teta1 * x
plt.plot(x, y, '-r', label='price = teta0 + teta1 * km')

plt.plot(km, prices, 'ro')
plt.ylabel('price')
plt.xlabel('km')
plt.show()
