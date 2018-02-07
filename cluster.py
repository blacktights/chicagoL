###
# cluster.py
#
# Purpose: this script takes daily ridership volume at each Chicago L station as features, 
# and clusters the stations using agglomerative clustering. The hope is to be able to 
# cluster stations based on fluctuating patterns (e.g. higher volume during weekend)
#
# Input file: (hardcoded) file named 2017rides2.csv, with Station ID, Date, and # Rides.
# Output file: (hardcoded) file named cluster.csv, with Station ID, and cluster assignment 
# 
# History
# 02/05/2018   Erika Lee	Created
#
# Known issues
# - Don't hardcode input and output files.
# - Cosine and manhanttan distance doesn't seem to yield very useful clusters (very 
# unbalanced), although I would have expected those affinity metrics to be able to capture # fluctuating patterns.
###


import csv
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

rides = np.genfromtxt('2017rides2.csv',delimiter=',')
stations = rides [:,0]
rides = rides[:,1:]
rides = normalize(rides,axis=1)
model = AgglomerativeClustering(n_clusters=2)
model.fit(rides)
print stations[0]
print model.labels_[0]

output = open('cluster.csv', 'w')
output.write('Station Id' + '\t' +'Cluster' + '\n')
for i in range(len(stations)):
	output.write(str(int(stations[i])) + '\t' +str(model.labels_[i]) + '\n')
