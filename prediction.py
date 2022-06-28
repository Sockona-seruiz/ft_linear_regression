import numpy as np
import matplotlib.pyplot as plt

outfile = open("thetas.csv","r")
data = outfile.readlines()
for line in data:
  words = line.split(",")
  words[1] =words[1][:-1]
  if 'theta0' in line:
    theta0 = float(words[1])
  else:
    theta1 = float(words[1])
outfile.close()

km = input("Enter a mileage : ")
price = theta0 + theta1 * km

print("The estimated price for your vehicule is : " + str(price))
