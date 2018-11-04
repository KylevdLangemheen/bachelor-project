import knn
import scipy
import readdata
import numpy as np
import random
#a test file for showing how to test knn, and also for myself to test my own algorithm
#prints progress

#makes the training data/label set x/y, and testing data/label set xt/yt, based on different parameters
#disregard is only used if there are no requirements on the (frequency of the) labels: disregards part of the dataset
#split decides what part of the used data is train, and what part is test
#normal decides whether each label should appear equally frequently
#TODO: implement non-normal dataset generation by host, rather than on whole dataset
#minimal decides what the minimal amount of datapoints should be for each label when normal = True and hosts = None
#hosts preset host labels that should be used, rather than a minimal function.
def makeHostDataset(data,labels,disregard = 0.0,split = 0.5,normal = False,minimal = 20,hosts = None):
    x,y,xt,yt,labelts = ([] for i in range(5)) #initialise train x and y, and test xt and yt, and extracted host labels labelts
    
    for label in labels:
        labelts.append(label["host"])
    if normal:
        smallestCount = None
        if hosts is None:
            uniques = []
            for host in labelts:
                if host not in uniques:
                    uniques.append(host)
            for unique in uniques:
                if labelts.count(unique) >= minimal:
                    hosts.append(unique)
        if hosts is None:
            print("Error, empty hosts list!")
            exit()
        else:
            for host in hosts:
                count = labelts.count(host)
                if smallestCount is None:
                    smallestCount = count
                else:
                    if smallestCount > count:
                        smallestCount = count
        possibleSets = dict()
        for i in range(len(labelts)):
            if labelts[i] in hosts:
                if labelts[i] in possibleSets.keys():
                    possibleSets[labelts[i]].append(i)
                else:
                    possibleSets[labelts[i]] = [i]
        train = []
        test = []
        for key in possibleSets:
            possible = possibleSets[key]
            sample = random.sample(possible,int(smallestCount*split))
            for item in sample:
                possible.remove(item)
            train += sample
            test += random.sample(possible,int(smallestCount*(1-split)))
        for i in train:
            x.append(data[i])
            e = dict(host=labelts[i])
            y.append(e)
        for i in test:
            xt.append(data[i])
            e = dict(host=labelts[i])
            yt.append(e)
    else:
        for i in range(len(data)):
            if np.random.uniform()<disregard: #ignore most of the data hahahaha
                continue
            if np.random.uniform()<split: #chance of adding it to training or testing set (randomly)
                x.append(data[i])
                e = dict(host=labelts[i])
                y.append(e)
            else:
                xt.append(data[i])
                e = dict(host=labelts[i])
                yt.append(e)


    return (x,y,xt,yt)

dataLocation = "HA_t_complete_human.fasta"
print("reading data")
dataobj = readdata.readData(dataLocation,["host","fasta"])
print("Cleaning labels")
dataobj.cleanHost()
print("separating data and labels")
xfull,yfull = dataobj.sepDataLabels()
print("translating data to phoc")
xfull = dataobj.dataToPhoc(xfull,4,False)

'''
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
    if np.random.uniform()<0.0: #ignore most of the data hahahaha
        continue

    if np.random.uniform()<0.05: #chance of adding it to training or testing set (randomly)
        x.append(xfull[i])
        y.append(yfull[i])
        trainIndexes.append(i)
    else:
        xt.append(xfull[i])
        yt.append(yfull[i])
        testIndexes.append(i)

#print("Train indexes: " + str(trainIndexes))
#print("Test indexes: " + str(testIndexes))
'''
print("Splitting dataset")
x,y,xt,yt = makeHostDataset(xfull,yfull,normal=True,hosts=["Human","Swine","American_Black_Duck","Green_Winged_Teal","Mallard",
"Pintail","Blue_Winged_Teal","Duck","Goose","Chicken","Gull","Equine","Northern_Shoveler","Ruddy_Turnstone","Shorebird","Turkey"])
print("training knn")
knnobj = knn.knn(3,x,y,scipy.spatial.distance.euclidean)

print("testing knn")
correct = 0
tests = len(xt)
#predict every item in the test set and compare the algorithm's answer to its label.
results = open("answers.txt","w")
for i in range(tests):
    xi = xt[i]
    yi = yt[i]
    ans = knnobj.predict1(xi)
    #print("Answer: " + str(ans[0]) + ", reality: " + str(yi["host"]))
    if ans[0] == yi["host"]:
        correct += 1
    else:
        results.write("Answer: " + str(ans[0]) + ", reality: " + str(yi["host"]) + "\n")
    print("Progress " + str((i/tests)*100) + "%", end='\r', flush=True)
print("test complete")
print("Correct = " + str(correct) + "Total = " + str(tests))