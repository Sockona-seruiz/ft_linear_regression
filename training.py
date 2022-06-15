import numpy as np
import matplotlib.pyplot as plt

prices = []
km = []
teta0 = 0
teta1 = 0

tmpteta0 = 0
tmpteta1 = 0

Lr = 0.1

outfile = open("data2.csv","r")
data = outfile.readlines()
# File parsing arranged int two arrays
for line in data:
  if 'km' not in line:
      words = line.split(",")
      words[1] =words[1][:-1]
      km.append(float(words[0]))
      prices.append(float(words[1]))
      print("km = " + words[0] + "    price = " + words[1])
outfile.close()

j = 0
LR_m = Lr/len(km)

while j < 100:
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


# print("tmpteta0 = " + str(tmpteta0))
# print("tmpteta1 = " + str(tmpteta1))
print("teta0 = " + str(teta0))
print("teta1 = " + str(teta1))

x = np.linspace(0,2,2)
y = teta0 + teta1 * x
plt.plot(x, y, '-r', label='price = teta0 + teta1 * km')

plt.plot(km, prices, 'ro')
plt.ylabel('price')
plt.xlabel('km')
plt.show()   
