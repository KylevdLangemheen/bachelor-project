import numpy as np
from keras.utils import to_categorical
import readdata

def oneHot(c):
    onehot = [0] * 26
    onehot[ord(c)-65] = 1
    return onehot

plvlmax = 15

inp = "HA_t_complete_some.fasta"
outp = "phocs/phoc"

dataobj = readdata.readData(inp)
x, y = dataobj.sepDataLabels()

for lvl in range(11,plvlmax+1):
    print("level = " + str(lvl))
    phocs = dataobj.dataToPhoc(x,lvl)
    goal = open(outp + str(lvl) + ".txt","w")
    for i in range(len(phocs)):
        line = str(phocs[i]).replace(",","")[1:-1] + " "
        labels = y[i]
        for key in labels.keys():
            line += str(labels[key]) + " "
        line = line[:-1] + "\n"
        goal.write(line)
    goal.close()