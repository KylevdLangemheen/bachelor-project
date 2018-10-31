from nltk.metrics import distance as distance

class knn:
    def __init__(self,k,train,labels,distMeasure = distance.edit_distance):
        self.k = k
        self.train = train
        self.labels = labels
        self.distMeasure = distMeasure
    
    def predict1(self,data):
        nearest = self.getNearest(data)
        hist = []
        for i in range(len(self.labels[0])): hist.append(dict())
        for i in nearest:
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
        answer = []
        #print(hist)
        for field in hist:
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

    def getNearest(self,data):
        nearest = []
        indices = list(range(len(self.train)))
        for _ in range(self.k):
            closestD = None
            closestI = None
            for index in indices:
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
            nearest.append(closestI)
            indices.remove(closestI)
        return nearest
