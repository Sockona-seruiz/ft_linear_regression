import numpy as np
import matplotlib.pyplot as plt

outfile = open("teta.csv","r")
data = outfile.readlines()
for line in data:
  words = line.split(",")
  words[1] =words[1][:-1]
  if 'teta0' in line:
    teta0 = int(words[1])
  else:
    teta1 = int(words[1])
outfile.close()

print("teta0 = " + str(teta0))
print("teta1 = " + str(teta1))