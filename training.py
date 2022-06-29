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
  try:
    outfile = open("data.csv", "r")
  except IOError:
    return (-2, -1)

  data = outfile.readlines()
  # File parsing arranged int two arrays
  for line in data:
    if 'km' not in line:
        words = line.split(",")
        if (len(words) == 2 and (words[0] != "" and words[0] != '\n') and (words[1] != "" and words[1] != '\n')):
          km.append(float(words[0]))
          prices.append(float(words[1]))
        else:
          return (-1, -1)
  outfile.close()
  return (km, prices)

def write_data(new_theta0, new_theta1):
  try:
    file = open("thetas.csv", "w")
  except IOError:
     print ("Error: permission denied: 'thetas.csv'. No data written")
     return
  file.write("theta0," + str(new_theta0) + '\n' + "theta1," + str(new_theta1) + '\n')
  file.close()

def scale_down(km):
  i = 0
  d_km = []
  while (i < len(km)):
    d_km.append((float(km[i]) - float(min(km))) / (float(max(km)) - float(min(km))))
    i += 1
  return (d_km)

def training(km, prices, iteration):
  LR_m = Lr/len(km)
  theta0 = 0
  theta1 = 0
  j = 0
  while j < iteration:
    sum0 = 0
    sum1 = 0
    i = 0
    while i < len(km):
      sum0 += (theta0 + theta1 * km[i]) - prices[i]
      sum1 += ((theta0 + theta1 * km[i]) - prices[i]) * km[i]
      i += 1
    tmptheta0 = LR_m * sum0
    tmptheta1 = LR_m * sum1
    theta0 -= tmptheta0
    theta1 -= tmptheta1
    j += 1
  return (theta0, theta1)

def descale_thetas(km, theta0, theta1):
  # On calcule deux points de la droite
  km0 =  (float(min(km)) - float(min(km))) / (float(max(km)) - float(min(km)))
  p0 = theta0 + theta1 * km0
  km1 =  (float(max(km)) - float(min(km))) / (float(max(km)) - float(min(km)))
  p1 = theta0 + theta1 * km1
  # On calcule le coef directeur
  new_theta1 = (p1 - p0) / (max(km) - min(km))
  # On calcule l'ordonne a l'origine
  new_theta0 = (float(0) - float(min(km))) / (float(max(km)) - float(min(km)))
  new_theta0 = theta0 + theta1 * new_theta0
  return (new_theta0, new_theta1)

def error_calc(prices, km, new_theta0, new_theta1):
  i = 0
  error = 0
  while (i < len(prices)):
    error += (prices[i] - (new_theta0 + new_theta1 * km[i])) ** 2
    i += 1
  error = error / len(prices)
  error = math.sqrt(error)
  return (error)


def main():
  [km, prices] = read_data()
  if (km == -1):
    print("data.csv is crrupted")
    return
  elif (km == -2):
    print ("Error: no such file: 'data.csv'")
    return

  d_km = scale_down(km)
  [theta0, theta1] = training(d_km, prices, iteration)
  [new_theta0, new_theta1] = descale_thetas(km, theta0, theta1)
  write_data(new_theta0, new_theta1)
  error = error_calc(prices, km, new_theta0, new_theta1)

  plt.text(max(km) * 0.7,max(prices) * 0.9,'Error : ' + str(error))
  x = np.linspace(min(km), max(km), max(km) - min(km))
  y = new_theta0 + new_theta1 * x
  plt.plot(x, y, '-b', label='price = theta0 + theta1 * km')

  plt.plot(km, prices, 'ro')
  plt.ylabel('price')
  plt.xlabel('km')
  plt.show()
  return

main()
