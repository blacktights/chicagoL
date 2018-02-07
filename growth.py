###
# growth.py
#
# Purpose: this script processes annual sum of ridership at each Chicago L station, and
# fits a linear regression model, in order to use the model coefficient as a proxy for
# anual ridership growth rate.
#
# Input file: (hardcoded) file named rides.csv, with Station ID, Year, and Sum # Rides.
# Output file: (hardcoded) file named growth.csv, with Station ID, Model Coefficient, and
# quartile assignment of each station's growth rate
# 
# History
# 02/05/2018   Erika Lee	Created
#
# Known issues
# - Don't hardcode input and output files.
# - Quartile assignment should be 4-3-2-1 (higher number has higher growth rate).
###

import csv
from sklearn import linear_model
import numpy as np

station, year, rides = np.genfromtxt('rides.csv',delimiter=',',skip_header=1,unpack=True)

length = np.where(station[:-1] != station [1:])[0] + 1
start = 0
stations = []

# Fit linear regression model to each station's annual ridership volume
coef =[]
for end in length:
	x = year[start:end]
	y = rides[start:end]
	model = np.polyfit(x, y, 1)
	stations.append(int(station[start]))
	coef.append(model[0])
	start = end

coef = np.array(coef)
percentile75 = np.percentile(coef,75)
median= np.percentile(coef,50)
percentile25= np.percentile(coef,25)

# Assign quartile to each station based on their growth rate (model coefficient)
quartile = []
for c in coef:
	if c >= percentile75:
		quartile.append(1)
	elif c >= median:
		quartile.append(2)
	elif c >= percentile25:
		quartile.append(3)
	else:
		quartile.append(4)

output = open('growth.csv', 'w')
output.write('Station Id' + '\t' + 'Coef' + '\t' + 'Quartile' + '\n')
for i in range(len(stations)):
	output.write(str(stations[i]) + '\t' + str(coef[i]) + '\t' + str(quartile[i]) + '\n')

