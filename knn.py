from nltk.metrics import distance as distance

class knn:
    def __init__(self,k,train,labels):
        self.k = k
        self.train = train
        self.labels = labels
    
    def predict1(self,data):
        nearest = self.getNearest(data)
        
        for i in nearest:
            neighbour = self.train[i]
            for key in neighbour.keys:
                if key == "fasta":
                    break
                

        return

    def getNearest(self,data):
        nearest = []
        indices = []
        for i in range(len(self.train)):
            indices.append(i) #VERY HACKY, find a better way to add these numbers to an array!!
        for _ in range(self.k):
            closestD = None
            closestI = None
            for index in indices:
                compareData = self.train[index]
                d = distance.edit_distance(data,compareData)
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
