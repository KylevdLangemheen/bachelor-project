import knn
import scipy
import readdata
import numpy as np
np.random.seed(42)

dataLocation = "HA_t_complete_human.fasta"
print("reading data")
dataobj = readdata.readData(dataLocation,["host","fasta"])
print("Cleaning labels")
dataobj.cleanHuman()
print("separating data and labels")
xfull,yfull = dataobj.sepDataLabels()
print("translating data to phoc")
xfull = dataobj.dataToPhoc(xfull,6)

x = []
y = []
xt = []
yt = []
trainIndexes = []
testIndexes = []
print("separating train and test set")
for i in range(len(xfull)):
    if np.random.uniform()<0.9:
        continue

    if np.random.uniform()>0.5:
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
for i in range(tests):
    xi = xt[i]
    yi = yt[i]
    ans = knnobj.predict1(xi)
    if ans[0] == yi["host"]:
        correct += 1
    print("Progress " + str((i/tests)*100) + "%", end='\r', flush=True)
print("test complete")
print("Correct = " + str(correct) + "Total = " + str(tests))


'''
print("testing knn")
print("knn's answer:")
print(obj.predict1(x[30-1]))
print("Should have been:")
print(y[30-1])
'''