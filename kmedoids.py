import numpy as np
from nltk.metrics import distance as distance
from copy import deepcopy
np.random.seed(123456789)

class kmedoids:
    def __init__(self, k, train, tolerance=1):
        self.k = k
        self.train = train

        #select initial medoids
        self.initMedoids()
        #assign initial points to medoids
        self.assignPoints()

        changed = True
        while changed:
            print("and we loop!")
            changed = False
            previousClusters = deepcopy(self.clusters)
            for clusterID in range(len(self.clusters)):
                for i in range(len(self.train)):
                    if self.isAMedoid(i):
                        continue
                    self.clusters[clusterID]["medoid"] = i
                    self.resetClusters()
                    self.assignPoints()
                    if(self.fitness(self.clusters)<self.fitness(previousClusters)):
                        previousClusters = deepcopy(self.clusters)
                        changed = True
                    else:
                        self.clusters = deepcopy(previousClusters)

    def printClusters(self):
        for cluster in self.clusters:
            print("Medoid = " + str(cluster["medoid"]) + ", members = " + str(cluster["members"]) + ", distance = " + str(cluster["distance"]))
        print("Translated:")
        for cluster in self.clusters:
            names = []
            names.append(self.train[cluster["medoid"]])
            for i in cluster["members"]:
                names.append(self.train[i])
            print(names)
        print("fitness = " + str(self.fitness(self.clusters)))

    def fitness(self,clusters):
        total = 0
        for cluster in clusters:
            total += cluster["distance"]
        return total

    def resetClusters(self):
        for cluster in self.clusters:
            cluster["members"] = []
            cluster["distance"] = 0
                
    def isAMedoid(self,i):
        for cluster in self.clusters:
            if cluster["medoid"]==i:
                return True
        return False
    
    def initMedoids(self):
        self.clusters = []
        for _ in range(self.k):
            cluster = dict()
            cluster["medoid"] = np.random.randint(len(self.train))
            cluster["distance"] = 0
            cluster["members"] = []
            self.clusters.append(cluster)
    
    def assignPoints(self):
        for i in range(len(self.train)):
            if self.isAMedoid(i):
                continue
            bestDistance = None
            bestCluster = None
            for clusterID in range(len(self.clusters)):
                cluster = self.clusters[clusterID]
                d = distance.edit_distance(self.train[i],self.train[cluster["medoid"]])
                if bestDistance is None:
                    bestDistance = d
                    bestCluster = clusterID
                else:
                    if d<bestDistance:
                        bestDistance = d
                        bestCluster = clusterID
            self.clusters[bestCluster]["members"].append(i)
            self.clusters[bestCluster]["distance"] += bestDistance