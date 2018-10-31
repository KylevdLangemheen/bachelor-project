from nltk.metrics import distance as distance

class knn:
    def __init__(self,k,train,labels,distMeasure = distance.edit_distance):
        #set every "global" variable
        self.k = k
        self.train = train
        self.labels = labels
        self.distMeasure = distMeasure #distance measurement function, needs to always be as function(a,b)!!
    
    #predict 1 datapoint based on k nearest neighbours
    def predict1(self,data):
        nearest = self.getNearest(data) #get k nearest neighbours by index
        hist = [] #list of histograms of votes for labels, each histogram is one label
        for i in range(len(self.labels[0])): hist.append(dict()) #add a histogram for every label
        for i in nearest: #for every nearest neighbour
            #add its labels as votes in the histogram
            label = self.labels[i]
            j = 0
            for key in label.keys():
                value = label[key]
                #print("Key: " + str(key) + ", Value: " + str(value) + ", Index: " + str(j))
                if value in hist[j]:
                    hist[j][value] += 1
                else:
                    hist[j][value] = 1
                j += 1
        answer = [] #list of answer labels made up of the most frequent labels in the histograms
        #print(hist)
        for field in hist: #for every different label
            #get the most frequent value and add that to the answer list
            mostFrequentValue = None
            mostFrequentKey = None
            for key in field.keys():
                if mostFrequentValue is None:
                    mostFrequentValue = field[key]
                    mostFrequentKey = key
                else:
                    if mostFrequentValue < field[key]:
                        mostFrequentValue = field[key]
                        mostFrequentKey = key
            answer.append(mostFrequentKey)
        return answer

    #get the k nearest datapoints
    def getNearest(self,data):
        nearest = []
        indices = list(range(len(self.train))) #get a list of indices from which we can choose our nearest neighbours
        for _ in range(self.k):
            #do this until we found enough neighbours
            closestD = None
            closestI = None
            for index in indices:
                #find the nearest neighbour out of the available datapoints
                #print("Closest so far = " + str(closestI) + ", comparing to: " + str(index))
                compareData = self.train[index]
                d = self.distMeasure(data,compareData)
                if closestD is None:
                    closestD = d
                    closestI = index
                else:
                    if closestD>d:
                        closestD = d
                        closestI = index
            nearest.append(closestI) #add that index to the nearest neighbour index
            indices.remove(closestI) #and remove it from the total list of indices so it won't be selected again
        return nearest
