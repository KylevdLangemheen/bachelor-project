import kmedoids

dataLocation = "HA_t_complete_all.fasta"

dataFile = open(dataLocation,"r")

'''
words = ['apple', 'Doppler', 'applaud', 'append', 'barker', 
         'baker', 'bismark', 'park', 'stake', 'steak', 'teak', 'sleek']

print("Running kmedoids!")
test = kmedoids.kmedoids(3,words)
print("Printing results!")
test.printClusters()
'''

lines = dataFile.readlines()[1:44:2]

print("Running kmedoids!")
test = kmedoids.kmedoids(3,lines)
print("Printing results!")
test.printClusters()
