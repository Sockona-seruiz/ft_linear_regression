import numpy as np
import matplotlib.pyplot as plt

theta0 = None
theta1 = None


def main():
  try:
    outfile = open("thetas.csv", "r")
  except IOError:
    print ("Error: no such file: 'thetas.csv'")
    return (1)

  data = outfile.readlines()
  for line in data:
    if (len(line) > 0):
      words = line.split(",")
      if 'theta0' in line:
        theta0 = float(words[1])
      elif 'theta1' in line:
        theta1 = float(words[1])
  outfile.close()

  if ((theta0 == None) or (theta1 == None)):
    print("thetas.csv is corrupted")

  km = input("Enter a mileage : ")
  price = theta0 + theta1 * km

  print("The estimated price for your vehicule is : " + str(price))

main ()
