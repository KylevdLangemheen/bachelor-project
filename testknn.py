import knn
import scipy
import readdata
import numpy as np
np.random.seed(42)

#a test file for showing how to test knn, and also for myself to test my own algorithm
#prints progress

dataLocation = "HA_t_complete_human.fasta"
print("reading data")
dataobj = readdata.readData(dataLocation,["host","fasta"])
print("Cleaning labels")
dataobj.cleanHuman()
print("separating data and labels")
xfull,yfull = dataobj.sepDataLabels()
print("translating data to phoc")
xfull = dataobj.dataToPhoc(xfull,6)

#x and y are training data and training labels, xt and yt are test data and test labels, respectively
x = []
y = []
xt = []
yt = []
#keep track of the indexes for debugging purposes
trainIndexes = []
testIndexes = []
print("separating train and test set")
for i in range(len(xfull)):
    if np.random.uniform()<0.9: #ignore most of the data hahahaha
        continue

    if np.random.uniform()<0.5: #chance of adding it to training or testing set (randomly)
        x.append(xfull[i])
        y.append(yfull[i])
        trainIndexes.append(i)
    else:
        xt.append(xfull[i])
        yt.append(yfull[i])
        testIndexes.append(i)

#print("Train indexes: " + str(trainIndexes))
#print("Test indexes: " + str(testIndexes))

print("training knn")
knnobj = knn.knn(1,x,y,scipy.spatial.distance.euclidean)

print("testing knn")
correct = 0
tests = len(xt)
#predict every item in the test set and compare the algorithm's answer to its label.
for i in range(tests):
    xi = xt[i]
    yi = yt[i]
    ans = knnobj.predict1(xi)
    if ans[0] == yi["host"]:
        correct += 1
    print("Progress " + str((i/tests)*100) + "%", end='\r', flush=True)
print("test complete")
print("Correct = " + str(correct) + "Total = " + str(tests))
