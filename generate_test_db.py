import random
import sys
import numpy as np

outfile = open('db.json', 'w+')

dataSet = np.genfromtxt('accel_data.csv', delimiter=',')

jsonText = "{\"date\": \"2016-10-16T07:45:30\", \"name\": \"Jackie Wolfe\", \"weight\": 30.4, \"time\":["
for data in dataSet:
    jsonText +=  "\"" + str(data[0]) + "\","
jsonText = jsonText[:-1]
jsonText += "], \"accel\":["
for data in dataSet:
    jsonText +=  "\"" + str(data[1]) + "\","
jsonText = jsonText[:-1] 
jsonText += "]}"

outfile.write(jsonText)
outfile.close()
