import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import crystalball
import uproot
import numpy as np
import math

factor = 0.5;
input_file = uproot.open("trkana.Triggered.root")
input_tree = input_file["TrkAnaNeg/trkana"]
df = input_tree.pandas.df(flatten = False)
file2 = uproot.open("reco-Delta40-trig.root")
RPCReco2 = file2["TrkAnaNeg/trkana"]
df2 = RPCReco2.pandas.df(flatten=False)

data1 = df["deent.mom"]#background
data2 = df2["deent.mom"]#signal

reconstructData = []

(counts, bins) = np.histogram(data2, bins = 200, range = (0,80))

#print(counts)
print(len(bins))
n1, bins1, patches1 = plt.hist(bins[:-1], bins, weights = factor*counts)
print(len(n1))

numbins = 200;
range1 = 80;
n2, bins2, patches2 = plt.hist(data1, bins = numbins, range = (0,80))
print(n2[100])
print(n1[100])
current = 0;
for i in range(len(n1)):
    n1[i] += n2[i]
    for number in range(n1[i].astype(np.int64)):
        reconstructData.append((current + 0.000000000000001))

    current += (range1/numbins);

print(n1[100])

bins = 200
range = 80

print(reconstructData)

plt.hist(reconstructData, bins = 200, range = (0,80),  label="Reduced Signal + Spectrum")

plt.show()