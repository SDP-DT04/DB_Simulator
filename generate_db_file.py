import random
import sys
import derivative
import matplotlib.pyplot as plt

outfile = open('db.json', 'w+')

# build array of last names
infile = open('first_names.txt', 'r') 
first_names = (infile.read()).split('\n')
first_names.pop()
infile.close()

# build array of first names
infile = open('last_names.txt', 'r')
last_names = (infile.read()).split('\n')
last_names.pop()
infile.close()

for entry in range(0, int(sys.argv[1])):
    firstName = first_names[random.randint(0,19)]
    lastName = last_names[random.randint(0,20)]

    totTime = random.randint(8000, 15000)

    date = random.randint(1473690000, 1473726191)

    weight = random.randint(0, 100)
    while weight % 5 != 0:
        weight += 1

    position = []
    time = 0
    i = 0
    position.append(round(random.random() / 5, 3))
    while time < totTime:
        position.append(round(position[i] + random.random() / 5, 3))
        time += 100
        i += 1

    velocity = derivative.derivative(position)
    accel = derivative.derivative(velocity)

    outfile.write("{\"date\": " + str(date) + ", \"name\": \"" + firstName + " " + lastName + "\", " + "\"weight\": " + str(weight) + ", \"tot_time\": " + str(totTime) + " , \"position\": [")
    for val in position: 
        outfile.write(" \"" + str(val) + "\", ")
    outfile.write("\"" + str(position[len(position)-1]) + "\"" + ", \"accel\": [")

    for val in accel: 
        outfile.write(" \"" + str(round(val,3)) + "\", ")
    outfile.write("\"" + str(round(accel[len(accel)-1], 3)) + "\"]}\n")
outfile.close()
#plt.plot(accel)
#plt.show()
