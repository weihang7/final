import numpy as np
import csv

for DELAY in range(10):
    print "DELAY: " + str(DELAY)
    x = []
    y = []
    dates = set()
    with open('data2.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dates.add(row[2])
            y.append([(int(row[7])+int(row[8]))/20])
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2] in dates:
                x.append([int(row[7])/10])

    bad = 0
    for i in range(len(y)):
        if y[i-bad] == -1000:
            x.pop(i)
            y.pop(i-bad)
            bad += 1

    x = np.matrix(x[DELAY:])
    a = np.matrix(np.zeros((1, 1)))
    if DELAY != 0:
        y = np.matrix(y[:-DELAY])
    else:
        y = np.matrix(y)

    for row in x:
        a += row.getT() * row

    print x.shape
    print a.shape
    print y.shape
    beta = a.getI() * x.getT() * y
    print beta
    y_hat = x * beta

    mse = 0
    for idx in range(len(y)):
        mse += (y[idx] - y_hat[idx]) ** 2

    print mse / (len(y) - 1)

"""
with open('lr.dat', 'w') as f:
    out = ""
    for i in range(len(y)):
        out += str(x.item((i, 0))) + ' ' + str(y.item((i, 0))) + ' ' + str(y_hat.item((i, 0))) + "\n"
    f.write(out)
"""
