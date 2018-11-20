import knn
import scipy
import readdata
import numpy as np
import random

ksetting  = 1
phoclevel = 3

#a test file for showing how to test knn, and also for myself to test my own algorithm
#prints progress

mammal = ["Sea_Mammal","Human","Swine","Dog","Domestic_Cat","Large_Cat","Civet","Bat","Donkey","Equine","Horse","Ferret","Flat_Faced_Bat",
"Sloth","Panda","Lion","little_yellow_shouldered_bat","mink","Mink","Weasel","Muskrat","Rat","Pika","Plateau_Pika","Raccoon_Dog","Skunk",
"sloth_bear","tiger","Camel"]

bird = ["Adelie_Penguin","African_Starling","African_Stonechat","American_Black_Duck","American_Coot","Coot","Avian","Green_Winged_Teal",
"American_Green_Winged_Teal", "Eurasian_Teal","Mallard","Oystercatcher","American_White_Pelican","American_Wigeon","American_Widgeon",
"Northern_Pintail","Green_Winged_Teal_","Cinnamon_Teal","Blue_Winged_Teal_","Blue_Winged_Teal","Duck","Goose","Waterfowl","Crane",
"Aquatic_Bird","Bird","Grey_Heron","Australian_Shelduck","Pochard","Baikal_Teal","Bald_Eagle","Bantam","Bar_Headed_Goose","Barn_Swallow",
"Barnacle_Goose","Bewick's_Swan","Bewick'S_Swan","Chicken","Black_Duck","Black_Headed_Gull","Black_Scoter","Skimmer","Swan","Black_Billed_Magpie",
"Heron","Gull","Black_Legged_Kittiwake","Black_Neck_Crane","Black_Necked_Grebe","Black_Necked_Stilt","Godwit","Blackbird","Flycatcher",
"Finch","Breeder_Duck","Broiler_Duck","Brown_Headed_Gull","Budgerigar","Bufflehead","Bulbul","Common_Buzzard","California_gull",
"Canada_Goose","Canvasback","Crow","Teal","Pigeon","Silky_Chicken","Yellow_Billed_Teal","Chinese_Francolin","Babbler","Chinese_Pond_Heron",
"Penguin","Chukar","Common_Coot","Cormorant","Common_Eider","Common_Goldeneye","Mew_Gull","Common_Iora_","Kestrel","Moorhen","Common_Murre",
"Common_Myna","Common_Pochard","Common_Scoter","Shelduck","Condor","Parrot","Hawk","Eagle","Crested_Myna","Whooper_Swan","Mute_Swan",
"Cygnus_Olor","Double_Crested_Cormorant","Dove","Muscovy_Duck","Dunlin","Eagle_Owl","Eastern_Buzzard","Egret","Tern","Emu","Eurasian_Coot",
"Curlew","Eurasian_Eagel_Owl","Eurasian_Wigeon","European_Herring_Gull","Fairy_Bluebird","Falcon","Feral_Pigeon","Fowl","Franklin's_Gull",
"Gadwall","Garganey","Guineafowl","Glaucous_Gull","Golden_Pheasant","Common_Merganser","Goshawk","Plover","Gray_Teal","Grey_Crowned_Crane",
"Great_Barbet","Great_Black_Headed_Gull","Great_Crested_Grebe","Grebe","Great_Horned_Owl","Greater_Scaup","Greater_White_Fronted_Goose",
"Green_Peafowl","Spot_Billed_Duck","Grey_Faced_Buzzard","Greylag_Goose","Guillemot","Guinea_Fowl","Guinea","Helmeted_Guineafowl","Herring_Gull",
"Myna","Black_Winged_Stilt","Hooded_Merganser","Horned_Puffin","Houbara_Bustard","House_Crow","Iceland_Gull","Peafowl","Japanese_Quail",
"Quail","Japanese_White_Eye","Kalij_Pheasant","Kelp_Gull","Knot","Laughing_Gull","Least_Sandpiper","Lesser_Kestrel","Lesser_Scaup",
"Lesser_Snow_Goose","Snow_Goose","Little_Egret","Little_Grebe","Little_Tern","Long_Tailed_Duck","Macaw","Magpie_Robin","Mallard_Duck",
"Mallard_Black_Duck_Hybrid","Stork","Smew","Murre","Loriinae","Northern_Shoveler","Northern_Shov","Openbill_Stork","Ostrich","Owl",
"Pacific_Golden_Plover","Parakeet","Partridge","Peacock","Pekin_Robin","Pelican","Peregrine_Falcon","Pheasant","Magpie","Pink_Footed_Goose",
"Pintail","Pintail_Duck","Poultry","Red_Crested_Pochard","Red_Knot","Red_Billed_Teal","Red_Necked_Stint","Redhead_Duck","Redhead","Rhea",
"Ring_Necked_Duck","Ring_Billed_Gull","Rook","Rosy_Billed_Pochard","Ruddy_Turnstone","Rufous_Necked_Stint","Ibis","Saker_Falcon","Sanderling",
"Sandpiper","Munia","Scaup","Scoter","Semipalmated_Sandpiper","Stint","Sharp_Tailed_Sandpiper","Shearwater","Shorebird","Shoveler","Shrike",
"Slaty_Backed_Gull","Slender_Billed_Gull","Snipe","Snowy_Owl","Softbill","Sooty_Tern","Sparrow","Spur_Winged_Goose","Starling","Scooter",
"Swiftlet","Sandgrouse","Common_Tern","Thrush","Tree_Sparrow","Tufted_Duck","Tufted_Duck_","Tundra_Swan","Turkey","Turtledove","Velvet_Scoter",
"Wedge_Tailed_Shearwater","Whiskered_Tern","White_Bellied_Bustard","White_Peafowl","White_Rumped_Munia","White_Fronted_Goose","White_Rumped_Sandpiper",
"White_Winged_Scoter","Widgeon","Wild_Chicken","Wild_Duck","Wood_Duck","Yellow_Billed_Duck","Yellow_Billed_Pintail"]

duck = ["American_Black_Duck","Green_Winged_Teal","American_Green_Winged_Teal", "Eurasian_Teal","Mallard","American_Wigeon","American_Widgeon",
"Northern_Pintail","Green_Winged_Teal_","Cinnamon_Teal","Blue_Winged_Teal_","Blue_Winged_Teal","Waterfowl","Australian_Shelduck",
"Pochard","Baikal_Teal","Bantam","Black_Duck","Black_Scoter","Breeder_Duck","Broiler_Duck","Bufflehead","Canvasback","Teal","Yellow_Billed_Teal",
"Common_Eider","Common_Pochard","Common_Scoter","Shelduck","Muscovy_Duck","Eurasian_Wigeon","Gadwall","Garganey","Common_Merganser","Gray_Teal",
"Greater_Scaup","Spot_Billed_Duck","Hooded_Merganser","Lesser_Scaup","Long_Tailed_Duck","Mallard_Duck",
"Mallard_Black_Duck_Hybrid","Smew","Northern_Shoveler","Northern_Shov","Pintail","Pintail_Duck","Red_Crested_Pochard","Red_Billed_Teal",
"Redhead_Duck","Redhead","Ring_Necked_Duck","Rosy_Billed_Pochard","Scaup","Scoter","Shoveler","Scooter","Tufted_Duck","Tufted_Duck_","Velvet_Scoter",
"White_Winged_Scoter","Widgeon","Wild_Duck","Wood_Duck","Yellow_Billed_Duck","Yellow_Billed_Pintail","Common_Goldeneye"]

other = ["Unknown","Insect","Environment","Laboratory_derived","environmment","LAB"]

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
xfull = dataobj.dataToPhoc(xfull,phoclevel,False)

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
knnobj = knn.knn(ksetting,x,y,scipy.spatial.distance.euclidean)

print("testing knn")
correct = 0
close = 0
almost = 0
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
        if (ans[0] in mammal and yi["host"] in mammal) or (ans[0] in bird and yi["host"] in bird):
            almost += 1
            if ans[0] in duck and yi["host"] in duck:
                close += 1
        else:
            results.write("Answer: " + str(ans[0]) + ", reality: " + str(yi["host"]) + ", fasta: " + str(xi) + "\n")
    print("Progress " + str((i/tests)*100) + "%", end='\r', flush=True)
print("                                        ")
print("test complete")
print("Counts- Absolutely correct: " + str(correct) + ", Very close to correct: " + str(close) + ", Almost correct: " + str(almost) + ", Total: " + str(tests))
print("Percentages- Absolute: " + str(correct/tests) + ", Very close: " + str((correct+close)/tests) + ", Almost: " + str((correct+almost)/tests))
print("Settings- k: " + str(ksetting) + ", phoclevel: " + str(phoclevel))